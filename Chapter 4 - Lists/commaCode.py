# commaCode script
# Chapter 4 - Lists
def func(arg):
    text = ""
    for i in range(len(arg)):
        text = text + arg[i] + ". "
        if i == len(arg) - 2:
            text += "and "
    return text


spam = ['apples', 'bananas', 'tofu', 'cats']
print(func(spam))
