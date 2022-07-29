
import sys

args = sys.argv[1:]

list = [i[::-1] for i in args]

list
print(list.reverse())

for i in range(len(args)):
    print("",end='', sep='')

