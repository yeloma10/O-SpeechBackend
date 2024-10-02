from django.urls import path  # Importation de la fonction path pour définir les URL
from . import views  # Importation des vues du module courant

# Liste des URL de l'application
urlpatterns = [
    path('', views.index)  # URL pour la page d'accueil, associée à la vue 'index'
]
