from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import IngredientItem, RecipeItem

# Personalização do formulário para IngredientItem
class IngredientItemForm(forms.ModelForm):
    class Meta:
        model = IngredientItem
        fields = '__all__'
        widgets = {
            'property': forms.Textarea(attrs={'rows': 10, 'cols': 40}),  # Campo maior
        }

# Personalização do formulário para RecipeItem
class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = '__all__'
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
            'directions': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }

# Personalização do Admin para IngredientItem
class IngredientItemAdmin(admin.ModelAdmin):
    form = IngredientItemForm
    list_display = ('name', 'formatted_property', 'img_url')

    def formatted_property(self, obj):
        return format_html(obj.property.replace("\n", "<br>"))
    formatted_property.short_description = 'Property (Formatted)'

# Personalização do Admin para RecipeItem
class RecipeItemAdmin(admin.ModelAdmin):
    form = RecipeItemForm
    list_display = ('name', 'formatted_ingredients', 'directions', 'img_url')

    def formatted_ingredients(self, obj):
        return format_html(obj.ingredients.replace("\n", "<br>"))
    formatted_ingredients.short_description = 'Ingredients (Formatted)'

# Registra os modelos no Django Admin
admin.site.register(IngredientItem, IngredientItemAdmin)
admin.site.register(RecipeItem, RecipeItemAdmin)
