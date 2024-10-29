from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredients


class IngredientInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 5


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'raw_weight', 'weight', 'amount', 'cost')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    inlines = [IngredientInline]
