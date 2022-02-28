# regexSearch.py - opens all .txt files in a folder and searches all lines for user-provided regex

import os
import re
import pyinputplus as pyip

userThingy = pyip.inputStr(prompt="What are you looking for? ")
regexObj = re.compile(str(userThingy))
found = None

for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        lines = []
        fContent = f.read()
        fContent = fContent.split("\n")
        i = 1
        for line in fContent:
            # if userThingy in line:
            #     print(f"Found \"{userThingy}\" in {filename} at {i} line")
            if regexObj.search(line):
                print(f"Found \"{userThingy}\" in {filename} at {i} line")
            i += 1
