from django.shortcuts import render
from .constants import INDEX_TEMPLATE_NAME, RECIPE_TEMPLATE_NAME, ABOUT_TEMPLATE_NAME
from .utils import check_recipe_existence
from django.http import Http404
from .models import Ingredient, RecipeIngredients, Recipe


def index(request):
    """Main page handler"""
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'recipes_len': len(recipes)
    }
    return render(
        request=request,
        template_name=INDEX_TEMPLATE_NAME,
        context=context
    )


def recipe_details(request, pk):
    """Specific recipe details handler"""
    if not check_recipe_existence(pk):
        raise Http404("Рецепт не найден")

    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = RecipeIngredients.objects.filter(recipe=recipe)

    ingredients_list = [
        {
            'id': recipe_ingredient.ingredient.id,
            'name': recipe_ingredient.ingredient.name,
            'measuring': recipe_ingredient.ingredient.measuring,
            'measure': recipe_ingredient.measure,
            'measure_weight': recipe_ingredient.measure_weight,
            'cost': recipe_ingredient.measure *
                    recipe_ingredient.ingredient.cost,

        }
        for recipe_ingredient in recipe_ingredients
    ]

    total_cost = sum([ingredient['cost'] for ingredient in ingredients_list])
    total_weight = sum([ingredient['measure_weight'] * ingredient['measure']
                      for ingredient in ingredients_list])

    context = {
        "recipe": recipe,
        "recipe_ingredients": ingredients_list,
        "total_cost": total_cost,
        "total_weight": total_weight
    }

    return render(request, RECIPE_TEMPLATE_NAME, context)


def about(request):
    """About page handler"""
    return render(request, ABOUT_TEMPLATE_NAME)
