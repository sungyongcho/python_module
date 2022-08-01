import sys

# for not printing traceback
sys.tracebacklimit = 0

cookbook = {
    'Sandwich': {'ingredients': ['ham', 'bread', 'cheese'],
                 'meal': 'lunch',
                 'prep_time': 60},
    'Cake':     {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                 'meal': 'lunch',
                 'prep_time': 15},
    'Salad':    {'ingredients': ['flour', 'sugar', 'egg'],
                 'meal': 'dessert',
                 'prep_time': 10}
}


def print_all_recipe_names():
    for key, value in cookbook.items():
        print(key)


def print_recipe_details(key):
    print("Recipe for", key.lower(), end=":\n")
    print("  Ingredients list:", cookbook[key]['ingredients'])
    print("  To be eaten for", cookbook[key]['meal'], end='.\n')
    print("  Takes", cookbook[key]['prep_time'],
          "minutes of cooking", end='.\n\n')


def print_the_cookbook():
    for key, value in cookbook.items():
        print_recipe_details(key)


def delete_a_recipe(key):
    del cookbook[key]


def add_a_recipe():
    name = input("Enter a name:\n")
    while name.lower() in {k.lower(): v for k, v in cookbook.items()}:
        name = input("A recipe already exists, please add another recipe: \n")

    ingredients = []
    tmp = input("Enter ingredients:\n")
    while tmp != "":
        ingredients.append(tmp)
        tmp = input()

    type = input("Enter a meal type:\n")
    while (type != 'breakfast' and
           type != 'lunch' and
           type != 'dinner' and
           type != 'dessert'):
        type = input("Wrong value, please enter from " +
                     "breakfast, lunch, dinner or dessert: \n")

    time = input("Enter a preparation time:\n")
    while not (time.isdigit() and int(time) > 0):
        time = input("Wrong value, please enter appropriate minutes: \n")

    cookbook.update(
        {name.title(): {'ingredients': ingredients,
                        'meal': type,
                        'prep_time': int(time)}})


def list_options():
    print("List of available option:\n" +
          "  1: Add a recipe\n" +
          "  2: Delete a recipe\n" +
          "  3: Print a recipe\n" +
          "  4: Print the cookbook\n" +
          "  5: Quit\n")


def menu_choose():
    user_input = input("Please select an option:\n>> ")
    print('')
    return user_input


def recipe():
    user_input = menu_choose()
    while not (user_input.isdigit() and 0 < int(user_input) < 6):
        print("Sorry, this option does not exist.")
        list_options()
        user_input = menu_choose()

    user_input = int(user_input)
    if user_input == 1:
        add_a_recipe()
    elif user_input == 2:
        user_input = input("Type a recipe name to delete:\n>> ")
        if not (user_input.lower() in
                {k.lower(): v for k, v in cookbook.items()}):
            print("Recipe does not exist, please try agiain.\n")
        else:
            delete_a_recipe(user_input.title())
            print("Recipe", user_input.title(), "deleted.\n")
    elif user_input == 3:
        user_input = input("Please enter a recipe name " +
                           "to get its details:\n>> ")
        if not (user_input.lower() in
                {k.lower(): v for k, v in cookbook.items()}):
            print("Recipe does not exist, please try agiain.\n")
        else:
            print_recipe_details(user_input.title())
    elif user_input == 4:
        print_the_cookbook()
    elif user_input == 5:
        print("Cookbook closed. Goodbye !")
        return False
    return True


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !\n")
    list_options()
    loop = True
    while loop is True:
        loop = recipe()
