import os

print("Now in this directory '% s' there are files" % os.getcwd())
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
