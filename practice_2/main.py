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
    name: str
    ingredients: List[Ingredient]

    def __init__(self, name, ingredients):
        new_ingredients = [Ingredient(name=name, raw_weight=raw_weight, weight=weight, amount=amount, cost=cost)
                           for name, raw_weight, weight, amount, cost in ingredients]
        super().__init__(name=name, ingredients=new_ingredients)

    @staticmethod
    def validate_portions(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            portions = kwargs.get('portions', args[1] if len(args) > 1 else None)
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


if __name__ == '__main__':

    receipt_from_api = {
        'title': 'Азу',
        'ingredients_list': [
            ('Говядина', 150, 125, 2, 300),
            ('Картофель', 80, 60, 3, 50),
            ('Лук репчатый', 80, 60, 1, 30),
            ('Помидоры', 150, 100, 1, 70),
            ('Масло сливочное', 150, 50, 1, 90),
            ('Огурцы', 70, 60, 3, 20)
        ]
    }

    receipt = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    print(f'Рецепт: {str(receipt)}')
    print(f"Стоимость 1 порции: {receipt.calc_cost()}")
    print(f"Вес 1 порции: {receipt.calc_weight()}")
    print(f"Сырой вес 1 порции: {receipt.calc_weight(raw=True)}")
