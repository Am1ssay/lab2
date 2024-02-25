import os
import os.path
from os import listdir
from os.path import isfile, join


def revstr(string):
    return string[::-1]


def uniq_numbs(nums):
    a = list()
    for i in range(0, len(nums)):
        if numbers.count(nums[i]) == 1:
            a.append(nums[i])
    return a


def startlet(words, let):
    a = list()
    for s in words:
        if s[0] == let:
            a.append(s)
    return a


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


def pown(nums):
    a = list()
    for i in range(0, len(nums)):
        a.append(int(nums[i])**2)
    return a


print("1.Enter your name: ", end="")
name = str(input())
print("Hello, ", name, "!", sep="")
print("2.Now enter some string that will be reversed: ", end="")
string = str(input())
print(revstr(string))
print(
    "3.Alright, now let's make a new directory in '% s' :)\nEnter name of new directory: "
    % os.getcwd(),
    end="")
namedir = str(input())
os.mkdir(namedir)
print("4.Now in this directory '% s' there are files" % os.getcwd())
mypath = str(os.getcwd())
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename), " size -",
              os.stat(filename).st_size, "bytes"
              " creation time -",
              os.stat(filename).st_ctime)
print("5.Now enter some numbers: ", end="")
numbers = input().split()
print("There are uniq numbers: ", uniq_numbs(numbers))
print("9.This are quadz: ", pown(numbers))
print("6.Now enter some words: ", end="")
words = input().split()
print("Enter start letter: ", end="")
let = str(input())
print("This words start with '% s': " % let, startlet(words, let[0]))
print("7.Enter phrase: ", end="")
phrase = str(input())
print("Sogl/Glas ", cntlet(phrase))
if phrase == phrase[::-1]:
    print("It's pallindrom")
else:
    print("It's not pallindrom")
