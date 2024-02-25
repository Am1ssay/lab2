import os

print(
    "3.Alright, now let's make a new directory in '% s' :)\nEnter name of new directory: "
    % os.getcwd(),
    end="")
namedir = str(input())
os.mkdir(namedir)
