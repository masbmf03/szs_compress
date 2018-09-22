# This is a SZS compressor designed by masbmf03 for the Variety Pack Dev Team, powered by Wimm's SZS Tool.

# View the readme.md for more information.

import subprocess
import os
import sys
import glob

print('''
   _____ ______ _____    _____  ____  __  __ _____  _____  ______  _____  _____ 
  / ____|___  // ____|  / ____|/ __ \|  \/  |  __ \|  __ \|  ____|/ ____|/ ____|
 | (___    / /| (___   | |    | |  | | \  / | |__) | |__) | |__  | (___ | (___  
  \___ \  / /  \___ \  | |    | |  | | |\/| |  ___/|  _  /|  __|  \___ \ \___ \ 
  ____) |/ /__ ____) | | |____| |__| | |  | | |    | | \ \| |____ ____) |____) |
 |_____//_____|_____/   \_____|\____/|_|  |_|_|    |_|  \_\______|_____/|_____/ 
                                                                                                                         
''')
directory = None
while directory != '':
    directory = input("Please paste directory: ")
    if directory == '':
        continue
    if not directory.endswith(os.path.sep):
        directory += os.path.sep
    os.chdir(directory)
    lst = glob.glob('*.szs')
    files = [os.path.splitext(x)[0] for x in lst]
   
    while len(files) >= 0:
        os.chdir(directory)
        subprocess.call(["wszst", "x", "{}.szs".format(files[0])], cwd=directory)
        subprocess.call(["wszst", "create", "{}.d".format(files[0]), "-o"], cwd=directory)
        subprocess.call(["rmdir", "/Q", "/S", "{}.d".format(directory+files[0])], cwd=directory, shell=True)
        del files[0]
        if not files:
            print("Process has been completed.")
            break











