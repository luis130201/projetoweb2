from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ingredient.views import (
    ingredientView,
    searchView,
    get_ingredientId,
    get_match_recipe,
    add_recipe,
    add_ingredient  # Importando a view add_ingredient
)

urlpatterns = [
    # Administração
    path('admin/', admin.site.urls),

    # Views de ingredientes
    path('', ingredientView, name='ingredient_view'),  # Página de ingredientes
    path('search/<int:ingredientId>/', searchView, name='search_view'),  # Pesquisa de receitas
    path('add_recipe/', add_recipe, name='add_recipe'),  # Adicionar nova receita

    # API
    path('api/ingredient_id/<ingredientName>/', get_ingredientId, name='get_ingredient_id'),
    path('api/match_recipe/', get_match_recipe, name='match_recipe'),

    # URL para adicionar ingredientes
    path('add-ingredient/', add_ingredient, name='add_ingredient'),  # Nova URL para adicionar ingrediente
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)