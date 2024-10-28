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
    ingredients = recipe.ingredients.all()

    context = {
        "recipe": recipe,
        "recipe_ingredients":ingredients
    }

    return render(request, RECIPE_TEMPLATE_NAME, context)


def about(request):
    """About page handler"""
    return render(request, ABOUT_TEMPLATE_NAME)
