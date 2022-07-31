
import sys

args = sys.argv[1:]

list = [i[::-1] for i in args]

# print(list)

for i in range(len(args) - 1, -1, -1):
    for j in range(len(args[i]) - 1, -1, -1):
        if (args[i][j].isupper()):
            print(args[i][j].lower(), end='', sep='')
        else:
            print(args[i][j].upper(), end='', sep='')
    if (i != 0):
        print(end=' ', sep='')
