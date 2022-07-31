# Part 1

import sys

# for string.punctuation
import string

# for not printing traceback
sys.tracebacklimit = 0


def text_count(inputString):
    count_upper = 0
    count_lower = 0
    count_punctuation = 0
    count_spaces = 0
    for i in range(0, len(inputString)):
        if (inputString[i].isupper()):
            count_upper += 1
        if (inputString[i].islower()):
            count_lower += 1
        if (inputString[i].isspace()):
            count_spaces += 1
        if inputString[i] in string.punctuation:
            count_punctuation += 1
    print("The text contains", str(len(inputString)), "character(s):")
    print("-", str(count_upper), "upper letter(s)")
    print("-", str(count_lower), "lower letter(s)")
    print("-", str(count_punctuation), "punctuation mark(s)")
    print("-", str(count_spaces), "space(s)")


def text_analyzer(inputString=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if(inputString is None or inputString == ""):
        print("What is the text to analyze?")
        inputString = input(">> ")
        text_count(inputString)
    elif(isinstance(inputString, str) is False):
        raise AssertionError("argument is not a string")
    else:
        text_count(inputString)


# Part 2
if __name__ == "__main__":
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument are provided")
    elif (len(sys.argv) == 1):
        text_analyzer("")
    else:
        text_analyzer(sys.argv[1])
