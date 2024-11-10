from django.core.exceptions import ValidationError
from django.test import TestCase
from ..models import Ingredient, RecipeIngredients, Recipe


class TestDbCreation(TestCase):
    """Тесты успешного создания в бд"""

    INGREDIENT_NAME = 'Тестовый ингредиент'
    INGREDIENT_MEASURING = 'грамм'
    INGREDIENT_COST = 10
    INGREDIENT_MEASURE = 100
    INGREDIENT_MEASURE_WEIGHT = 1
    RECIPE_NAME = 'Тестовый рецепт'

    @ classmethod
    def setUpTestData(cls):
        cls.ingredient_test = Ingredient.objects.create(
            name = cls.INGREDIENT_NAME,
            measuring = cls.INGREDIENT_MEASURING,
            cost = cls.INGREDIENT_COST
        )
        cls.recipe_test = Recipe.objects.create(
            name = cls.RECIPE_NAME
        )
        cls.recipe_ingredient_test = RecipeIngredients.objects.create(
            recipe = cls.recipe_test,
            ingredient = cls.ingredient_test,
            measure = cls.INGREDIENT_MEASURE,
            measure_weight = cls.INGREDIENT_MEASURE_WEIGHT
        )

    def test_validate_ingredient_name(self):
        """Валидация имени созданного ингредиента"""
        ingredient = Ingredient.objects.get(id=self.ingredient_test.id)
        self.assertEqual(ingredient.name, self.INGREDIENT_NAME)

    def test_validate_ingredient_measuring(self):
        """Валидация вида измерения созданного ингредиента"""
        ingredient = Ingredient.objects.get(id=self.ingredient_test.id)
        self.assertEqual(ingredient.measuring, self.INGREDIENT_MEASURING)

    def test_validate_ingredient_cost(self):
        """Валидация цены созданного ингредиента"""
        ingredient = Ingredient.objects.get(id=self.ingredient_test.id)
        self.assertEqual(ingredient.cost, self.INGREDIENT_COST)

    def test_validate_recipe_name(self):
        """Валидация имени созданного рецепта"""
        recipe = Recipe.objects.get(id=self.recipe_test.id)
        self.assertEqual(recipe.name, self.RECIPE_NAME)

    def test_validate_recipe_ingredients_count(self):
        recipe = Recipe.objects.get(id=self.recipe_test.id)
        self.assertEqual(recipe.ingredients.count(), 1)

    def test_validate_ingredient_measure(self):
        """Валидация измерения созданного ингредиента в рецепте"""
        recipe = Recipe.objects.get(id=self.recipe_test.id)
        recipe_ingredients = RecipeIngredients.objects.filter(recipe=recipe)
        self.assertEqual(recipe_ingredients[0].measure, self.INGREDIENT_MEASURE)

    def test_validate_ingredient_measure_weight(self):
        """Валидация веса по умолчанию созданного ингредиента в рецепте"""
        recipe = Recipe.objects.get(id=self.recipe_test.id)
        recipe_ingredients = RecipeIngredients.objects.filter(recipe=recipe)
        self.assertEqual(recipe_ingredients[0].measure_weight, self.INGREDIENT_MEASURE_WEIGHT)

    @classmethod
    def tearDownClass(cls):
        cls.ingredient_test.delete()
        cls.recipe_test.delete()


class ErrorTests(TestCase):
    INGREDIENT_NAME = 'TEST'
    INGREDIENT_MEASURING = 'TEST'
    INGREDIENT_COST = 10
    SUP_INGREDIENT_COST = 15

    def test_ingredient_name_unique(self):
        """Проверка уникальности имени ингредиента"""
        Ingredient.objects.create(name=self.INGREDIENT_NAME,
                                  measuring=self.INGREDIENT_MEASURING,
                                  cost=self.INGREDIENT_COST)
        with self.assertRaises(ValidationError):
            ingredient = Ingredient(name=self.INGREDIENT_NAME,
                                    measuring=self.INGREDIENT_MEASURING,
                                    cost=self.SUP_INGREDIENT_COST)
            ingredient.full_clean()

    def test_ingredient_cost_min_value(self):
        """Проверка минимального значения для стоимости ингредиента"""
        with self.assertRaises(ValidationError):
            ingredient = Ingredient(name=self.INGREDIENT_NAME,
                                    measuring=self.INGREDIENT_MEASURING,
                                    cost=0.0)
            ingredient.full_clean()

    def test_recipe_name_unique(self):
        """Проверка уникальности имени рецепта"""
        Recipe.objects.create(name="Cake")
        with self.assertRaises(ValidationError):
            recipe = Recipe(name="Cake")
            recipe.full_clean()


class RecipeIngredientsErrorTests(TestCase):
    def setUp(self):
        """Создаем тестовые данные для ингредиента и рецепта"""
        self.ingredient = Ingredient.objects.create(name="Тест", measuring="грамм", cost=2.0)
        self.recipe = Recipe.objects.create(name="Тест")

    def test_recipe_ingredient_unique_together(self):
        """Проверка уникальности пары рецепт-ингредиент"""
        RecipeIngredients.objects.create(
            recipe=self.recipe,
            ingredient=self.ingredient,
            measure=50,
            measure_weight=100
        )
        with self.assertRaises(ValidationError):
            duplicate_entry = RecipeIngredients(
                recipe=self.recipe,
                ingredient=self.ingredient,
                measure=30,
                measure_weight=50
            )
            duplicate_entry.full_clean()

    def test_recipe_ingredient_measure_min_value(self):
        """Проверка минимального значения для количества ингредиента"""
        with self.assertRaises(ValidationError):
            recipe_ingredient = RecipeIngredients(
                recipe=self.recipe,
                ingredient=self.ingredient,
                measure=0,
                measure_weight=100
            )
            recipe_ingredient.full_clean()



