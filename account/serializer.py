from rest_framework import serializers  # Importation du module serializers de DRF
from django.contrib.auth.models import User  # Importation du modèle User de Django
from django.contrib.auth import get_user_model  # Importation de la fonction pour obtenir le modèle utilisateur

User = get_user_model()  # Obtention du modèle utilisateur

# Définition du sérialiseur pour l'utilisateur
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Spécifie le modèle à utiliser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']  # Champs à inclure dans le sérialiseur
        extra_kwargs = {'password': {'write_only': True}}  # Indique que le mot de passe est en écriture uniquement

    def create(self, validated_data):  # Méthode pour créer un nouvel utilisateur
        user = User.objects.create_user(
            username=validated_data['username'],  # Récupère le nom d'utilisateur
            first_name=validated_data['first_name'],  # Récupère le prénom
            last_name=validated_data['last_name'],  # Récupère le nom de famille
            email=validated_data['email'],  # Récupère l'email
            password=validated_data['password']  # Récupère le mot de passe
        )
        return user  # Retourne l'utilisateur créé

# Définition du sérialiseur pour la conversion texte en parole
class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=115000)  # Champ pour le texte, longueur maximale de 115000 caractères
    language = serializers.CharField(max_length=10)  # Champ pour la langue, longueur maximale de 10 caractères
    selectedVoice = serializers.CharField(max_length=10)  # Champ pour la voix sélectionnée, longueur maximale de 10 caractères

# Sérialiseur pour la conversion texte en parole avec vidéo (décommenté)
# class TextToSpeechSerializerVideo(serializers.Serializer):
#     text = serializers.CharField(max_length=5000)
#     language = serializers.CharField(max_length=5)
#     selectedVoice = serializers.CharField(max_length=10)
#     videoFile = serializers.FileField()

# Définition du sérialiseur pour la conversion texte en parole avec vidéo
class TextToSpeechSerializerVideo(serializers.Serializer):
    text = serializers.CharField()  # Champ pour le texte
    language = serializers.CharField()  # Champ pour la langue
    selectedVoice = serializers.CharField()  # Champ pour la voix sélectionnée
    videoFile = serializers.FileField()  # Champ pour le fichier vidéo

# Définition du sérialiseur pour le profil de l'utilisateur
class UserSerializerProfile(serializers.ModelSerializer):
    class Meta:
        Model = User  # Spécifie le modèle à utiliser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Champs à inclure dans le sérialiseur
