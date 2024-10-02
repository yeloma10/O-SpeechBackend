"""
Configuration de Django pour le projet tts_backend.

Généré par 'django-admin startproject' utilisant Django 5.0.2.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/topics/settings/

Pour la liste complète des paramètres et de leurs valeurs, voir
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path  # Importation de la classe Path pour manipuler les chemins

# Construction des chemins à l'intérieur du projet, comme ceci : BASE_DIR / 'sous_dossier'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Définit le répertoire de base du projet


# Paramètres de développement rapides - non adaptés à la production
# Voir https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : gardez la clé secrète utilisée en production secrète !
SECRET_KEY = 'django-insecure-9nd^70o2=tz)*a1goyot%i-7nxxo!kdhbr)-9h=o(#pvco=k&%'

# AVERTISSEMENT DE SÉCURITÉ : ne pas exécuter avec debug activé en production !
DEBUG = True  # Mode de débogage activé pour le développement

ALLOWED_HOSTS = []  # Liste des hôtes autorisés (vide en développement)


# Définition des applications

INSTALLED_APPS = [
    'django.contrib.admin',  # Application d'administration Django
    'django.contrib.auth',  # Application d'authentification
    'django.contrib.contenttypes',  # Gestion des types de contenu
    'django.contrib.sessions',  # Gestion des sessions
    'django.contrib.messages',  # Gestion des messages
    'django.contrib.staticfiles',  # Gestion des fichiers statiques
    'account',  # Application personnalisée pour la gestion des comptes
    'education',  # Application personnalisée pour l'éducation
    'marketing',  # Application personnalisée pour le marketing
    'rest_framework',  # Django REST Framework pour les API
    'rest_framework_simplejwt',  # Support pour JWT dans DRF
    'corsheaders',  # Gestion des en-têtes CORS
    'Speack',  # Application personnalisée pour le projet
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Middleware pour gérer les CORS
    'django.middleware.common.CommonMiddleware',  # Middleware commun
    'django.middleware.security.SecurityMiddleware',  # Middleware de sécurité
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware de session
    'django.middleware.common.CommonMiddleware',  # Middleware commun (répété, peut être retiré)
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware pour la protection CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware d'authentification
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de gestion des messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware pour éviter le clickjacking
]

ROOT_URLCONF = 'tts_backend.urls'  # Configuration des URLs racines

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend pour le rendu des templates
        'DIRS': ['templates'],  # Répertoire des templates
        'APP_DIRS': True,  # Activation de la recherche de templates dans les applications
        'OPTIONS': {
            'context_processors': [  # Liste des processeurs de contexte
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration de l'authentification avec JWT
WSGI_APPLICATION = 'tts_backend.wsgi.application'  # Application WSGI

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (  # Classes d'authentification par défaut
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta  # Importation de timedelta pour gérer les durées

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),  # Durée de vie du token d'accès
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),  # Durée de vie du token de rafraîchissement
    'ROTATE_REFRESH_TOKENS': False,  # Ne pas faire tourner les tokens de rafraîchissement
    'BLACKLIST_AFTER_ROTATION': True,  # Ajouter les tokens à une liste noire après rotation
    'AUTH_HEADER_TYPES': ('Bearer',),  # Types d'en-têtes d'authentification
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  # Classes de tokens d'authentification
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Origines autorisées pour CORS
]

# Base de données
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Moteur de base de données SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Nom du fichier de base de données
    }
}

# Validation des mots de passe
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validation de similarité
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validation de longueur minimale
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validation de mots de passe communs
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validation de mots de passe numériques
    },
]

# Internationalisation
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'  # Code de langue

TIME_ZONE = 'UTC'  # Fuseau horaire

USE_I18N = True  # Activation de l'internationalisation

USE_TZ = True  # Activation de la gestion des fuseaux horaires


# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'  # URL pour accéder aux fichiers statiques

# Type de champ de clé primaire par défaut
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Type de champ auto-incrémenté par défaut
