import sys

for i in range(len(sys.argv), 1, -1):
    for j in range(len(sys.argv[i - 1]), 0, -1):
        print(sys.argv[i - 1][j - 1], end='', sep='')