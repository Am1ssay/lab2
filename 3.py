import os
import sys


if len(sys.argv) > 1:
    os.mkdir(sys.argv[1])
else:
    print("There is no expected param. Example:\npy example.py directory")
