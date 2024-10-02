from django.apps import AppConfig  # Importation de la classe AppConfig pour configurer l'application

# Définition de la configuration de l'application "education"
class EducationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Spécifie le type de champ auto-incrémenté par défaut
    name = 'education'  # Nom de l'application
