import os, shutil
from pathlib import Path

end1 = 1
prefix = input("Enter prefix of filename: ")
len_prefix = len(prefix)
folder = os.path.abspath('/home/jyothika/amfoss/absp/Chapter10/spam/')
for foldername, subfolders, filenames in os.walk(folder):
    for file in filenames:
        end = int(file[len_prefix:-4])
        if file.startswith(prefix):
            if end1 != end:
                if 1 < end1 < 9:
                    new_name = prefix+ '00'+ str(end1)+ '.txt'
                elif 9 < end1 < 99:
                    print("hi")
                    new_name = prefix+ '0'+ str(end1)+ '.txt'
                else:
                    new_name = prefix+ str(end1)+ '.txt'
                os.rename(folder+'/'+ file, 'spam/' + new_name)
            end1 += 1