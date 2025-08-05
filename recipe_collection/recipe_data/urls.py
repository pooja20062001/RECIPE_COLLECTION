from django.urls import path
from .import views


urlpatterns=[
    path('',views.recipes,name='recipes'),
    path('add_recipe/',views.add_recipe,name='add_recipe'),
    path('recipe_list/',views.recipe_list,name='recipe_list'),
    path('recipe_edit/<int:id>/',views.recipe_edit,name='recipe_edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
]