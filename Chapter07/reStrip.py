import re

def strip(text, *sub):
    lstrip = re.compile(r'^\s')
    rstrip = re.compile(r'\s$')
    word = re.compile(re.compile(*sub))

    while lstrip.search(text) != None:
        text = text[1:]

    while rstrip.search(text) != None:
        text = text[:-1]

    while word.search(text) != None:
        index = word.search(text).span()
        text = text[:index[0]] + text[index[1]:]

    return text


strippedText = strip("     kkkhohohoollhohohll      ", 'ho')
print(strippedText)
