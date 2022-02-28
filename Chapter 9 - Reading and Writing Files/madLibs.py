# madLibs.py - Read text file and enter user input at KEYWORD
# Outputs sentance with capital keywords replaced by user-chosen words
# and writes it to a file called output.txt

import pyinputplus as pyip

nouncount = i = 0

adj = pyip.inputStr(prompt="What is your adjective?")
noun = pyip.inputStr(prompt="What is your noun?")
verb = pyip.inputStr(prompt="What is your verb?")
noun2 = pyip.inputStr(prompt="What is your second noun?")


with open('madlib1.txt', 'r') as fileObject:
    fileContent = fileObject.read()
    fileContent = fileContent.split(' ')
    print(fileContent)
    print(len(fileContent))

    for word in fileContent:
        if word.isupper():
            dotBool = False
            if word.endswith('.'):
                dotBool = True
            if word.startswith('ADJECTIVE'):
                fileContent[i] = fileContent[i].replace(word, adj)
                if dotBool:
                    fileContent[i] += '.'
            elif word.startswith('NOUN'):
                if nouncount == 0:
                    fileContent[i] = fileContent[i].replace(word, noun)
                    nouncount += 1
                else:
                    fileContent[i] = fileContent[i].replace(word, noun2)
                if dotBool:
                    fileContent[i] += '.'
            elif word.startswith('VERB'):
                fileContent[i] = fileContent[i].replace(word, verb)
                if dotBool:
                    fileContent[i] += '.'
        i += 1
    fileContent = ' '.join(fileContent)
    print(fileContent)
    with open('output.txt', 'w') as f:
        f.write(fileContent)
