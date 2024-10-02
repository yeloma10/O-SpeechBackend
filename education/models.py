from django.db import models  # Importation du module models pour définir les modèles de la base de données
from django.contrib.auth.models import User  # Importation du modèle User pour gérer les utilisateurs

# Création de modèles pour l'application

class Parametre_vocal(models.Model):  # Définition d'un modèle pour les paramètres vocaux
    vitesse = models.IntegerField()  # Champ pour la vitesse de la voix (entier)
    langue = models.CharField(max_length=255)  # Champ pour la langue, avec une longueur maximale de 255 caractères
    voix = models.CharField(max_length=255)  # Champ pour la voix, avec une longueur maximale de 255 caractères

class Contenu(models.Model):  # Définition d'un modèle pour le contenu de l'utilisateur
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien vers le modèle User, avec suppression en cascade
    text = models.TextField()  # Champ pour le texte, pouvant contenir un texte long
    parametre = models.OneToOneField(Parametre_vocal, on_delete=models.CASCADE)  # Lien vers les paramètres vocaux, avec une relation un à un
