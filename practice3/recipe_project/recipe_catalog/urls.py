from django.urls import path
from .views import about, index, recipe_details


urlpatterns = [
    path('', index, name='main'),
    path('recipe/<int:pk>/', recipe_details, name='receipt'),
    path('about', about, name='about'),
]
