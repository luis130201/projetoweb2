import os

# Define o diretório base do projeto, que é o diretório onde está o manage.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ATENÇÃO DE SEGURANÇA: mantenha a chave secreta usada em produção em segredo!
SECRET_KEY = 'buh1%m)5=9ge@*pw$ypg$vfh#41r#460rv9gtdy@j-w4(+toq*'

# ATENÇÃO DE SEGURANÇA: não execute com o debug ativado em produção!
DEBUG = True

ALLOWED_HOSTS = []  # Define quais domínios ou IPs podem acessar o seu site


# Definição das aplicações (apps) do Django no projeto

INSTALLED_APPS = [
    'django.contrib.admin',  # Administração do Django
    'django.contrib.auth',  # Sistema de autenticação
    'django.contrib.contenttypes',  # Tipo de conteúdo
    'django.contrib.sessions',  # Sessões do Django
    'django.contrib.messages',  # Sistema de mensagens
    'django.contrib.staticfiles',  # Arquivos estáticos (CSS, JS, etc.)
    'ingredient',  # App customizado para ingredientes
]

# Configuração do middleware: componentes que processam as requisições
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Segurança do site
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manipulação de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware comum
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# Arquivo de URLs raiz
ROOT_URLCONF = 'django_project.urls'

# Configuração dos templates (arquivos HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend para renderizar templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório onde os templates são armazenados
        'APP_DIRS': True,  # Permite que cada app tenha seu próprio diretório de templates
        'OPTIONS': {
            'context_processors': [  # Processadores de contexto que adicionam variáveis ao contexto do template
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do WSGI para o servidor de produção
WSGI_APPLICATION = 'django_project.wsgi.application'


# Configuração do banco de dados
# O Django usa SQLite por padrão, mas pode ser configurado para outros bancos

from pathlib import Path

# BASE_DIR agora é um objeto Path para facilitar manipulação de caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Usando SQLite como banco de dados
        'NAME': BASE_DIR / 'db.sqlite3',  # Caminho para o banco de dados
    }
}


# Validação de senhas para garantir que as senhas dos usuários sejam seguras
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Valida a semelhança da senha com o nome de usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Senha precisa ter um comprimento mínimo
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Verifica se a senha é uma senha comum
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Verifica se a senha é apenas numérica
    },
]


# Internacionalização: Configurações de idioma e fuso horário

LANGUAGE_CODE = 'en-us'  # Define o idioma do site
TIME_ZONE = 'UTC'  # Define o fuso horário
USE_I18N = True  # Ativa a internacionalização
USE_L10N = True  # Ativa a localização (formatos regionais)
USE_TZ = True  # Usa fuso horário para as datas


# Configuração de arquivos estáticos (CSS, JavaScript, imagens)

STATIC_URL = '/static/'  # URL para acessar os arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Diretório onde os arquivos estáticos são armazenados
]


# Define o tipo de campo para a chave primária dos modelos, no caso um BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
