"""
Configuration des URL pour le projet tts_backend.

La liste `urlpatterns` associe les URL aux vues. Pour plus d'informations, veuillez consulter :
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemples :
Vues fonctionnelles
    1. Ajoutez un import :  from my_app import views
    2. Ajoutez une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajoutez un import :  from other_app.views import Home
    2. Ajoutez une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclusion d'une autre configuration d'URL
    1. Importez la fonction include() : from django.urls import include, path
    2. Ajoutez une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # Importation de l'administration Django
from django.urls import path, include  # Importation des fonctions pour définir les URL et inclure d'autres fichiers d'URL

# Liste des URL du projet
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour accéder au panneau d'administration
    path("account/", include("account.urls")),  # Inclusion des URL de l'application "account"
    path("education/", include("education.urls")),  # Inclusion des URL de l'application "education"
    path("marketing/", include("marketing.urls")),  # Inclusion des URL de l'application "marketing"
    path("", include('Speack.urls'))  # Inclusion des URL de l'application "Speack" pour la racine
]
