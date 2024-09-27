"""
    Практическая работа №2
    АЗБУКИН ДАНИИЛ ЮРЬЕВИЧ БСБО-10-21
"""

class Ingredient:

    def __init__(self, name, raw_weight, weight, amount, cost):
        self.name = name
        self.raw_weight = raw_weight
        self.weight = weight
        self.amount = amount
        self.cost = cost


class Recipe:

    def __init__(self, name, ingredients):
        self.ingredients = [Ingredient(name=name, raw_weight=raw_weight, weight=weight, amount=amount, cost=cost)
                            for name, raw_weight, weight, amount, cost in ingredients]
        self.name = name

