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
    # print(answer)
    print('')
    user_input = get_user_input()
    while (user_input != 'exit'):
        count += 1
        if not user_input.isdigit():
            print("That's not a number.")
        elif (int(user_input) == answer):
            if (answer == 42):
                print("The answer to the ultimate question of life,",
                      "the universe and everything is 42.")
            if (count == 1):
                print("Congratulations! you got in your on first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in " + str(count) + " attempts!", end="\n")
            break
        elif (0 > int(user_input) or int(user_input) > 99):
            print("number ranger not accepted.")
        elif (int(user_input) > answer):
            print("Too High!")
        else:
            print("Too Low!")
        user_input = get_user_input()
