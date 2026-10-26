$ErrorActionPreference='Stop'
$compiler=Join-Path $env:SystemRoot 'Microsoft.NET/Framework64/v4.0.30319/csc.exe'
if(!(Test-Path -LiteralPath $compiler)){throw 'Existing .NET Framework compiler not found. No dependencies were installed.'}
& $compiler /nologo /target:winexe /optimize+ /platform:anycpu /r:System.Windows.Forms.dll ('/out:'+(Join-Path $PSScriptRoot 'SeraphicBlue-Startup-Settings.exe')) (Join-Path $PSScriptRoot 'Launcher.cs')
if($LASTEXITCODE-ne 0){throw 'GUI bootstrap compilation failed.'}
