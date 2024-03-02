import sys

if len(sys.argv) > 1:
    print(f"Привет, {sys.argv[1]}!")
else:
    print("There is no expected param. Example:\npy example.py Mark")
