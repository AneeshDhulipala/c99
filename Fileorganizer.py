import shutil
import os
sourcePath=r'C:\Users\AneeshD\Downloads'
listOfFiles=os.listdir(sourcePath)
for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext = ext[1:]
    if ext=='':
        continue

    if os.path.exists(sourcePath+'/'+ext):
        shutil.move(sourcePath+'/'+file,sourcePath+'/'+ext+'/'+file)
    else:
        os.makedirs(sourcePath+'/'+ext)
        shutil.move(sourcePath+'/'+file,sourcePath+'/'+ext+'/'+file)