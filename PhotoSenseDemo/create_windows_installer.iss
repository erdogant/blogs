[Setup]
AppName=PhotoSenseDemo
AppVersion=1.0
AppPublisher=PhotoSenseDemo
AppPublisherURL=https://erdogant.medium.com
AppCopyright="© 2025 PhotoSenseDemo"
DefaultDirName={autopf}\PhotoSenseDemo
DefaultGroupName=PhotoSenseDemo
OutputBaseFilename=PhotoSenseDemo_installer
Compression=lzma2
SolidCompression=yes
OutputDir=D:\REPOS\blogs\PhotoSenseDemo\build

[Files]
; Include all files and subdirectories from the build directory
Source: "D:\REPOS\blogs\PhotoSenseDemo\build\exe.win-amd64-3.12\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Create a shortcut to the main executable
Name: "{group}\PhotoSenseDemo"; Filename: "{app}\PhotoSenseDemo.exe"
Name: "{commondesktop}\\PhotoSenseDemo"; Filename: "{app}\\PhotoSenseDemo.exe"; Tasks: desktopicon
Name: "{commondesktop}\\PhotoSenseDemo"; Filename: "{app}\\PhotoSenseDemo.exe"; IconFilename: "{app}\\icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked
