# Part 1

import sys

# for string.punctuation
import string

# for not printing traceback
sys.tracebacklimit = 0

morse_list = []


def alphanumeric_to_morse_list(char):
    if (char.upper() == 'A'):
        morse_list.append(".-")
    elif (char.upper() == 'B'):
        morse_list.append("-...")
    elif (char.upper() == 'C'):
        morse_list.append("-.-.")
    elif (char.upper() == 'D'):
        morse_list.append("-..")
    elif (char.upper() == 'E'):
        morse_list.append(".")
    elif (char.upper() == 'F'):
        morse_list.append("..-.")
    elif (char.upper() == 'G'):
        morse_list.append("--.")
    elif (char.upper() == 'H'):
        morse_list.append("....")
    elif (char.upper() == 'I'):
        morse_list.append("..")
    elif (char.upper() == 'J'):
        morse_list.append(".---")
    elif (char.upper() == 'K'):
        morse_list.append("-.-")
    elif (char.upper() == 'L'):
        morse_list.append(".-..")
    elif (char.upper() == 'M'):
        morse_list.append("--")
    elif (char.upper() == 'N'):
        morse_list.append("-.")
    elif (char.upper() == 'O'):
        morse_list.append("---")
    elif (char.upper() == 'P'):
        morse_list.append(".--.")
    elif (char.upper() == 'Q'):
        morse_list.append("--.-")
    elif (char.upper() == 'R'):
        morse_list.append(".-.")
    elif (char.upper() == 'S'):
        morse_list.append("...")
    elif (char.upper() == 'T'):
        morse_list.append("-")
    elif (char.upper() == 'U'):
        morse_list.append("..-")
    elif (char.upper() == 'V'):
        morse_list.append("...-")
    elif (char.upper() == 'W'):
        morse_list.append(".--")
    elif (char.upper() == 'X'):
        morse_list.append("-..-")
    elif (char.upper() == 'Y'):
        morse_list.append("-.--")
    elif (char.upper() == 'Z'):
        morse_list.append("--..")
    elif (char.upper() == 'O'):
        morse_list.append("-----")
    elif (char.upper() == '1'):
        morse_list.append(".----")
    elif (char.upper() == '2'):
        morse_list.append("..---")
    elif (char.upper() == '3'):
        morse_list.append("...--")
    elif (char.upper() == '4'):
        morse_list.append("....-")
    elif (char.upper() == '5'):
        morse_list.append(".....")
    elif (char.upper() == '6'):
        morse_list.append("-....")
    elif (char.upper() == '7'):
        morse_list.append("--...")
    elif (char.upper() == '8'):
        morse_list.append("---..")
    elif (char.upper() == '9'):
        morse_list.append("----.")


def sos(list):
    for i in range(len(list)):
        for j in range(0, len(list[i])):
            if (list[i][j] == ' '):
                morse_list.append('/')
            elif not (list[i][j].isalpha() or list[i][j].isnumeric()):
                print("ERROR")
                return
            else:
                alphanumeric_to_morse_list(list[i][j])
    print(*morse_list)


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print(end="")
    else:
        input_list = []
        if len(sys.argv) > 2:
            for i in range(1, len(sys.argv)):
                input_list.append(sys.argv[i])
                if (i != len(sys.argv) - 1):
                    input_list.append(' ')
        else:
            input_list = list(sys.argv[1].split(" "))
        sos(input_list)
