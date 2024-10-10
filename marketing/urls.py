from django.urls import path  # Importation de la fonction path pour définir les URL
from .views import *  # Importation de toutes les vues du module views

# Liste des URL de l'application
urlpatterns = [
    # Définition d'une URL pour la vue de conversion de texte en parole
    path('api/marketting/', TextToSpeechView.as_view(), name='marketing')  # Associe l'URL 'api/marketting/' à la vue TextToSpeechView
]
