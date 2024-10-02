from django.shortcuts import render  # Importation de la fonction render pour rendre des templates

# Définition de la vue pour la page d'accueil
def index(request):
    return render(request, 'index.html')  # Rend le template 'index.html' en réponse à la requête
