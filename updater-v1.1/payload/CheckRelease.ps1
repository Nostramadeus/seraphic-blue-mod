param([ValidateRange(1,3)][int]$TimeoutSeconds=3)
$ErrorActionPreference='Stop'
try {
    . "$PSScriptRoot/Update.ps1" -Library
    $release=Get-LatestRelease -TimeoutSeconds $TimeoutSeconds
    [Console]::Out.Write(($release | ConvertTo-Json -Depth 20 -Compress))
    exit 0
} catch { exit 1 }
