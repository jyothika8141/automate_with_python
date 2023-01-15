def convert_str(lst):
    st = ''
    for i in lst:
        st += i
        if lst.index(i) == len(lst) - 2:
            st += ', and '
            continue
        elif lst.index(i) == len(lst) - 1:
            continue
        st += ', '
    return st

spam = ['apples', 'bananas', 'tofu', 'cats']
string = convert_str(spam)
print(string)
