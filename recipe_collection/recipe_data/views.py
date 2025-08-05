from django.shortcuts import render,redirect,get_object_or_404
from .models import Recipe
from.forms import RecipeForm

def recipes(request):
    return render(request,'recipes.html')





def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
            context = {'form': form, 'action': 'Add'}
    else:
        form = RecipeForm()
        context = {'form': form, 'action': 'Add'}

    return render(request, 'add_recipe.html', context)  # Use add template here

                                           
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_edit.html', {'form': form, 'action': 'Edit'})  # Use edit template here


def recipe_list(request):
    search = request.GET.get("search")
    if search:
        all_recipes = Recipe.objects.filter(title__icontains=search)
    else:
        all_recipes = Recipe.objects.all()

    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'recipe_list.html', context)
    


def delete(request,id):
        task=get_object_or_404(Recipe,id=id)
        task.delete()
        return redirect('recipes')



        
