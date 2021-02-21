msbuild SM3DW-Keys\SM3DW-Keys.csproj -p:Configuration=Release
msbuild Super-Mario-3d-World-Mod-Downloader.sln -p:Configuration=Release
copy Super-Mario-3d-World-Mod-Downloader\bin\Release\Super-Mario-3d-World-Mod-Downloader.exe %CD%
copy Super-Mario-3d-World-Mod-Downloader\bin\Release\SM3DW-Keys.dll %CD%