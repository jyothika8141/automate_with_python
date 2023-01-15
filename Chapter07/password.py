import re
st = 'Jyoth1ka'
if len(st) >= 8:
    cond1 = re.compile(r'\d')
    mo1 = cond1.search(st)
    if mo1 != None:
        cond2 = re.compile(r'[A-Z]')
        mo2 = cond2.search(st)
        if mo2 != None:
            cond3 = re.compile(r'[a-z]')
            mo3 = cond3.search(st)
            if mo3 != None:
                print('Strong')
            else:
                print('Not strong')
        else:
            print('Not strong')
    else:
        print("Not strong")
else:
    print('Not strong')
