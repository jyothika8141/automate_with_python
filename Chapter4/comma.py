spam = ['apples', 'bananas', 'tofu', 'cats']

lenSpam = len(spam)
string = ""

for i in spam:
    if spam.index(i) == lenSpam - 1:
        string += "and " + i
        break
    string += i + ", "

print(string)
