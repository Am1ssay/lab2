print("Enter phrase: ", end="")
phrase = str(input())
if phrase == phrase[::-1]:
    print("This is pallindrom")
else:
    print("This is not pallindrom")
