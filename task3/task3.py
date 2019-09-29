from sys import argv
from os import listdir
from os.path import isfile, join, realpath

directory = argv
path = realpath(directory[1])
flist = listdir(path)
cashes = []

def read_to_list(path):
    lst = []
    with open(path) as infile:
        for line in infile:
            lst.append(float(line.rstrip()))
    return lst

for fname in listdir(path):
    for n, e in enumerate(read_to_list(join(path, fname))):
        try:
            cashes[n].append(e)
        except IndexError:
            cashes.append([e])

cashes = list(map(sum, cashes))
print(cashes.index(max(cashes))+1)
