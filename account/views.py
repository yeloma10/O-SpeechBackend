from django.shortcuts import render  # Importation de la fonction render pour rendre des templates
from django.contrib.auth import get_user_model  # Importation de la fonction pour obtenir le modèle utilisateur
from rest_framework.views import APIView  # Importation de la classe APIView pour créer des vues API
from rest_framework.response import Response  # Importation de la classe Response pour retourner des réponses
from rest_framework import status  # Importation des statuts HTTP pour les réponses
from rest_framework.permissions import IsAuthenticated  # Importation pour gérer les permissions d'authentification
from rest_framework import generics  # Importation des classes génériques pour simplifier les vues
from .serializer import *  # Importation de tous les sérialiseurs du module serializer
from django.http import JsonResponse  # Importation de la classe JsonResponse pour retourner des réponses JSON

User = get_user_model()  # Obtention du modèle utilisateur

# Vue pour créer un nouvel utilisateur
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()  # Définition de la requête pour tous les utilisateurs
    serializer_class = UserSerializer  # Spécification du sérialiseur à utiliser

# Vue pour récupérer le profil d'un utilisateur
class UserProfileView(generics.RetrieveAPIView):
    def get(self, request, id):  # Méthode pour gérer les requêtes GET
        try:
            user = User.objects.get(pk=id)  # Recherche l'utilisateur par son ID
            user_data = {
                "id": user.id,  # ID de l'utilisateur
                "username": user.username,  # Nom d'utilisateur
                "email": user.email,  # Email de l'utilisateur
                "first_name": user.first_name,  # Prénom de l'utilisateur
                "last_name": user.last_name,  # Nom de famille de l'utilisateur
                # Ajoutez d'autres champs que vous souhaitez exposer
            }
            return JsonResponse(user_data, status=200)  # Retourne les données de l'utilisateur avec un statut 200
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)  # Retourne une erreur si l'utilisateur n'est pas trouvé
