# Windows GUI updater

1. Close the game and extract the [updater ZIP](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-updater-windows-v1.0.0.zip).
2. Open **SeraphicBlue-Update.exe**.
3. Click **Choose...**, select the old game folder containing **PLAY.cmd**, then click **Update to latest**.
4. After verification, click **Play updated copy**.

Keep **Update.ps1** beside the program. No Python installation is needed. The updater uses Windows PowerShell supplied with Windows10/11. It creates a new same-edition game folder beside the old one, keeps a verified save/settings backup, preserves the new EasyRPG.ini and checks the release checksum plus extracted file hashes. If already current, it does not reinstall.

Supported: intact stable full-game manifests and standard save/config paths. Patch-only installs, modified databases, custom save paths, Linux and Steam Deck use the [manual steps](../INSTALL.md#update-and-keep-saves). No edition conversion or downgrade. Interrupted updates stop before final installation; keep the old folder and backup. No automatic cleanup.

Source: Update.ps1 contains the updater. Launcher.cs is the console-free Windows launcher. Build the launcher with the Windows .NET Framework C# compiler, target winexe, references System.Windows.Forms.dll, debug disabled. The downloadable ZIP includes the same source. New updater code is covered by LICENSE-MIT.txt.
