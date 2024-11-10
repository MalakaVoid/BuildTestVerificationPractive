from django.test import TestCase, Client
from django.urls import reverse
from ..models import Ingredient, Recipe, RecipeIngredients


class TestMain(TestCase):
    MAIN_PAGE_URL = reverse('main')
    RECIPE_NAME = "Pancakes"

    def setUp(self):
        self.recipe = Recipe.objects.create(name=self.RECIPE_NAME)
        self.client = Client()

    def test_status_code(self):
        response = self.client.get(self.MAIN_PAGE_URL)
        self.assertEqual(response.status_code, 200)


    def test_context(self):
        response = self.client.get(self.MAIN_PAGE_URL)
        self.assertIn('recipes', response.context)

    def test_validate_recipe_name(self):
        response = self.client.get(self.MAIN_PAGE_URL)
        self.assertEqual(response.context['recipes'][0].name, self.RECIPE_NAME)

    def test_recipes_amount(self):
        response = self.client.get(self.MAIN_PAGE_URL)
        self.assertEqual(len(response.context['recipes']), 1)

    def tearDown(self):
        self.recipe.delete()


class TestAbout(TestCase):
    ABOUT_PAGE_URL = reverse('about')

    def setUp(self):
        self.recipe = Recipe.objects.create(name="Pancakes")
        self.client = Client()

    def test_status_code(self):
        response = self.client.get(self.ABOUT_PAGE_URL)
        self.assertEqual(response.status_code, 200)


class TestRecipes(TestCase):
    CONTEXT_FIELDS = (
        "recipe",
        "recipe_ingredients",
        "total_cost",
        "total_weight",
    )
    INGREDIENTS = [
        dict(name="Соль", measuring="грамм", cost=0.05,  measure=5, measure_weight=5),
        dict(name="Сахар", measuring="грамм", cost=0.1, measure=10, measure_weight=10),
        dict(name="Мука", measuring="грамм", cost=0.2, measure=100, measure_weight=100)
    ]

    def setUp(self):
        self.ingredients = []
        self.recipe = Recipe.objects.create(name="Блинчики")

        for ingredient in self.INGREDIENTS:
            self.ingredients.append(Ingredient.objects.create(name=ingredient["name"],
                                      measuring=ingredient["measuring"],
                                      cost=ingredient["cost"]))
        for ingredient, ingredient_class in zip(self.INGREDIENTS, self.ingredients):
            RecipeIngredients.objects.create(recipe=self.recipe,
                                             ingredient=ingredient_class,
                                             measure=ingredient["measure"],
                                             measure_weight=ingredient["measure_weight"])

        self.total_cost = sum([ingredient['measure'] * ingredient['cost']
                               for ingredient in self.INGREDIENTS])
        self.total_weight = sum([ingredient['measure_weight'] * ingredient['measure']
                            for ingredient in self.INGREDIENTS])

        self.client = Client()

    def get_response(self):
        response = self.client.get(reverse('receipt',
                                           kwargs={'pk': self.recipe.id}))
        return response

    def test_status_code(self):
        response = self.get_response()
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.get_response()
        length = sum([1 for key in self.CONTEXT_FIELDS if key in response.context])
        self.assertEqual(length, len(self.CONTEXT_FIELDS))

    def test_total_weight_calculation(self):
        response = self.get_response()
        self.assertEqual(response.context['total_weight'], self.total_weight)

    def test_total_cost_calculation(self):
        response = self.get_response()
        self.assertEqual(response.context['total_cost'], self.total_cost)
