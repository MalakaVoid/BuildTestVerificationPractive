from .utils import Recipe

"""Template names"""
INDEX_TEMPLATE_NAME = 'recipe_catalog/index.html'
RECIPE_TEMPLATE_NAME = 'recipe_catalog/recipe.html'
ABOUT_TEMPLATE_NAME = 'recipe_catalog/about.html'

"""mock recipes"""
mock_recipes = [
    Recipe({
        'id': 1,
        'name': 'Азу',
        'ingredients': [
            ('Говядина', 150, 125, 2, 300),
            ('Картофель', 80, 60, 3, 50),
            ('Лук репчатый', 80, 60, 1, 30),
            ('Помидоры', 150, 100, 1, 70),
            ('Масло сливочное', 150, 50, 1, 90),
            ('Огурцы', 70, 60, 3, 20)
        ]
    }),
    Recipe({
        "id": 2,
        "name": "Долма",
        "ingredients": [
            ('Говядина', 100, 83, 1, 150),
            ('Свинной фарш', 50, 43, 2, 80),
            ('Репчатый лук', 80, 60, 1, 40),
            ('Листья винограда', 25, 21, 4, 20),
            ('Круглый рис', 100, 80, 1, 40),
            ('Сыр', 80, 60, 1, 120)
        ]
    })
]