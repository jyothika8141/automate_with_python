import re
from pathlib import Path

userinput = input("Enter expression to check: ")
userregex = re.compile(userinput)
p = Path('/home/jyothika/Desktop')
files = p.glob('*.txt')
for file in files:
    with open(file) as f:
        data = f.read()
        search = userregex.search(data)
        if search == None:
            continue
        print(file)
        print(data)
