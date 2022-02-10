# Chapter 7 - Regular Expressions
# strongPassDetect.py - detects whether password in clipboard is strong
import re
import pyperclip

clipboard = pyperclip.paste()

if len(clipboard) > 7:
    length = True
else:
    length = False

# Regex for lowercase
lowercase_regex = re.compile(r'[a-z]')
x = lowercase_regex.findall(clipboard)
if len(x) > 0:
    lowercase = True
else:
    lowercase = False

# Regex for uppercase
uppercase_regex = re.compile(r'[A-Z]')
x = uppercase_regex.findall(clipboard)
if len(x) > 0:
    uppercase = True
else:
    uppercase = False

# Regex for numbers
number_regex = re.compile(r'[0-9]')
x = number_regex.findall(clipboard)
if len(x) > 0:
    number = True
else:
    number = False

if length and lowercase and uppercase and number:
    total = "strong"
else:
    total = "weak"

print(f'''Password being tested: {clipboard}
Following is whether password matches requirements:
length: {length}
lowercase: {lowercase} 
uppercase: {uppercase} 
number: {number}
Therefore your password is {total}''')
