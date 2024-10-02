#!/usr/bin/env python
"""Utilitaire en ligne de commande de Django pour les tâches administratives."""
import os  # Importation du module os pour interagir avec le système d'exploitation
import sys  # Importation du module sys pour accéder aux arguments de la ligne de commande


def main():
    """Exécute les tâches administratives."""
    # Définit la variable d'environnement pour le module de paramètres de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tts_backend.settings')
    try:
        # Tente d'importer la fonction pour exécuter les commandes de gestion de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Êtes-vous sûr qu'il est installé et "
            "disponible dans votre variable d'environnement PYTHONPATH ? Avez-vous "
            "oublié d'activer un environnement virtuel ?"
        ) from exc  # Propage l'exception d'importation
    # Exécute la ligne de commande Django avec les arguments fournis
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()  # Appelle la fonction main si le script est exécuté directement
