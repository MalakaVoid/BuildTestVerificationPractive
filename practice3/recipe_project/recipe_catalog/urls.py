from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .constants import LOGIN_TEMPLATE_NAME
from .views import about, index, recipe_details, register, add_recipe, add_ingredient, my_recipes, delete_recipe, \
    manage_recipes, delete_ingredient, edit_ingredient, add_ingredient_to_recipe_action, edit_ingredient_form, \
    edit_recipe

urlpatterns = [
    path('', index, name='main'),
    path('recipe/<int:pk>/', recipe_details, name='receipt'),
    path('about', about, name='about'),
    path('login/', LoginView.as_view(template_name=LOGIN_TEMPLATE_NAME), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('my_recipes/', my_recipes, name='my_recipes'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('add_ingredient/', add_ingredient, name='add_ingredient'),
    path('delete_recipe/<int:pk>/', delete_recipe, name='delete_recipe'),
    path('edit_recipe/<int:pk>/', edit_recipe, name='edit_recipe'),
    path('manage_recipes/', manage_recipes, name='manage_recipes'),
    path('manage_recipes/delete_ingredient/<int:recipe_id>/', delete_ingredient, name='delete_ingredient'),
    path('manage_recipes/edit_ingredient/<int:recipe_id>/', edit_ingredient, name='edit_ingredient'),
    path('manage_recipes/add_ingredient_to_recipe/<int:recipe_id>/', add_ingredient_to_recipe_action, name='add_ingredient_to_recipe_action'),
    path('manage_recipes/edit_ingredient_form/<int:recipe_id>/<int:ingredient_id>/', edit_ingredient_form, name='edit_ingredient_form'),
]
