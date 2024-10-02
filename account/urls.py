from django.urls import path  # Importation de la fonction path pour définir les URL
from .views import *  # Importation de toutes les vues du module views
from rest_framework_simplejwt.views import (  # Importation des vues pour la gestion des tokens JWT
    TokenObtainPairView,
    TokenRefreshView,
)

# Liste des URL de l'application
urlpatterns = [
    path('api/register/', UserCreateView.as_view(), name='user-register'),  # URL pour l'enregistrement d'un nouvel utilisateur
    path('api/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL pour obtenir un token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL pour rafraîchir un token JWT
    path('profile/<int:id>/', UserProfileView.as_view(), name='user-profile'),  # URL pour récupérer le profil d'un utilisateur par ID
]
