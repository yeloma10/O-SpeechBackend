from rest_framework.views import APIView  # Importation de la classe APIView pour créer une vue API
from rest_framework.response import Response  # Importation de la classe Response pour retourner des réponses
from rest_framework import status  # Importation des statuts HTTP pour les réponses
from django.http import HttpResponse  # Importation de la classe HttpResponse pour retourner des fichiers
import pyttsx3  # type: ignore # Importation de pyttsx3 pour la conversion de texte en parole
from moviepy.editor import VideoFileClip, AudioFileClip  # Importation de MoviePy pour manipuler des vidéos
import tempfile  # Importation pour créer des fichiers temporaires
import os  # Importation pour manipuler des fichiers et répertoires
from account.serializer import TextToSpeechSerializerVideo  # Importation du sérialiseur pour valider les données

# Définition de la vue pour la conversion de texte en parole et la synchronisation avec une vidéo
class TextToSpeechView(APIView):
    def post(self, request, *args, **kwargs):  # Méthode pour gérer les requêtes POST
        serializer = TextToSpeechSerializerVideo(data=request.data)  # Initialise le sérialiseur avec les données reçues
        if serializer.is_valid():  # Vérifie si les données sont valides
            text = serializer.validated_data.get('text')  # Récupère le texte validé
            language = serializer.validated_data.get('language')  # Récupère la langue validée
            selected_voice = serializer.validated_data.get('selectedVoice')  # Récupère la voix sélectionnée
            video_file = serializer.validated_data.get('videoFile')  # Récupère le fichier vidéo

            try:
                # Création de l'audio à partir du texte avec sélection de voix
                engine = pyttsx3.init()  # Initialise le moteur de synthèse vocale
                voices = engine.getProperty('voices')  # Récupère la liste des voix disponibles

                # Vérifie si la voix sélectionnée est valide
                if selected_voice.isdigit() and int(selected_voice) < len(voices):
                    engine.setProperty('voice', voices[int(selected_voice)].id)  # Définit la voix sélectionnée

                # Crée un fichier audio temporaire pour sauvegarder le son
                audio_fp_name = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
                engine.save_to_file(text, audio_fp_name)  # Sauvegarde l'audio dans un fichier temporaire
                engine.runAndWait()  # Exécute le moteur pour générer le fichier audio

                # Sauvegarde le fichier vidéo dans un fichier temporaire
                video_fp_name = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name
                with open(video_fp_name, 'wb') as video_fp:  # Ouvre le fichier vidéo en mode écriture binaire
                    video_fp.write(video_file.read())  # Écrit le contenu du fichier vidéo

                # Manipulation des vidéos pour ajouter l'audio
                video_clip = VideoFileClip(video_fp_name)  # Charge le clip vidéo
                audio_clip = AudioFileClip(audio_fp_name)  # Charge le clip audio

                # Synchronisation de l'audio et de la vidéo
                final_clip = video_clip.set_audio(audio_clip)  # Associe l'audio au clip vidéo
                final_fp_name = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name
                final_clip.write_videofile(final_fp_name, codec='libx264', audio_codec='aac')  # Écrit le clip final

                # Crée une réponse HTTP avec le fichier vidéo final
                with open(final_fp_name, 'rb') as final_file:  # Ouvre le fichier final en mode lecture binaire
                    response = HttpResponse(final_file.read(), content_type="video/mp4")  # Crée la réponse HTTP
                    response['Content-Disposition'] = 'attachment; filename="synced_video.mp4"'  # Indique que c'est un fichier à télécharger

                # Suppression des fichiers temporaires pour libérer de l'espace
                os.remove(audio_fp_name)  # Supprime le fichier audio temporaire
                os.remove(video_fp_name)  # Supprime le fichier vidéo temporaire
                os.remove(final_fp_name)  # Supprime le fichier vidéo final

                return response  # Retourne la réponse avec le fichier vidéo synchronisé

            except Exception as e:  # Gestion des exceptions
                # Suppression des fichiers temporaires en cas d'erreur
                for temp_file in [audio_fp_name, video_fp_name, final_fp_name]:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)  # Supprime le fichier s'il existe

                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # Retourne une réponse d'erreur

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retourne les erreurs de validation si présentes
