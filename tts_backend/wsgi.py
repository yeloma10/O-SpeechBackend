"""
WSGI config pour le projet tts_backend.

Il expose l callable WSGI comme une variable de niveau module nommée ``application``.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os  # Importation du module os pour interagir avec le système d'exploitation

from django.core.wsgi import get_wsgi_application  # Importation de la fonction pour obtenir l'application WSGI

# Définit la variable d'environnement pour le module de paramètres de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tts_backend.settings')

# Obtention de l'application WSGI
application = get_wsgi_application()  # Exposition de l'application WSGI pour le déploiement
