param([Parameter(Mandatory=$true)][string]$GameFolder,[switch]$Disable,[switch]$StateOnly)
$ErrorActionPreference='Stop'
$installerRoot=$PSScriptRoot; $requestedFolder=$GameFolder
$payload=if(Test-Path -LiteralPath (Join-Path $installerRoot 'payload/Update.ps1')){Join-Path $installerRoot 'payload'}else{$installerRoot}
. (Join-Path $payload 'Update.ps1') -Library
$standard='4e580185c1b511a19b2aa785310a72f54d46140b665e3e142cfdd6d0da0941ad'
$old=Get-Installation $requestedFolder
$launcher=Join-Path $old.Root 'PLAY.cmd'; $backup=Join-Path $old.Root 'PLAY.pre-startup.cmd'
$wrapper=if($payload -ceq $installerRoot){Join-Path $payload 'PLAY.startup.cmd'}else{Join-Path $installerRoot 'launchers/PLAY.cmd'}
$bundleFile=Join-Path $payload 'FILES.json'; $bundle=[IO.File]::ReadAllText($bundleFile,[Text.Encoding]::UTF8) | ConvertFrom-Json
$helper=Join-Path $old.Root '.sb-startup-updates'
$allowed=@('FILES.json')+@($bundle.files.PSObject.Properties.Name)
function Assert-Bundle([string]$Directory) {
    $null=Assert-SafePath $Directory
    $actual=@(Get-ChildItem -Force -LiteralPath $Directory)
    if ($actual.Count -ne $allowed.Count) { throw 'Unknown or modified helper directory. Nothing was overwritten.' }
    foreach($entry in $actual) {
        $null=Assert-SafePath $entry.FullName
        if($entry.PSIsContainer -or $entry.Name -cnotin $allowed) { throw 'Unknown helper files. Nothing was overwritten.' }
        $expected=if($entry.Name -ceq 'FILES.json'){Get-Digest $bundleFile}else{[string]$bundle.files.($entry.Name)}
        if((Get-Digest $entry.FullName) -cne $expected){throw 'Modified helper files. Nothing was overwritten.'}
    }
}
Assert-Bundle $payload
$null=Assert-SafePath $launcher; $null=Assert-SafePath $backup; $null=Assert-SafePath $helper
$current=Get-Digest $launcher; $wrapperHash=Get-Digest $wrapper
if($current -cne $standard -and $current -cne $wrapperHash){throw 'Modified/custom launcher. Startup checks were not installed.'}
if(Test-Path -LiteralPath $backup){if((Get-Digest $backup) -cne $standard){throw 'The original launcher backup differs. Nothing was overwritten.'}}
if(Test-Path -LiteralPath $helper){Assert-Bundle $helper}
if($StateOnly){
    if($current -ceq $wrapperHash){if(!(Test-Path -LiteralPath $backup -PathType Leaf)-or !(Test-Path -LiteralPath $helper -PathType Container)){throw 'Installed helper/backup missing.'};Write-Output 'Enabled'}else{Write-Output 'Disabled'}
    exit 0
}
if($Disable){
    if($current -ceq $standard){Write-Output 'Startup checks are already disabled.';exit 0}
    if(!(Test-Path -LiteralPath $backup -PathType Leaf)){throw 'Original launcher backup is missing.'}
    $bytes=[IO.File]::ReadAllBytes($backup)
}else{
    if($current -ceq $wrapperHash){if(!(Test-Path -LiteralPath $backup -PathType Leaf)-or !(Test-Path -LiteralPath $helper -PathType Container)){throw 'Installed helper/backup missing.'};Write-Output 'Startup checks are already enabled.';exit 0}
    if(!(Test-Path -LiteralPath $helper)){
        $stage=$helper+'.installing-'+[Guid]::NewGuid().ToString('N')
        [IO.Directory]::CreateDirectory($stage)|Out-Null
        foreach($name in $allowed){[IO.File]::Copy((Join-Path $payload $name),(Join-Path $stage $name),$false)}
        Assert-Bundle $stage
        [IO.Directory]::Move($stage,$helper)
    }
    if(!(Test-Path -LiteralPath $backup)) {[IO.File]::Copy($launcher,$backup,$false)}
    if((Get-Digest $backup) -cne $standard){throw 'Original launcher backup failed verification.'}
    $bytes=[IO.File]::ReadAllBytes($wrapper)
}
$temporary=Join-Path $old.Root ('PLAY.startup-pending-'+[Guid]::NewGuid().ToString('N')+'.tmp')
$stream=[IO.File]::Open($temporary,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
try{$stream.Write($bytes,0,$bytes.Length)}finally{$stream.Dispose()}
if((Get-Digest $launcher) -cne $current){throw 'Launcher changed during installation. Nothing was overwritten.'}
[IO.File]::Replace($temporary,$launcher,[System.Management.Automation.Language.NullString]::Value)
Write-Output $(if($Disable){'Startup checks disabled. Exact original launcher restored; helper and backup retained.'}else{'Optional startup checks enabled. Original launcher kept byte-exact.'})
