[Setup]
AppName=FileConverterTool
AppVersion=1.0.0
DefaultDirName={localappdata}\FileConverterTool
PrivilegesRequired=none
DefaultGroupName=FileConverterTool
UninstallDisplayIcon={app}\main.exe
OutputDir=.\Installer
OutputBaseFilename=FileConverterTool_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\Projects\python\tool_convert\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\FileConverterTool"; Filename: "{app}\main.exe"
Name: "{commondesktop}\FileConverterTool"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Tạo biểu tượng ngoài màn hình desktop"; GroupDescription: "Tùy chọn thêm:"

[Run]
Filename: "{app}\main.exe"; Description: "Khởi động ứng dụng sau khi cài"; Flags: nowait postinstall skipifsilent runascurrentuser

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
