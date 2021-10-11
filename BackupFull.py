import shutil
import os
sourcePath=r'C:\Users\AneeshD\Downloads/'
DestinationPath=r'C:\Users\AneeshD\Downloads\Backup/'
listOfFiles=os.listdir(sourcePath)
for file in listOfFiles:
    shutil.copy(sourcePath+file,DestinationPath)  