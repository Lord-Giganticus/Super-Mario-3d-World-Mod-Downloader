import win32api
import os
import shutil

drives = win32api.GetLogicalDriveStrings()

os.mkdir("C:\Lord-G")
os.chdir("C:\Lord-G")
input("Due to the mod's size, you'll have to dl the latest (and I mean it, the old ones don't work with this.) zip and save it C:\Lord-G\ as SM3DWR.zip.")
os.system('cmd /c start https://gamebanana.com/gamefiles/download/12437')
input("Once that's done press enter to continue,")
os.system('cmd /c curl http://stahlworks.com/dev/unzip.exe -o unzip.exe')
os.system('cmd /c unzip *zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.exe')

choice = input("There are 2 ways for the mod to be installed. Enter the number corresponding to your choice.\n[1]SDCafiine\n[2]CEMU\n")
if choice == "1":
    USA = "0005000010145c00"
    EUR = "0005000010145d00"
    JPN = "0005000010106100"
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
    region = input("Enter a number corresponding to the region you live in.\n[1]USA\n[2]EUR\[3]JPN\n")
    if region == "1":
        os.chdir(drive_choice)
        os.chdir('sdcafiine')
        os.mkdir(USA)
        os.chdir(USA)
        os.mkdir("SM3DWR")
        os.chdir("SM3DWR")
        sdcafiine_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", sdcafiine_folder)
        input("Complete. Press enter to exit.")
        exit()
    elif region == "2":
        os.chdir(drive_choice)
        os.chdir('sdcafiine')
        os.mkdir(EUR)
        os.chdir(EUR)
        os.mkdir("SM3DWR")
        os.chdir("SM3DWR")
        sdcafiine_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", sdcafiine_folder)
        input("Complete. Press enter to exit.")
        exit()
    elif region == "3":
        os.chdir(drive_choice)
        os.chdir('sdcafiine')
        os.mkdir(JPN)
        os.chdir(JPN)
        os.mkdir("SM3DWR")
        os.chdir("SM3DWR")
        sdcafiine_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", sdcafiine_folder)
        input("Complete. Press enter to exit.")
        exit()
    else:
        input("Well, you chose wrong! You'll have to rerun the program so press enter to exit.")
        exit()
elif choice == "2":
    USA = "10145c00"
    EUR = "10145d00"
    JPN = "10106100"

    mlc01_location = input("Enter the path to your cemu's mlc01 folder:\n")
    os.chdir(mlc01_location)
    os.chdir("usr")
    os.chdir("title")
    os.chdir("00050000")
    region = input("Enter a number corresponding to the region you live in.\n[1]USA\n[2]EUR\[3]JPN\n")
    if region == "1":
        if os.path.isdir(USA) == False:
            os.mkdir(USA)
        os.chdir(USA)
        os.chdir("content")
        content_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", content_folder)
        input("Complete. Press enter to exit.")
        exit()
    elif region == "2":
        if os.path.isdir(EUR) == False:
            os.mkdir(EUR)
        os.chdir(EUR)
        os.chdir("content")
        content_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", content_folder)
        input("Complete. Press enter to exit.")
        exit()
    elif region == "3":
        if os.path.isdir(JPN) == False:
            os.mkdir(JPN)
        os.chdir(JPN)
        os.chdir("content")
        content_folder = os.getcwd()
        shutil.copytree("C:\Lord-G\SM3DWR", content_folder)
        input("Complete. Press enter to exit.")
        exit()
    else:
        input("Well, you chose wrong! You'll have to rerun the program so press enter to exit.")
        exit()
else:
    input("Well, you chose wrong! You'll have to rerun the program so press enter to exit.")
    exit()