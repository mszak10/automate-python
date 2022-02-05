#! python3
# Chapter 6 - Manipulating Strings
# mclip.py - A multi-clipboard program.
import sys, pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print("Usage: python mclip.py [phrase] --> copies phrase text")
    sys.exit()

phrase = sys.argv[1]

if phrase in TEXT:
    pyperclip.copy(TEXT[phrase])
    print("Copied: " + phrase)
else:
    print("Failed to copy: " + phrase)