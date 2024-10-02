from rest_framework import serializers  # Importation du module serializers de DRF

# Définition d'un sérialiseur pour la conversion de texte en parole
class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=5000)  # Champ pour le texte, avec une longueur maximale de 5000 caractères
    language = serializers.CharField(max_length=10)  # Champ pour la langue, avec une longueur maximale de 10 caractères
    selectedVoice = serializers.CharField(max_length=10)  # Champ pour la voix sélectionnée, avec une longueur maximale de 10 caractères
