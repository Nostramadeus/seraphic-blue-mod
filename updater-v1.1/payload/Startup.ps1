param([string]$GameFolder, [switch]$Library)
$ErrorActionPreference='Stop'
$runStartup=!$Library
$script:StartupRoot=$PSScriptRoot
$script:RequestedGameFolder=$GameFolder
. "$PSScriptRoot/Update.ps1" -Library

function Get-BoundedRelease([int]$Milliseconds=3000) {
    $info=[Diagnostics.ProcessStartInfo]::new()
    $info.FileName=Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
    if (!(Test-Path -LiteralPath $info.FileName -PathType Leaf)) { return $null }
    $info.Arguments='-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "'+(Join-Path $script:StartupRoot 'CheckRelease.ps1')+'" -TimeoutSeconds 3'
    $info.UseShellExecute=$false; $info.CreateNoWindow=$true; $info.WindowStyle='Hidden'
    $info.RedirectStandardOutput=$true; $info.RedirectStandardError=$true
    $process=[Diagnostics.Process]::new(); $process.StartInfo=$info
    $clock=[Diagnostics.Stopwatch]::StartNew(); $started=$false
    try {
        $started=$process.Start()
        if (!$started) { return $null }
        $stdout=$process.StandardOutput.ReadToEndAsync(); $stderr=$process.StandardError.ReadToEndAsync()
        $remaining=[Math]::Max(0,$Milliseconds-[int]$clock.ElapsedMilliseconds)
        if (!$process.WaitForExit($remaining)) { try { $process.Kill() } catch { }; return $null }
        if ($process.ExitCode -ne 0 -or !$stdout.IsCompleted) { return $null }
        return ($stdout.GetAwaiter().GetResult() | ConvertFrom-Json)
    } finally { if ($started -and !$process.HasExited) { try { $process.Kill() } catch { } }; $process.Dispose() }
}

function Confirm-StartupUpdate($Old, $Asset) {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $form=[Windows.Forms.Form]::new(); $form.Text='Seraphic Blue - Update available'
    $form.ClientSize=[Drawing.Size]::new(580,230); $form.StartPosition='CenterScreen'; $form.FormBorderStyle='FixedDialog'; $form.MaximizeBox=$false; $form.MinimizeBox=$false
    $form.Font=[Drawing.Font]::new('Segoe UI',11)
    $text=[Windows.Forms.Label]::new(); $text.SetBounds(24,24,532,110)
    $text.Text='A newer '+$Old.Edition+' release is available: '+$Asset.Tag+".`nInstall into a new folder and open it when ready?`nThe current game and a save/settings backup are kept."
    $install=[Windows.Forms.Button]::new(); $install.Text='Install update'; $install.SetBounds(24,160,250,44); $install.DialogResult='Yes'
    $current=[Windows.Forms.Button]::new(); $current.Text='Play current'; $current.SetBounds(306,160,250,44); $current.DialogResult='No'
    $form.Controls.AddRange(@($text,$install,$current)); $form.AcceptButton=$current; $form.CancelButton=$current
    $current.TabIndex=0; $install.TabIndex=1; $form.ActiveControl=$current
    try { return ($form.ShowDialog() -eq 'Yes') } finally { $form.Dispose() }
}

function Invoke-StartupUpdate([string]$Folder) {
    try {
        $old=Get-Installation $Folder
        $release=Get-BoundedRelease
        if (!$release) { return 0 }
        $asset=Get-ReleaseAsset $old $release
        if (!$asset) { return 0 }
        # Missing Forms/GUI errors are caught before suppressing the current launch.
        if (!(Confirm-StartupUpdate $old $asset)) { return 0 }
        if (Show-Updater '' $old.Root $release -Startup) { return 10 }
    } catch { }
    return 0
}

if ($runStartup) { exit (Invoke-StartupUpdate $script:RequestedGameFolder) }
