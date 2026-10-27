# Regression test for the 2026-10-27 "property 'Text' cannot be found" bug.
# Drives Install-VerifiedUpdate with the same $progress closure the GUI uses ($status Label, $form),
# without showing any window. Usage: test_gui_status.ps1 -Script <Update.ps1> -Game <old folder> -Zip <full game zip> -Sha <hex> -Tag vX.Y.Z
param([string]$Script, [string]$Game, [string]$Zip, [string]$Sha, [string]$Tag)
$ErrorActionPreference = 'Stop'
. $Script -Library
Add-Type -AssemblyName System.Windows.Forms
$form = [Windows.Forms.Form]::new()
$status = [Windows.Forms.Label]::new()
$seen = [Collections.Generic.List[string]]::new()
$progress = { param($message) $status.Text=$message; $seen.Add($message); $form.Refresh(); [Windows.Forms.Application]::DoEvents() }
try {
    $result = Install-VerifiedUpdate $Game $Zip $Sha $Tag $progress
    'PASS: ' + $result.Folder
    'Status messages: ' + ($seen -join ' | ')
    exit 0
} catch {
    'FAIL: ' + $_.Exception.Message
    exit 1
} finally { $form.Dispose() }
