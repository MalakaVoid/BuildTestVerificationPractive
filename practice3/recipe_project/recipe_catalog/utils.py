from pydantic import BaseModel, PositiveInt
from typing import List
from functools import wraps


class Ingredient(BaseModel):
    name: str
    raw_weight: PositiveInt
    weight: PositiveInt
    amount: PositiveInt
    cost: PositiveInt


class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[Ingredient]

    def __init__(self, recipe_info):
        new_ingredients = [Ingredient(name=name, raw_weight=raw_weight, weight=weight, amount=amount, cost=cost)
                           for name, raw_weight, weight, amount, cost in recipe_info['ingredients']]
        super().__init__(id=recipe_info['id'], name=recipe_info['name'], ingredients=new_ingredients)

    @staticmethod
    def validate_portions(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            portions = kwargs.get('portions', args[1] if len(args) > 1 else 1)
            if not isinstance(portions, int) or portions <= 0:
                raise ValueError("Порции должны быть положительным целым числом!")
            return func(*args, **kwargs)

        return wrapper

    @validate_portions
    def calc_cost(self, portions=1):
        total_cost = sum(item.cost * item.amount for item in self.ingredients)
        return total_cost * portions

    @validate_portions
    def calc_weight(self, portions=1, raw=False):
        if not isinstance(raw, bool):
            raise ValueError("Атрибут raw должен быть булевым значением!")

        if raw:
            return sum(item.raw_weight * item.amount for item in self.ingredients) * portions

        return sum(item.weight * item.amount for item in self.ingredients) * portions

    def __str__(self):
        return self.name


def find_recipe_by_id(recipe_id, recipes):
    """
    :param recipe_id: Recipe
    :param recipes: List[Recipe]
    :return: Recipe or None
    """
    recipe = next((recipe for recipe in recipes if recipe.id == recipe_id), None)
    return recipe
