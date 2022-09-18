from multiprocessing.sharedctypes import Value
import sys
import datetime

from recipe import Recipe


class Book:

    def __init__(self, name=None):

        if name:
            self.name = name
        else:
            self.name = ""
        # ref:
        # https://stackoverflow.com/questions/11040177/datetime-round-trim-number-of-digits-in-microseconds
        time = datetime.datetime.now()
        self.last_update = time
        self.creation_date = time

        self.recipes_list = {
            "starter": set(),
            "lunch": set(),
            "dessert": set(),
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the \
            instance"""
        result = None
        for recipe_set in self.recipes_list.values():
            for recipe in recipe_set:
                if recipe.name == name:
                    print(recipe)
                    result = recipe
        return result
        # gen = (recipe.name for recipe in recipe_set if recipe.name == name)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not (recipe_type == "starter" or
                recipe_type == "lunch" or
                recipe_type == "dessert"):
            raise ValueError(
                "recipe_type must be starter, lunch, or dessert")
        name_list = []
        if not (self.recipes_list.get(recipe_type)):
            return None
        for recipe in self.recipes_list.get(recipe_type):
            # name_list.append(recipe.name)
            name_list.append(recipe)

        return name_list

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].add(recipe)
        self.last_update = datetime.datetime.now()
