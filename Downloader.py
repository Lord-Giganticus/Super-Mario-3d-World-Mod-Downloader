import os
import sys
import shutil

try:
    os.system('curl --version > curl_test.txt')
    os.remove('curl_test.txt')
except:
    print("curl is not installed!")
    exit()

if len(sys.argv) < 3: # sys.argv MUST be 3 args even if they aren't right.              # Somehow CodeQL isn't complaining about this URL.
    print("There must be three arguments! Example: C:\Users\Lord-G\Documents\Python\SM3DWMD https://gamebanana.com/dl/513081 I:\sdcaffine\TitleID\modpack1")
    exit()
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
dl_location = os.path.dirname(__file__) # Defined here so it isn't Unbound possibly.
link = str('https://gamebanana.com/dl/513081') # Defined here so it isn't Unbound possibly. # Somehow CodeQL isn't complaining about this URL.
script_dir = os.path.dirname(__file__)
os.mkdir(script_dir+'\content')
save_location = script_dir+'\content' # Defined here so it isn't Unbound possibly. # May cause a problem with line 44-45.
# Checking the args:
if os.path.isdir(arg1) == True:
    dl_location = arg1
else:
    print("First argument is not a valid directory. Defaulting to the scripts location.")
if arg2.startswith('https') == True: #CodeQL has been making a complaint about this line not having a sanitized URL. So it'll just check for https for now.
    link = arg2
else:
    print("Second argument is not a gamebanana link. Defaulting to https://gamebanana.com/dl/513081")
if os.path.isdir(arg3) == True:
    save_location = arg3
else:
    print("Third agument is not a valid directory. Defaulting to a folder we made in the scripts location.") # Again, this might cause problems with line 44-45.
# Defining the downloader:
def downloader(dl_folder,link,save_folder): # For a unknown reason, adding :str to the parameters was causing a crash.
    os.chdir(dl_folder)
    os.system('curl -L '+link+' > DL.zip')
    os.system('curl http://stahlworks.com/dev/unzip.exe --output unzip.exe') # Will attempt to remove usage of this so the script can be used on non Windows systems.
    os.system('cmd /c unzip *zip') # Will attempt to remove usage of this so the script can be used on non Windows systems.
    os.remove('DL.zip') # Will attempt to remove usage of this so the script can be used on non Windows systems.
    potental_mods = []
    if os.path.isdir('content') == True: # Just in case the zip does this. I don't expect many people to have their zips like this.
            potental_mods.append('content')
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir+'\content') == True: # dir+'\content' is used so it's set to the right directory.
            potental_mods.append(dir+'\content')
    print("Dectected",len(potental_mods),"content subfolders.")
    mod_choice = int(input("Enter the number entry for which content folder is the correct one. (starts at 0)")) # Oh boy do I hope no one makes a Issue because of this being a int, not a str.
    mod = potental_mods[mod_choice]
    os.chdir(mod)
    mod = os.getcwd()
    os.chdir('../')
    shutil.move(mod,save_folder) # Might throw an exception if save_location and dl_location are both set to os.path.dirname(__file__). Thus is why save_location is set to os.path.dirname(__file__)+'\content'.
    print("Complete.")
    return exit()
# Converting variables to strings just in case because I can't add :str to line 37 for some reason.
dl_location = str(dl_location)
link =  str(link)
save_location = str(save_location)

downloader(dl_location,link,save_location) # Runs downloader.