import os
import shutil

source=input("Source Folder:")
destination=input("Copy to:")
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)