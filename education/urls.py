from django.urls import path  # Importation de la fonction path pour définir les URL
from .views import text_to_speech  # Importation de la vue text_to_speech depuis le module views

# Liste des URL de l'application
urlpatterns = [
    # Définition d'une URL pour la conversion de texte en parole
    path('api/education/', text_to_speech, name='education'),  # Associe l'URL 'text-to-speech/' à la vue text_to_speech
]
