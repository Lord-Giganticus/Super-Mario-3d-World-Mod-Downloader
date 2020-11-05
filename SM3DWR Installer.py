import win32api
import os
import shutil

drives = win32api.GetLogicalDriveStrings()
USA = "0005000010145c00"
EUR = "0005000010145d00"
JPN = "0005000010106100"

os.mkdir("C:\Lord-G\SM3DWR")
os.chdir("C:\Lord-G\SM3DWR")
os.system('cmd /c curl https://lord-giganticus.github.io/Super-Mario-3d-World-Repainted-Downloader/docs/SM3DWR.zip -o SM3DWR.zip')
os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
os.system('cmd /c unzip *zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.exe')

choice = input("There are 2 ways for the mod to be installed. Enter the number corresponding to your choice.\n[1]SDCafiine\n[2]CEMU\n")
if choice == "1":
    print(drives)
    drive_choice = input("Enter the drive that is your SD/USB from above.\n")
    os.chdir(drive_choice)
    if os.path.isdir('sdcafiine') == False:
        cont = input("The sdcaffine folder dosen't exist! If this is not the correct drive enter 1.(Press enter to continue as normal.)\n")
        if cont == "1":
            exit()
        os.mkdir('sdcafiine')
    if os.path.isdir('wiiu') == False:
        cont = input("The wiiu folder dosen't exist! If this is not the correct drive enter 1.(Press enter to continue as normal.)\n")
        if cont == "1":
            exit()
        os.mkdir('wiiu')
        os.chdir('wiiu')
    if os.path.isdir('apps') and os.path.isdir('apps\SDcafiine') == False:
        os.chdir(drive_choice)
        os.system('cmd /c curl https://www.wiiubru.com/appstore/zips/SDcafiine.zip -o sdcafiine.zip')
        os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
        os.system('cmd /c unzip *zip')
        os.system('cmd /c del /f *.zip')
        os.system('cmd /c del /f *.exe')
        os.system('cmd /c del /f *.install')
        os.system('cmd /c del /f *.json')
    