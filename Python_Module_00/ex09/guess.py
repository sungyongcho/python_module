import sys

# for random number
import random

# for not printing traceback
sys.tracebacklimit = 0


answer = random.randint(1, 99)


def welcome_message():
    print("This is an interactive guessing game!")
    print("You have to enter a number between",
          "1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")


def get_user_input():
    user_input = input("What's your guess between 1 and 99?\n>> ")
    return user_input


if __name__ == "__main__":
    welcome_message()
    count = 0
    # print("answer:", answer)
    print('')
    while (True):
        user_input = get_user_input()
        if user_input == 'exit':
            break
        try:
            float(user_input)
        except ValueError:
            print("That's not a number.")
            continue
        count += 1
        try:
            user_input = int(user_input)
        except ValueError:
            print("number range not accepted (integer only)")
            continue
        if user_input == answer:
            if (answer == 42):
                print("The answer to the ultimate question of life,",
                      "the universe and everything is 42.")
            if (count == 1):
                print("Congratulations! you got in your on first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in " + str(count) + " attempts!", end="\n")
            break
        elif (1 > user_input or user_input > 99):
            print("number ranger not accepted.")
        elif (user_input > answer):
            print("Too High!")
        else:
            print("Too Low!")
    print("Goodbye!")
