import os
import shutil

source = input("Enter Source Folder")
destinstion = input("Enter Destination Folder")
source = source + '/'
destinstion = destinstion + '/'
listdirectory = os.listdir(source)
for file in listdirectory:
    shutil.copy((source + file),(destinstion + file))