"""
Configuration ASGI pour le projet tts_backend.

Elle expose l callable ASGI comme une variable de niveau module nommée ``application``.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os  # Importation du module os pour interagir avec le système d'exploitation

from django.core.asgi import get_asgi_application  # Importation de la fonction pour obtenir l'application ASGI

# Définit la variable d'environnement pour le module de paramètres de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tts_backend.settings')

# Obtention de l'application ASGI
application = get_asgi_application()  # Exposition de l'application ASGI pour le déploiement
