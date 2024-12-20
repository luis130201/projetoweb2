import os

from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente DJANGO_SETTINGS_MODULE, indicando o arquivo de configurações do Django
# Esse arquivo contém todas as configurações necessárias para o funcionamento do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# Cria a aplicação WSGI que o servidor usará para interagir com o Django
# Essa é a interface entre o servidor web e o código do Django
application = get_wsgi_application()
