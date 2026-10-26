using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

[assembly: AssemblyTitle("Seraphic Blue Startup Update Settings")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

internal static class Launcher {
    [STAThread]
    private static void Main() {
        try {
            string folder = AppDomain.CurrentDomain.BaseDirectory;
            string script = Path.Combine(folder, "payload", "Update.ps1");
            if (!File.Exists(script)) throw new IOException("Keep the complete updater folder together. Extract the ZIP first.");
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System), @"WindowsPowerShell\v1.0\powershell.exe");
            start.Arguments = "-NoLogo -NoProfile -STA -ExecutionPolicy Bypass -File \"" + script + "\"";
            start.WorkingDirectory = folder;
            start.UseShellExecute = false;
            start.CreateNoWindow = true;
            start.WindowStyle = ProcessWindowStyle.Hidden;
            Process.Start(start);
        } catch (Exception error) {
            MessageBox.Show(error.Message, "Seraphic Blue Updater", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
