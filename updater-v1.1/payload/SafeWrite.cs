using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Runtime.InteropServices;
using Microsoft.Win32.SafeHandles;

// Deny write/delete opens on each directory while a destination file is open.
// OPEN_REPARSE_POINT checks the directory itself, not the target of a junction.
public sealed class StartupSafeDirectory : IDisposable {
    [StructLayout(LayoutKind.Sequential)]
    private struct Information {
        public uint Attributes, CreatedLow, CreatedHigh, AccessLow, AccessHigh;
        public uint WrittenLow, WrittenHigh, Volume, SizeHigh, SizeLow, Links, IndexHigh, IndexLow;
    }
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    private static extern SafeFileHandle CreateFile(string name, uint access, uint share,
        IntPtr security, uint creation, uint flags, IntPtr template);
    [DllImport("kernel32.dll", SetLastError=true)]
    private static extern bool GetFileInformationByHandle(SafeFileHandle file, out Information information);
    private readonly List<SafeFileHandle> handles = new List<SafeFileHandle>();

    private void Hold(string path) {
        SafeFileHandle handle = CreateFile(path, 0x80000000, 1, IntPtr.Zero, 3, 0x02200000, IntPtr.Zero);
        if (handle.IsInvalid) { handle.Dispose(); throw new Win32Exception(Marshal.GetLastWin32Error()); }
        try {
            Information information;
            if (!GetFileInformationByHandle(handle, out information)) throw new Win32Exception(Marshal.GetLastWin32Error());
            if ((information.Attributes & 0x400) != 0 || (information.Attributes & 0x10) == 0)
                throw new IOException("Destination contains a linked or non-directory path.");
            handles.Add(handle);
        } catch { handle.Dispose(); throw; }
    }
    public static StartupSafeDirectory Acquire(string directory) {
        var lease = new StartupSafeDirectory();
        try {
            string full = Path.GetFullPath(directory);
            if (full.StartsWith(@"\\")) throw new IOException("Destination must be local.");
            string current = Path.GetPathRoot(full);
            lease.Hold(current);
            foreach (string part in full.Substring(current.Length).Split(new char[] {'\\', '/'}, StringSplitOptions.RemoveEmptyEntries)) {
                current = Path.Combine(current, part);
                // Parent handles remain held while this single next level is made/opened.
                if (!Directory.Exists(current)) Directory.CreateDirectory(current);
                lease.Hold(current);
            }
            return lease;
        } catch { lease.Dispose(); throw; }
    }
    public void Dispose() {
        for (int i=handles.Count-1; i>=0; --i) handles[i].Dispose();
        handles.Clear();
    }
}
