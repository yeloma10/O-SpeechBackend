from django.apps import AppConfig  # Importation de la classe AppConfig pour configurer l'application

# Définition de la configuration de l'application "marketing"
class MarketingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Spécifie le type de champ auto-incrémenté par défaut
    name = 'marketing'  # Nom de l'application
