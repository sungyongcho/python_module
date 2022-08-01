import sys
import datetime

from recipe import Recipe



class Book:

    def __init__(self):
        self.name = ""
        self.last_update = datetime.time()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {
            "starter": set(),
            "lunch": set(),
            "dessert": set(),
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_set in self.recipes_list.values():
            for recipe in recipe_set:
                if recipe.name == name:
                    return recipe
        # gen = (recipe.name for recipe in recipe_set if recipe.name == name)


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        name_list = []
        for recipe in self.recipes_list.get(recipe_type):
            name_list.append(recipe.name)
        return name_list


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].add(recipe)
        self.last_update = datetime.datetime.now()


aaa = Book()

bbb = Recipe('aaa', 1, ['', 'aa', 'bb'],
             "aaaaaaaaaa bbbbbbbbbb. dddddddddd.", "LUnch")

aaa.add_recipe(bbb)

print(aaa.last_update)
print(aaa.get_recipe_by_name('aaa'))
# print(aaa.get_recipes_by_types('lunch'))
print(aaa.get_recipes_by_types('lunch'))
