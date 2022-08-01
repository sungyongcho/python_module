# Part 1

import sys

# for string.punctuation
import string

# for not printing traceback
# sys.tracebacklimit = 0


def filterwords(input_string, num):
    new_string = input_string.translate(str.maketrans('',
                                                      '',
                                                      string.punctuation))
    input_list = list(new_string.split(" "))
    new_list = []
    for i in range(len(input_list)):
        if len(input_list[i]) > int(num):
            new_list.append(input_list[i])
    print(new_list, num)


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("ERROR")
    else:
        if not sys.argv[2].isdigit():
            print("ERROR")
        else:
            filterwords(sys.argv[1], sys.argv[2])
