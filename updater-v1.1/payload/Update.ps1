param([switch]$Library, [string]$RenderPreview, [string]$GameFolder)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
Add-Type -AssemblyName System.IO.Compression
$script:Repo = 'Nostramadeus/seraphic-blue-mod'
$script:UpdaterRoot=$PSScriptRoot

function Assert-SafePath([string]$Path) {
    $full = [IO.Path]::GetFullPath($Path)
    if ($full.StartsWith('\\')) { throw 'Choose a local drive, not a network folder.' }
    $part = $full
    while ($part) {
        if (Test-Path -LiteralPath $part) {
            if ((Get-Item -Force -LiteralPath $part).Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw 'Linked folders or files are not supported. Choose a regular game folder.'
            }
        }
        $parent = [IO.Path]::GetDirectoryName($part)
        if ($parent -eq $part) { break }
        $part = $parent
    }
    return $full
}

function Get-Digest([string]$Path) {
    $stream=[IO.File]::OpenRead((Assert-SafePath $Path));$hash=[Security.Cryptography.SHA256]::Create()
    try{return ([BitConverter]::ToString($hash.ComputeHash($stream))).Replace('-','').ToLowerInvariant()}
    finally{$hash.Dispose();$stream.Dispose()}
}

function Get-Installation([string]$Folder) {
    $root = Assert-SafePath $Folder
    $manifestPath = Join-Path $root 'fullgame-manifest.json'
    $null = Assert-SafePath $manifestPath
    $null = Assert-SafePath (Join-Path $root 'RPG_RT.ldb')
    if (!(Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        throw 'Select the game folder containing fullgame-manifest.json. Older patch-only installs need the manual update steps.'
    }
    $manifest = [IO.File]::ReadAllText($manifestPath, [Text.Encoding]::UTF8) | ConvertFrom-Json
    if ($manifest.archive -notmatch '^seraphic-blue-fullgame-(EN-Altered|EN|JP)-(v\d+\.\d+\.\d+)\.zip$') {
        throw 'This installation is not a supported full-game release.'
    }
    $edition = $Matches[1]
    $tag = $Matches[2]
    if ($manifest.release -ne $tag) { throw 'The installation version information does not agree.' }
    $database = @( $manifest.members | Where-Object { $_.file -ceq 'RPG_RT.ldb' } )
    if ($database.Count -ne 1 -or (Get-Digest (Join-Path $root 'RPG_RT.ldb')) -cne $database[0].sha256) {
        throw 'The game database differs from its release manifest. Use a fresh matching-edition download.'
    }
    $launcher = Join-Path $root 'PLAY.cmd'
    $null = Assert-SafePath $launcher
    if (!(Test-Path -LiteralPath $launcher -PathType Leaf)) { throw 'PLAY.cmd is missing.' }
    $launchText = [IO.File]::ReadAllText($launcher)
    if ($launchText -notmatch '--save-path\s+"saves"' -or $launchText -notmatch '--config-path\s+"config"') {
        throw 'This launcher uses a custom save/config location. Use the manual update steps so the correct saves are copied.'
    }
    return [pscustomobject]@{ Root=$root; Edition=$edition; Tag=$tag }
}

function Get-LatestRelease([ValidateRange(1,300)][int]$TimeoutSeconds = 30) {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $release = Invoke-RestMethod -Uri ('https://api.github.com/repos/' + $script:Repo + '/releases/latest') -Headers @{ 'User-Agent'='SeraphicBlue-Updater'; Accept='application/vnd.github+json' } -TimeoutSec $TimeoutSeconds -UseBasicParsing
    if ($release.draft -or $release.prerelease -or $release.tag_name -notmatch '^v\d+\.\d+\.\d+$') {
        throw 'A stable release could not be identified.'
    }
    return $release
}

function Get-SaveSnapshot([string]$Root) {
    $snapshot = @{}
    foreach ($name in @('saves', 'config')) {
        $folder = Join-Path $Root $name
        if (!(Test-Path -LiteralPath $folder)) { continue }
        $null = Assert-SafePath $folder
        $pending = [Collections.Generic.Stack[string]]::new()
        $pending.Push($folder)
        while ($pending.Count) {
            foreach ($entry in @(Get-ChildItem -Force -LiteralPath $pending.Pop())) {
                $null = Assert-SafePath $entry.FullName
                $relative = $entry.FullName.Substring($Root.Length + 1)
                $sidecar=$relative -in @('saves\sb-repeat-a.json','saves\sb-repeat-b.json')
                if($sidecar -and ($entry.PSIsContainer -or $entry.Length-gt 8MB)){throw 'A repeat-command sidecar must be a regular file of at most 8 MiB.'}
                if ($entry.PSIsContainer) { $pending.Push($entry.FullName) }
                else {
                    $digest=Get-Digest $entry.FullName
                    if($snapshot.ContainsKey($relative) -and $snapshot[$relative]-cne $digest){throw 'Conflicting case aliases in personal data.'}
                    $snapshot[$relative] = $digest
                }
            }
        }
    }
    # Old full-game copies may still have root-level saves. Never choose between two different copies silently.
    foreach ($entry in @(Get-ChildItem -Force -LiteralPath $Root | Where-Object { $_.Name -match '^Save\d+\.lsd$' -or $_.Name -in @('sb-repeat-a.json','sb-repeat-b.json') })) {
        $null = Assert-SafePath $entry.FullName
        if($entry.PSIsContainer){throw 'A known root save or repeat sidecar is not a regular file.'}
        if ($entry.Name -in @('sb-repeat-a.json','sb-repeat-b.json') -and $entry.Length -gt 8MB) { throw 'A repeat-command sidecar exceeds its 8 MiB limit.' }
        $relative = 'saves\' + $entry.Name
        $digest = Get-Digest $entry.FullName
        if ($snapshot.ContainsKey($relative) -and $snapshot[$relative] -cne $digest) {
            throw 'Different saves with the same name exist in the game folder and saves folder. Resolve this before updating.'
        }
        $snapshot['root:' + $entry.Name] = $digest
    }
    $null=Get-NormalizedSnapshot $snapshot
    return $snapshot
}

function Get-PersonalRelative([string]$Key) {
    $relative=if($Key.StartsWith('root:')){'saves\'+$Key.Substring(5)}else{$Key}
    if($relative -in @('saves\sb-repeat-a.json','saves\sb-repeat-b.json')){return $relative.ToLowerInvariant()}
    return $relative
}

function Assert-SnapshotEqual($Before, $After) {
    if ($Before.Count -ne $After.Count) { throw 'Saves or settings changed. Close the game and try again.' }
    foreach ($key in $Before.Keys) {
        if (!$After.ContainsKey($key) -or $Before[$key] -cne $After[$key]) {
            throw 'Saves or settings changed. Close the game and try again.'
        }
    }
}

function Get-NormalizedSnapshot($Snapshot) {
    $normalized = @{}
    foreach ($key in $Snapshot.Keys) {
        $relative = Get-PersonalRelative $key
        if ($normalized.ContainsKey($relative) -and $normalized[$relative] -cne $Snapshot[$key]) { throw 'Conflicting save snapshot.' }
        $normalized[$relative] = $Snapshot[$key]
    }
    return $normalized
}

function Get-AvailableSpace([string]$Path) {
    $root = [IO.Path]::GetPathRoot((Assert-SafePath $Path))
    return [IO.DriveInfo]::new($root).AvailableFreeSpace
}

function Get-RoundedAllocation([long]$Bytes) {
    if ($Bytes -lt 0) { throw 'Invalid file size.' }
    return [long]([decimal]::Ceiling(([decimal]$Bytes / 65536)) * 65536)
}

function Assert-FreeSpace([string]$Path, [decimal]$Required) {
    if ($Required -lt 0 -or $Required -gt [long]::MaxValue) { throw 'Invalid required disk space.' }
    $available = Get-AvailableSpace $Path
    if ($available -lt $Required) { throw 'Not enough free disk space. The old game was not changed.' }
}

function Assert-DownloadSpace([string]$Path, [long]$AssetBytes) {
    if ($AssetBytes -le 0) { throw 'The download size is unavailable.' }
    Assert-FreeSpace $Path ([decimal]$AssetBytes + 128MB)
}

function Get-PersonalAllocation([string]$Root, $Snapshot) {
    $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    $total = [decimal]0
    foreach ($key in $Snapshot.Keys) {
        $relative = Get-PersonalRelative $key; $source = Join-Path $Root $key
        if ($key.StartsWith('root:')) { $source=Join-Path $Root $key.Substring(5) }
        if ($seen.Add($relative)) { $total += Get-RoundedAllocation (Get-Item -Force -LiteralPath $source).Length }
    }
    return $total
}

function Get-ReleaseAsset($Old, $Release) {
    if ($Release.draft -or $Release.prerelease -or $Release.tag_name -notmatch '^v\d+\.\d+\.\d+$') { throw 'A stable release could not be identified.' }
    if ([version]$Release.tag_name.Substring(1) -le [version]$Old.Tag.Substring(1)) { return $null }
    $name='seraphic-blue-fullgame-'+$Old.Edition+'-'+$Release.tag_name+'.zip'
    $assets=@($Release.assets | Where-Object { $_.name -ceq $name -and $_.state -eq 'uploaded' })
    if ($assets.Count -ne 1 -or $assets[0].digest -cnotmatch '^sha256:([a-f0-9]{64})$') { throw 'The matching download/checksum is unavailable.' }
    $digest=$Matches[1]
    $url='https://github.com/'+$script:Repo+'/releases/download/'+$Release.tag_name+'/'+$name
    if ([string]$assets[0].browser_download_url -cne $url -or [long]$assets[0].size -le 0) { throw 'Unexpected download address or size.' }
    return [pscustomobject]@{ Name=$name; URL=$url; Digest=$digest; Bytes=[long]$assets[0].size; Tag=$Release.tag_name }
}

function Invoke-StartupInstaller([string]$Folder,[ValidateSet('State','Enable','Disable')][string]$Mode) {
    $installer=Assert-SafePath (Join-Path $script:UpdaterRoot 'Install-startup-checks.ps1')
    if(!(Test-Path -LiteralPath $installer -PathType Leaf)){throw 'Startup installer is missing. Keep the complete updater folder together.'}
    $info=[Diagnostics.ProcessStartInfo]::new()
    $info.FileName=Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
    $info.Arguments='-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "'+$installer+'" -GameFolder "'+(Assert-SafePath $Folder)+'"'
    if($Mode -ceq 'State'){$info.Arguments+=' -StateOnly'}elseif($Mode -ceq 'Disable'){$info.Arguments+=' -Disable'}
    $info.UseShellExecute=$false;$info.CreateNoWindow=$true;$info.WindowStyle='Hidden';$info.RedirectStandardOutput=$true;$info.RedirectStandardError=$true
    $process=[Diagnostics.Process]::new();$process.StartInfo=$info;$started=$false
    try{
        $started=$process.Start();if(!$started){throw 'Startup installer could not start.'}
        $stdout=$process.StandardOutput.ReadToEndAsync();$stderr=$process.StandardError.ReadToEndAsync()
        if(!$process.WaitForExit(30000)){try{$process.Kill()}catch{};throw 'Startup installer timed out; current game retained.'}
        $text=$stdout.GetAwaiter().GetResult().Trim();$errorText=$stderr.GetAwaiter().GetResult().Trim()
        if($process.ExitCode-ne 0){throw ('Startup checks unavailable: '+$errorText)}
        return $text
    }finally{if($started -and !$process.HasExited){try{$process.Kill()}catch{}};$process.Dispose()}
}

function Start-UpdatedGame([string]$Folder,[switch]$KeepStartup) {
    if($KeepStartup){$null=Invoke-StartupInstaller $Folder 'Enable'}
    # Startup wrappers skip the check when custom launch arguments are supplied.
    $null = Assert-SafePath (Join-Path $Folder 'Player.exe')
    foreach ($name in @('saves','config')) { $directory=Assert-SafePath (Join-Path $Folder $name); [IO.Directory]::CreateDirectory($directory) | Out-Null }
    Start-Process -FilePath (Join-Path $Folder 'Player.exe') -WorkingDirectory $Folder -ArgumentList '--project-path "." --save-path "saves" --config-path "config" --encoding 932 --window' -ErrorAction Stop | Out-Null
}

function Expand-CheckedArchive([string]$Archive, [string]$Destination, [string]$Edition, [string]$Tag, [switch]$ValidateOnly) {
    $prefix = 'SeraphicBlue/'
    if ($Edition -eq 'EN-Altered') { $prefix = 'SeraphicBlue-Altered/' }
    $zip = [IO.Compression.ZipFile]::OpenRead($Archive)
    try {
        $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
        $total = [long]0
        $allocated = [decimal]0
        foreach ($entry in $zip.Entries) {
            $name = $entry.FullName
            if (!$name.EndsWith('/')) { $allocated += Get-RoundedAllocation $entry.Length }
            if ($name -eq 'IMPORTANT README (MUST READ).txt') { continue }
            if (!$name.StartsWith($prefix, [StringComparison]::Ordinal) -or $name.Contains('\') -or $name.Contains(':')) {
                throw 'Unexpected archive path.'
            }
            $relative = $name.Substring($prefix.Length)
            if (!$relative) { continue }
            if ($relative.Split('/') -contains '..' -or $relative.StartsWith('/')) { throw 'Unsafe archive path.' }
            foreach ($part in $relative.TrimEnd('/').Split('/')) {
                if (!$part -or $part -eq '.' -or $part -match '[<>|?*"\x00-\x1f]' -or $part -match '[. ]$' -or $part -match '^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$') {
                    throw 'Archive path is not a regular Windows filename.'
                }
            }
            if (($entry.ExternalAttributes -shr 16 -band 61440) -eq 40960) { throw 'Linked archive entries are not supported.' }
            if ($relative.EndsWith('/')) { continue }
            if (!$seen.Add($relative)) { throw 'Duplicate archive entry.' }
            if ($relative -match '^(saves|config)/|(^|/)Save\d+\.lsd$|(^|/)sb-repeat-[ab]\.json$') { throw 'A release must not contain personal saves, repeat sidecars or config.' }
            $total += $entry.Length
            if ($total -gt 8GB) { throw 'The expanded release is unexpectedly large.' }
            $target = [IO.Path]::GetFullPath((Join-Path $Destination $relative))
            if (!$target.StartsWith($Destination + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Archive path escapes the new folder.' }
        }
        if ($ValidateOnly) { return [pscustomobject]@{ Allocation=$allocated } }
        foreach ($entry in $zip.Entries) {
            if (!$entry.FullName.StartsWith($prefix, [StringComparison]::Ordinal)) { continue }
            $relative = $entry.FullName.Substring($prefix.Length)
            if (!$relative -or $relative.EndsWith('/')) { continue }
            $target = Join-Path $Destination $relative
            $lease=Get-DestinationLease ([IO.Path]::GetDirectoryName($target))
            try {
                $null=Assert-SafePath $target
                $inputStream = $entry.Open()
                try{$outputStream = [IO.File]::Open($target, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
                    try { $inputStream.CopyTo($outputStream) } finally { $outputStream.Dispose() }
                }finally{$inputStream.Dispose()}
            }finally{$lease.Dispose()}
        }
    } finally { $zip.Dispose() }
    $manifest = [IO.File]::ReadAllText((Join-Path $Destination 'fullgame-manifest.json'), [Text.Encoding]::UTF8) | ConvertFrom-Json
    if ($manifest.archive -cne ('seraphic-blue-fullgame-' + $Edition + '-' + $Tag + '.zip') -or $manifest.release -cne $Tag) { throw 'The downloaded edition/version does not match.' }
    $declared = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    foreach ($member in $manifest.members) {
        if (!$declared.Add([string]$member.file) -or !$seen.Contains([string]$member.file) -or $member.sha256 -cnotmatch '^[a-f0-9]{64}$' -or [long]$member.bytes -lt 0) { throw 'A release manifest member is invalid, duplicated or missing.' }
        $file = Join-Path $Destination $member.file
        if ((Get-Item -LiteralPath $file).Length -ne $member.bytes -or (Get-Digest $file) -cne $member.sha256) { throw 'An extracted release file failed verification.' }
    }
    foreach ($required in @('RPG_RT.ldb', 'RPG_RT.lmt', 'RPG_RT.ini', 'Map0001.lmu', 'EasyRPG.ini', 'Player.exe', 'PLAY.cmd')) {
        $file = Join-Path $Destination $required
        if (!$declared.Contains($required) -or !(Test-Path -LiteralPath $file -PathType Leaf) -or (Get-Item -LiteralPath $file).Length -le 0) { throw 'The new release is incomplete.' }
    }
    foreach ($name in $seen) {
        if ($name -notin @('fullgame-manifest.json', 'SHA256SUMS') -and !$declared.Contains($name)) { throw 'An extracted file is absent from the release manifest.' }
    }
}

function Get-DestinationLease([string]$Directory) {
    $null=Assert-SafePath $Directory
    if(!('StartupSafeDirectory' -as [type])){Add-Type -Path (Join-Path $script:UpdaterRoot 'SafeWrite.cs')}
    return [StartupSafeDirectory]::Acquire($Directory)
}

function Copy-PersonalData([string]$Source, [string]$Destination, $Snapshot) {
    foreach ($key in $Snapshot.Keys) {
        $relative = Get-PersonalRelative $key
        if ($key.StartsWith('root:')) {
            $sourcePath = Join-Path $Source $key.Substring(5)
        } else { $sourcePath = Join-Path $Source $key }
        $target = Join-Path $Destination $relative
        $lease=Get-DestinationLease ([IO.Path]::GetDirectoryName($target))
        try{
            $null=Assert-SafePath $target;$null=Assert-SafePath $sourcePath
            if (Test-Path -LiteralPath $target) {
                if ((Get-Digest $target) -cne $Snapshot[$key]) { throw 'Personal data destination conflicts.' }
            }else{
                $inputStream=[IO.File]::OpenRead($sourcePath)
                try{$outputStream=[IO.File]::Open($target,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
                    try{$inputStream.CopyTo($outputStream)}finally{$outputStream.Dispose()}
                }finally{$inputStream.Dispose()}
            }
            if ((Get-Digest $target) -cne $Snapshot[$key] -or (Get-Digest $sourcePath) -cne $Snapshot[$key]) { throw 'A save/settings copy failed verification.' }
        }finally{$lease.Dispose()}
    }
}

function Install-VerifiedUpdate([string]$OldFolder, [string]$Archive, [string]$ExpectedSHA256, [string]$Tag, [scriptblock]$Status = {}) {
    $old = Get-Installation $OldFolder
    if ($Tag -notmatch '^v\d+\.\d+\.\d+$' -or $ExpectedSHA256 -notmatch '^[a-f0-9]{64}$') { throw 'Invalid release metadata.' }
    if ($old.Tag -eq $Tag) { throw ('This copy already has ' + $Tag + '.') }
    if ([version]$Tag.Substring(1) -lt [version]$old.Tag.Substring(1)) { throw 'The available release is older than this installation. No downgrade was performed.' }
    & $Status 'Verifying the download...'
    if ((Get-Digest $Archive) -cne $ExpectedSHA256) { throw 'Download checksum mismatch. The old game was not changed.' }
    $parent = [IO.Path]::GetDirectoryName($old.Root)
    $output = Join-Path $parent ('SeraphicBlue-' + $old.Edition + '-' + $Tag)
    $stage = $output + '.partial-' + [Guid]::NewGuid().ToString('N')
    $backup = $output + '.save-backup-' + [Guid]::NewGuid().ToString('N')
    $null = Assert-SafePath $output
    if (Test-Path -LiteralPath $output) { throw 'The destination version folder already exists. Nothing was overwritten.' }
    $before = Get-SaveSnapshot $old.Root
    $expectedPersonal = Get-NormalizedSnapshot $before
    & $Status 'Checking archive paths and free space...'
    $plan = Expand-CheckedArchive $Archive $stage $old.Edition $Tag -ValidateOnly
    $personalAllocation = Get-PersonalAllocation $old.Root $before
    Assert-FreeSpace $parent ($plan.Allocation + 2*$personalAllocation + 128MB)
    Assert-SnapshotEqual $before (Get-SaveSnapshot $old.Root)
    try {
        & $Status 'Making a verified save/settings backup...'
        [IO.Directory]::CreateDirectory($backup) | Out-Null
        Copy-PersonalData $old.Root $backup $before
        Assert-SnapshotEqual $expectedPersonal (Get-SaveSnapshot $backup)
        Assert-SnapshotEqual $before (Get-SaveSnapshot $old.Root)
        & $Status 'Extracting and checking the new game...'
        Expand-CheckedArchive $Archive $stage $old.Edition $Tag
        if ((Get-Digest $Archive) -cne $ExpectedSHA256) { throw 'The download changed during extraction.' }
        & $Status 'Copying saves and settings...'
        # Copy from the verified snapshot backup, whose root-level saves have already been migrated.
        $backupSnapshot = Get-SaveSnapshot $backup
        Assert-SnapshotEqual $expectedPersonal $backupSnapshot
        Copy-PersonalData $backup $stage $backupSnapshot
        Assert-SnapshotEqual $before (Get-SaveSnapshot $old.Root)
        Assert-SnapshotEqual $expectedPersonal (Get-SaveSnapshot $backup)
        Assert-SnapshotEqual $expectedPersonal (Get-SaveSnapshot $stage)
        [IO.Directory]::Move($stage, $output)
    } catch {
        $failure = $_
        if (Test-Path -LiteralPath $stage -PathType Container) {
            try {
                $lease=Get-DestinationLease $stage
                try{$marker=Assert-SafePath (Join-Path $stage 'UPDATE-INCOMPLETE.txt');$stream=[IO.File]::Open($marker,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
                    try{$bytes=[Text.Encoding]::UTF8.GetBytes("Update failed. Do not play this partial copy. Your old game and backup are retained.`n");$stream.Write($bytes,0,$bytes.Length)}finally{$stream.Dispose()}
                }finally{$lease.Dispose()}
            } catch { }
        }
        if (($failure.Exception.HResult -band 65535) -in @(39,112)) { throw 'The disk filled during the update. The old game and retained backup were not overwritten.' }
        throw $failure
    }
    return [pscustomobject]@{ Folder=$output; Backup=$backup; Edition=$old.Edition; Tag=$Tag }
}

function Show-Updater([string]$Preview, [string]$InitialGameFolder, $KnownRelease=$null, [switch]$Startup) {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $form = [Windows.Forms.Form]::new()
    $form.Text = 'Seraphic Blue - Update'
    $form.ClientSize = [Drawing.Size]::new(660, 420)
    $form.StartPosition = 'CenterScreen'
    $form.Font = [Drawing.Font]::new('Segoe UI', 11)
    $form.FormBorderStyle = 'FixedDialog'
    $form.MaximizeBox = $false
    $title = [Windows.Forms.Label]::new(); $title.Text='Update Seraphic Blue'; $title.SetBounds(24,20,610,36); $title.Font=[Drawing.Font]::new('Segoe UI',18,[Drawing.FontStyle]::Bold)
    $help = [Windows.Forms.Label]::new(); $help.Text="Close the game first. Select the old game folder.`nA new copy will receive your saves and settings. The old copy is kept."; $help.SetBounds(24,65,610,60)
    $path = [Windows.Forms.TextBox]::new(); $path.SetBounds(24,139,495,30); $path.ReadOnly=$true
    $choose = [Windows.Forms.Button]::new(); $choose.Text='Choose...'; $choose.SetBounds(532,137,104,34)
    $status = [Windows.Forms.Label]::new(); $status.Text='Choose the folder containing PLAY.cmd.'; $status.SetBounds(24,188,610,66)
    $startupAction=[Windows.Forms.Button]::new();$startupAction.Text='Enable startup checks';$startupAction.SetBounds(24,276,436,42);$startupAction.Enabled=$false
    $update = [Windows.Forms.Button]::new(); $update.Text='Update to latest'; $update.SetBounds(24,346,208,42); $update.Enabled=$false
    $play = [Windows.Forms.Button]::new(); $play.Text='Play updated copy'; $play.SetBounds(252,346,208,42); $play.Visible=$false
    $close = [Windows.Forms.Button]::new(); $close.Text='Close'; $close.SetBounds(532,346,104,42)
    $form.Controls.AddRange(@($title,$help,$path,$choose,$status,$startupAction,$update,$play,$close))
    $state = @{ Result=$null; Busy=$false; Launched=$false; Failed=$false }
    $refreshStartup={
        $startupAction.Enabled=$false
        if($Startup -or $state.Busy -or !$path.Text){return}
        try{
            $startupState=Invoke-StartupInstaller $path.Text 'State'
            if($startupState -cnotin @('Enabled','Disabled')){throw 'Unknown startup state.'}
            $state.StartupEnabled=($startupState-ceq 'Enabled')
            $startupAction.Text=if($state.StartupEnabled){'Disable startup checks'}else{'Enable startup checks'}
            $startupAction.Enabled=$true
        }catch{$startupAction.Text='Startup checks unavailable for this folder'}
    }
    if ($InitialGameFolder) {
        try { $initial=Get-Installation $InitialGameFolder; $path.Text=$initial.Root; $status.Text=$initial.Edition+' / '+$initial.Tag+'. Ready to update.'; $update.Enabled=$true }
        catch { $status.Text=$_.Exception.Message; $state.Failed=$true }
    }
    & $refreshStartup
    $choose.Add_Click({
        $dialog=[Windows.Forms.FolderBrowserDialog]::new(); $dialog.Description='Select the old Seraphic Blue game folder'; $dialog.ShowNewFolderButton=$false
        if ($dialog.ShowDialog($form) -eq 'OK') {
            try { $install=Get-Installation $dialog.SelectedPath; $path.Text=$install.Root; $status.Text=$install.Edition + ' / ' + $install.Tag + '. Ready to check for an update.'; $update.Enabled=$true; $play.Visible=$false; & $refreshStartup }
            catch { $status.Text=$_.Exception.Message; $update.Enabled=$false; $startupAction.Enabled=$false }
        }
        $dialog.Dispose()
    })
    $startupAction.Add_Click({
        $state.Busy=$true;$startupAction.Enabled=$false;$choose.Enabled=$false;$update.Enabled=$false;$close.Enabled=$false
        try{
            $mode=if($state.StartupEnabled){'Disable'}else{'Enable'}
            $null=Invoke-StartupInstaller $path.Text $mode
            $status.Text=if($mode-ceq 'Enable'){'Startup checks enabled. Open PLAY.cmd to check before playing.'}else{'Startup checks disabled. The original launcher was restored.'}
        }catch{$status.Text=$_.Exception.Message}
        finally{$state.Busy=$false;$choose.Enabled=$true;$close.Enabled=$true;$update.Enabled=($null-eq $state.Result);& $refreshStartup}
    })
    $update.Add_Click({
        $state.Busy=$true; $choose.Enabled=$false; $update.Enabled=$false; $close.Enabled=$false;$startupAction.Enabled=$false
        try {
            $progress={ param($message) $status.Text=$message; $form.Refresh(); [Windows.Forms.Application]::DoEvents() }
            & $progress 'Checking the latest stable release...'
            $old=Get-Installation $path.Text; $release=$KnownRelease
            if (!$release) { $release=Get-LatestRelease }
            if ($old.Tag -eq $release.tag_name) { $status.Text='You already have the latest release: ' + $old.Tag; return }
            if ([version]$release.tag_name.Substring(1) -lt [version]$old.Tag.Substring(1)) { throw 'The available release is older than this installation. No downgrade was performed.' }
            $asset=Get-ReleaseAsset $old $release
            if (!$asset) { throw 'No newer matching release is available.' }
            $assetName=$asset.Name; $expected=$asset.Digest; $url=$asset.URL
            Assert-DownloadSpace ([IO.Path]::GetDirectoryName($old.Root)) $asset.Bytes
            $cache=Join-Path ([IO.Path]::GetDirectoryName($old.Root)) ('.sb-update-download-' + [Guid]::NewGuid().ToString('N'))
            [IO.Directory]::CreateDirectory($cache) | Out-Null
            $download=Join-Path $cache $assetName
            & $progress 'Downloading the full update. This window may wait while the download finishes...'
            $client=[Net.WebClient]::new()
            try {
                $client.Headers['User-Agent']='SeraphicBlue-Updater'
                $task=$client.DownloadFileTaskAsync([Uri]$url,$download)
                while (!$task.IsCompleted) { [Windows.Forms.Application]::DoEvents(); Start-Sleep -Milliseconds 100 }
                $task.GetAwaiter().GetResult()
            } finally { $client.Dispose() }
            if ((Get-Item -LiteralPath $download).Length -ne $asset.Bytes) { throw 'The downloaded size does not match the release.' }
            $state.Result=Install-VerifiedUpdate $old.Root $download $expected $release.tag_name $progress
            $status.Text='Updated to ' + $state.Result.Tag + ". Saves/settings verified.`nNew copy: " + $state.Result.Folder
            $play.Visible=$true
            if ($Startup) { Start-UpdatedGame $state.Result.Folder -KeepStartup; $state.Launched=$true; $state.Busy=$false; $form.Close() }
        } catch { $status.Text='Update stopped: ' + $_.Exception.Message; $state.Failed=$true; if ($Startup) { $state.Busy=$false; $form.Close() } }
        finally { $state.Busy=$false; $choose.Enabled=$true; $close.Enabled=$true; $update.Enabled=($null -eq $state.Result);& $refreshStartup }
    })
    $play.Add_Click({ if ($state.Result) { Start-UpdatedGame $state.Result.Folder; $state.Launched=$true; $form.Close() } })
    $close.Add_Click({ $form.Close() })
    $form.Add_FormClosing({ param($sender,$eventArgs) if ($state.Busy) { $eventArgs.Cancel=$true } })
    if ($Startup) {
        $choose.Enabled=$false
        $help.Text="Installing into a neighboring version folder. Your old game is kept.`nOn any update error, the current game will open."
        $form.Add_Shown({ if ($state.Failed) { $form.Close() } else { $update.PerformClick() } })
    }
    if ($Preview) {
        if ($env:SB_UPDATER_HIDDEN_PREVIEW -ne '1') { throw 'Preview rendering requires the private hidden-desktop test runner.' }
        $path.Text='D:\Games\SeraphicBlue-Altered'; $update.Enabled=$true
        $form.Show(); [Windows.Forms.Application]::DoEvents(); Start-Sleep -Milliseconds 700
        $bitmap=[Drawing.Bitmap]::new($form.Width,$form.Height)
        $form.DrawToBitmap($bitmap,[Drawing.Rectangle]::new(0,0,$form.Width,$form.Height)); $bitmap.Save($Preview); $bitmap.Dispose(); $form.Dispose()
    } else { [Windows.Forms.Application]::EnableVisualStyles(); [void]$form.ShowDialog(); $form.Dispose() }
    return $state.Launched
}

if (!$Library) { $null = Show-Updater $RenderPreview $GameFolder }
