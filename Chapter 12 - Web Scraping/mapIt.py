# mapIt.py - Launches a map in the browser using an address
# from user input or clipboard.

import pyperclip
import webbrowser

# Get address from user input
address = input("What's the address?")
if address == '':
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
