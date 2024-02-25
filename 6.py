def startlet(words, let):
    a = list()
    for s in words:
        if s[0] == let:
            a.append(s)
    return a


print("Enter some words: ", end="")
words = input().split()
print("Enter start letter: ", end="")
let = str(input())
print("This words start with '% s': " % let, startlet(words, let[0]))
