import os
from os import listdir
import shutil
#baseFilePath = input("Enter Base File Path:")
#tarFilePath = input("Enter Target File Path:")
baseFilePath = r"C:\Users\xxxx\OneDrive - yyyy\Project\Revit\python\Python Script\Copy files and rename\baseFilePath"
tarFilePath = r"C:\Users\xxxx\OneDrive - yyyy\Project\Revit\python\Python Script\Copy files and rename\tarFilePath"
movdir = tarFilePath
basedir = baseFilePath

test0=list()
test1=list()
test2=list()
testold=list()
testnew=list()
counts=0

formulatednewname=list()

for root, dirs, files in os.walk(basedir):
    for filename in files:
        # I use absolute path, case you want to move several dirs.
        old_name = os.path.join(os.path.abspath(root), filename)
        testold.append(old_name)
        
        # Separate base from extension
        base, extension = os.path.splitext(filename)
        
        basesplit=base.split("_")
        suf=int(basesplit[1])
        for i in range(30):
            i=i+1
            suf=suf+1
            i=basesplit[0]+"_"+str(suf).zfill(4)+extension
            #formulatednewname.append(basesplit[0]+"_"+str(suf).zfill(4)+extension)
            new_name = os.path.join(movdir, i)
            testnew.append(new_name)
            shutil.copy(old_name, new_name)
    
#print(testold[0])
#print(formulatednewname)
#print(range(len(testnew)))
#print(count)