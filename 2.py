import sys

if len(sys.argv) > 1:
    input = " ".join(sys.argv[1:])
    print(input[::-1])
else:
    print(
        "There is no expected param. Example:\npy example.py This is example sentence"
    )
