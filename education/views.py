from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
import pyttsx3 # type: ignore
from io import BytesIO
from account.serializer import TextToSpeechSerializer

@api_view(['POST'])  # Indique que cette vue accepte uniquement les requêtes POST
def text_to_speech(request):  # Définition de la fonction de conversion texte en parole
    serializer = TextToSpeechSerializer(data=request.data)  # Initialise le sérialiseur avec les données reçues
    if serializer.is_valid():  # Vérifie si les données sont valides
        text = serializer.validated_data['text']  # Récupère le texte validé
        selected_voice = serializer.validated_data['selectedVoice']  # Récupère la voix sélectionnée

        try:
            # Initialise le moteur de synthèse vocale
            engine = pyttsx3.init()

            # Récupère les voix disponibles
            voices = engine.getProperty('voices')

            # Sélectionne la voix correspondant à l'ID choisi
            if selected_voice.isdigit() and int(selected_voice) < len(voices):
                engine.setProperty('voice', voices[int(selected_voice)].id)
            else:
                return JsonResponse({'error': 'Sélection de voix invalide'}, status=400)

            # Crée un flux en mémoire pour le fichier audio
            speech_file = BytesIO()
            engine.save_to_file(text, speech_file)  # Enregistre l'audio dans le flux BytesIO
            engine.runAndWait()  # Exécute le moteur
            
            # Réinitialise le pointeur du flux au début
            speech_file.seek(0)

            # Crée une réponse HTTP avec le fichier audio
            response = HttpResponse(speech_file.getvalue(), content_type='audio/wav')
            response['Content-Disposition'] = 'attachment; filename="speech.wav"'  # Indique que c'est un fichier à télécharger
            
            return response  # Retourne la réponse avec l'audio
        except Exception as e:  # Gestion des exceptions
            return JsonResponse({'error': str(e)}, status=500)  # Retourne une réponse JSON avec l'erreur
    else:
        return JsonResponse(serializer.errors, status=400)  # Retourne les erreurs de validation
