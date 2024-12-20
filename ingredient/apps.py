from django.apps import AppConfig

# A classe 'IngredientConfig' é responsável pela configuração da aplicação 'ingredient' no Django.
# Ela herda de 'AppConfig', que é a classe base para configurar aplicativos Django.

class IngredientConfig(AppConfig):
    name = 'ingredient'  # Define o nome da aplicação. O Django usará esse nome para localizar a aplicação.
