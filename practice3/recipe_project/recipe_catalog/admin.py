from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredients


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'raw_weight', 'weight', 'amount', 'cost')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(RecipeIngredients)
class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient')
    search_fields = ('recipe__name', 'ingredient__name')
