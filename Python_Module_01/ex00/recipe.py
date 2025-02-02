import sys

# for not printing traceback
# sys.tracebacklimit = 0


class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        if not isinstance(name, str):
            raise ValueError("value must be string")
        elif name == '' or name == "":
            raise ValueError("name must not be empty")
        else:
            self.name = name

        if not isinstance(cooking_lvl, int):
            raise ValueError("cooking_lvl must be an integer")
        elif not (1 <= int(cooking_lvl) and int(cooking_lvl) <= 5):
            raise ValueError("cooking_lvl must be between 1 and 5")
        else:
            self.cooking_lvl = cooking_lvl

        if not isinstance(cooking_time, int):
            raise ValueError("cooking_time must be an integer")
        elif not (int(cooking_time) > 0):
            raise ValueError(
                "cooking_time must be bigger than 0 (no negative numbers)")
        else:
            self.cooking_time = cooking_time

        tmp = []
        for i in range(len(ingredients)):
            if len(ingredients[i]) != 0:
                tmp.append(ingredients[i])
        if not isinstance(ingredients, list):
            raise ValueError("ingredients must be passed as list")
        elif len(tmp) == 0:
            raise ValueError("ingredients must not be empty")
        else:
            self.ingredients = tmp
        self.description = description

        recipe_type = recipe_type.lower()
        if len(recipe_type) == 0:
            raise ValueError("recipe_type must not be empty")
        elif not(recipe_type == "starter" or
                 recipe_type == "lunch" or
                 recipe_type == "dessert"):
            raise ValueError("recipe_type must be \"starter\", \"lunch\"," +
                             " or \"dessert\"")
        else:
            self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "  Name: " + self.name + "\n"
        txt += "  Cooking Level: " + str(self.cooking_lvl) + "\n"
        txt += "  Ingredients: " + ', '.join(self.ingredients) + "\n"
        txt += "  Description: " + self.description + "\n"
        txt += "  Recipe type: " + self.recipe_type + "\n"
        return txt
