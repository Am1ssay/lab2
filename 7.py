def cntlet(phrase):
    sogl = 0
    glas = 0
    a = {'a', 'e', 'y', 'u', 'o', 'i'}
    for i in range(0, len(phrase)):
        if phrase[i] in a:
            glas += 1
        else:
            sogl += 1
    return sogl, glas


print("Enter phrase: ", end="")
phrase = str(input())
print("Sogl/Glas ", cntlet(phrase))
