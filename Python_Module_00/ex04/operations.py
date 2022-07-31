import sys

# for string.punctuation
import string

# for not printing traceback
sys.tracebacklimit = 0


def operations(a, b):
    print("Sum:\t\t", a+b)
    print("Difference:\t", a-b)
    print("Product:\t", a*b)
    try:
        if(str(a/b)[::-1].find('.') > 3):
            print("Quotient:\t", str(round(a/b, 3)) + '...')
        else:
            print("Quotient:\t", a/b)
    except ZeroDivisionError:
        print("Quotient:\t ERROR (division by zero)")
    try:
        print("Remainder:\t", a % b)
    except ZeroDivisionError:
        print("Remainder:\t ERROR (modulo by zero)")


if __name__ == "__main__":
    if (len(sys.argv) > 3):
        raise AssertionError("too many arguments")
    elif (len(sys.argv) == 1):
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
    elif (sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False):
        raise AssertionError("only integers")
    else:
        operations(int(sys.argv[1]), int(sys.argv[2]))
