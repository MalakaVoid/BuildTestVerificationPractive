from django.shortcuts import render
from .constants import INDEX_TEMPLATE_NAME, RECIPE_TEMPLATE_NAME, ABOUT_TEMPLATE_NAME, mock_recipes
from .utils import find_recipe_by_id
from django.http import Http404


def index(request):
    recipes = mock_recipes
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
    recipe = find_recipe_by_id(pk, mock_recipes)

    if not recipe:
        raise Http404("Рецепт не найден")

    context = {
        "recipe": recipe
    }

    return render(request, RECIPE_TEMPLATE_NAME, context)


def about(request):
    return render(request, ABOUT_TEMPLATE_NAME)
