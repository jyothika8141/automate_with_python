import re
date = '29/02/2005'
dateregx1 = re.compile(r'[1-2][0-9]/[0][1-9]/[1-2][0-9][0-9][0-9]')
dateregx2 = re.compile(r'[0][1-9]/[0][1-9]/[1-2][0-9][0-9][0-9]')
dateregx3 = re.compile(r'[3][0-1]/[0][1-9]/[1-2][0-9][0-9][0-9]')
dateregx4 = re.compile(r'[1-2][0-9]/[1][0-2]/[1-2][0-9][0-9][0-9]')
dateregx5 = re.compile(r'[0][1-9]/[1][0-2]/[1-2][0-9][0-9][0-9]')
dateregx6 = re.compile(r'[3][0-1]/[1][0-2]/[1-2][0-9][0-9][0-9]')

mo = dateregx1.search(date) or dateregx2.search(date) or dateregx3.search(date) or dateregx4.search(date) or dateregx5.search(date) or dateregx6.search(date)

if mo != None:
    date_str = mo.group()
    day = date_str[:2]
    month = date_str[3:5]
    year = date_str[6:]
    if month in ['04', '06', '09', '11']:
        if int(date) <= 30:
            print('Valid')
        else:
            print("Invalid Date")
    elif month == '02':
        leap = True if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0 else False
        if leap == True:
            if int(day) <= 29:
                print('Valid')
            else:
                print('Invalid')
        else:
            if int(day) <= 28:
                print('Valid')
            else:
                print('Invalid')
else:
    print("Invalid Date")
