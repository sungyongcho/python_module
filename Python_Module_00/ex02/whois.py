import sys

args = sys.argv

# for not printing traceback
sys.tracebacklimit = 0

if (len(args) > 2):
    raise AssertionError("more than one argument are provided")
elif (len(args) is 1):
    print("")
elif (args[1].isnumeric() is False):
    raise AssertionError("argument is not an integer")
elif (int(args[1]) == 0):
    print("I'm Zero.")
elif (int(args[1]) % 2) == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
