import os, shutil
from pathlib import Path
folder = os.path.abspath('/home/jyothika/Desktop')
for foldername, subfolders, filenames in os.walk(folder):
    for file in filenames:
        path = os.path.join(foldername, file)
        if file.endswith('.jpg') or file.endswith('.pdf'):
            shutil.copy(path, Path.home() / 'pdf&jpg')
            print("Copied file:", path)
