from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import IngredientItem, RecipeItem
from .forms import RecipeItemForm, IngredientForm  # Importando o formulário para ingredientes
import json

# View para listar e adicionar ingredientes
def ingredientView(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_view')  # Redireciona para a própria página após salvar
    else:
        form = IngredientForm()

    all_ingredients = IngredientItem.objects.all()
    return render(request, 'ingredient.html', {'all_ingredients': all_ingredients, 'form': form})

# View para adicionar uma receita
def add_recipe(request):
    if request.method == "POST":
        form = RecipeItemForm(request.POST, request.FILES)  # Inclua request.FILES para uploads
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirecione para outra página após salvar
    else:
        form = RecipeItemForm()

    return render(request, 'add_recipe.html', {'form': form})

# View para buscar receitas associadas a um ingrediente
def searchView(request, ingredientId):
    ingredientObject = get_object_or_404(IngredientItem, id=ingredientId)
    # Verifique se o filtro está correto, para evitar receitas não associadas ao ingrediente
    all_recipes = RecipeItem.objects.filter(list_ingredient=ingredientObject)

    list_recipes = [
        {
            'name': recipe.name,
            'ingredients': recipe.ingredients.split('#'),
            'directions': recipe.directions.split('#'),
            'img_url': recipe.img_url
        }
        for recipe in all_recipes
    ]

    return render(request, 'searchRecipe.html', {
        'ingredientObject': ingredientObject,
        'list_recipes': list_recipes
    })

# View para adicionar um novo ingrediente
def add_ingredient(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)  # Não é necessário passar request.FILES
        if form.is_valid():
            form.save()
            return redirect('ingredient_view')  # Redireciona para a página de ingredientes após salvar
    else:
        form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form})

# Obter ID do ingrediente por nome
def get_ingredientId(request, ingredientName):
    if request.method == 'GET':
        try:
            ingredientId = IngredientItem.objects.get(name=ingredientName).id
            response = json.dumps([{'ingredientId': ingredientId}])
        except IngredientItem.DoesNotExist:
            response = json.dumps([{'Error': 'No id with that name'}])
    return HttpResponse(response, content_type='text/json')

# Obter receitas correspondentes a uma lista de ingredientes
@csrf_exempt
def get_match_recipe(request):
    if request.method == 'POST':
        payload = json.loads(request.body).get('listIngredient', [])
        try:
            response = []
            for recipe in RecipeItem.objects.all():
                ingredient_names = [ingredient.name for ingredient in recipe.list_ingredient.all()]
                if set(payload).issubset(set(ingredient_names)):
                    response.append({
                        'name': recipe.name,
                        'ingredients': recipe.ingredients.split('#'),
                        'directions': recipe.directions.split('#'),
                        'img_url': recipe.img_url
                    })
            response = json.dumps(response)
        except Exception as e:
            response = json.dumps([{'Error': str(e)}])
    return HttpResponse(response, content_type='text/json')
