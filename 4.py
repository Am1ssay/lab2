import os
import sys
import time
from os import listdir
from os.path import isfile, join

if len(sys.argv) > 1:
    path = sys.argv[1]
    print("Now in this directory '% s' there are files" % path)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for filename in onlyfiles:
        if '.' in filename:
            print(
                f"Файл:{filename} size - {os.stat(filename).st_size} bytes creation time - {time.ctime(os.stat(filename).st_ctime)}"
            )
else:
    print("There is no expected param. Example:\npy example.py C:\directory")
