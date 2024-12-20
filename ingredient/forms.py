from django import forms  # Importa o módulo de formulários do Django
from .models import RecipeItem, IngredientItem  # Importa os modelos RecipeItem e IngredientItem
from .models import IngredientItem
# Define o formulário para criar ou editar um objeto RecipeItem
class RecipeItemForm(forms.ModelForm):
    # Meta classe usada para configurar o formulário baseado no modelo
    class Meta:
        model = RecipeItem  # Define que o modelo associado ao formulário é RecipeItem
        fields = ['name', 'ingredients', 'directions', 'img_url', 'list_ingredient']  # Campos que aparecerão no formulário

    img_url = forms.ImageField(required=False)  # Define que o campo 'img_url' é do tipo imagem e não é obrigatório
    list_ingredient = forms.ModelMultipleChoiceField(queryset=IngredientItem.objects.all(), widget=forms.CheckboxSelectMultiple)  # Permite selecionar múltiplos ingredientes, exibidos como checkboxes


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientItem
        fields = ['name', 'property', 'img_url']  # Substitua por seus campos do modelo