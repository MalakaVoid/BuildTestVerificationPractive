from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Ingredient(models.Model):
    """Ingredient model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    raw_weight = models.IntegerField(validators=[MinValueValidator(0)])
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    cost = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredients')

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    """Recipe = Ingredient model"""
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'ingredient')
