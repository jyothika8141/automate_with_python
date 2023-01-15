import os
folder = os.path.abspath('/home/jyothika/Downloads')
for foldername, subfolders, filenames in os.walk(folder):
    for file in filenames:
        path = os.path.join(foldername, file)
        size = os.path.getsize(path)
        if size > 100000000:
            print(path) 