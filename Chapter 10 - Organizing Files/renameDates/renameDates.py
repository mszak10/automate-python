# renameDates.py - Renames american date format files to european format
import os
import re
import shutil

textBeforePart = monthPart = dayPart = yearPart = textAfterPart = None
hits = 0

dateRegex = re.compile(r"^(.*?)" "\n"
                       r'(([01])?\d)-' "\n"
                       r"(([0123])?\d)-" "\n"
                       r"((19|20)\d\d)" "\n"
                       r"(.*?)$")

# Loop over the files in the working directory.
for usFilename in os.listdir(os.getcwd()):
    mo = dateRegex.search(usFilename)

    # Skip files without a date
    if mo is None:
        continue

    # Separate filename into parts
    textBeforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    textAfterPart = mo.group(8)

    # Form the European-style filename.
    euFilename = f"{textBeforePart}{dayPart}-{monthPart}-{yearPart}{textAfterPart}"

    # Get the full, absolute file paths.
    absFilePath = os.path.abspath(os.getcwd())
    usFilename = absFilePath + usFilename
    euFilename = absFilePath + euFilename

    # Rename the files.
    print(f"Renaming {usFilename} to {euFilename}.. ")
    shutil.move(usFilename, euFilename)
    hits += 1
print(f"Program terminated after {hits} changes")
