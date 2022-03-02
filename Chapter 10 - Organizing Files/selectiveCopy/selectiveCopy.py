# selectiveCopy.py - Copes all files of user-chosen extensions and copies them to "C:\Destination\"

import os
import re
import shutil

import pyinputplus as pyip

filetype = pyip.inputStr(prompt="What filetype? (ex: txt pdf cfg) ")

regex = re.compile(r"^(.*?)\." + filetype)

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('Folder: ' + folderName)
    for filename in filenames:
        mo = regex.search(filename)
        if mo is None:
            continue
        shutil.copy(folderName + '\\' + filename, "C:\\Destination\\")
