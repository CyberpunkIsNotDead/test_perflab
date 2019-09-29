from sys import argv
# try-except takes a lot of time to write so not using them

path = argv
quadrangle = []
dots = []

def read_to_list(infile, l):
    for line in infile:
        e = [float(n) for n in line.rstrip().split()]
        l.append(e) 

with open(path[1]) as infile:
    read_to_list(infile, quadrangle)

with open(path[2]) as infile:
    read_to_list(infile, dots)

def find_dot_location(dot, quadrangle):
    if quadrangle[0][0] < dot[0] < quadrangle[3][0] \
        and quadrangle[0][1] < dot[1] < quadrangle[1][1]:
        print(2)
    elif not quadrangle[0][0] <= dot[0] <= quadrangle[3][0] \
        or not quadrangle[0][1] <= dot[1] <= quadrangle[1][1]:
        print(3)
    elif dot in quadrangle:
        print(0)
    else:
        print(1)

for dot in dots:
    find_dot_location(dot, quadrangle)
