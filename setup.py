import sys
from cx_Freeze import setup, Executable

# Liste des fichiers sources
sources = ['main.py', 'UserInterface.py', 'PasswordGenerator.py']

# Paramètres de l'exécutable
executable = Executable(
    script='main.py',
    base='Console',  # Utilisez 'Console' si vous utilisez l'invite de commandes
    targetName='/mnt/c/Users/idaff/Desktop/PY-password-manager/password_generator.exe',  # Nom du fichier exécutable de sortie
    icon='password.png'  # Chemin vers l'icône de l'application (facultatif)
)

# Options de configuration
options = {
    'build_exe': {
        'includes': ['smtplib', 'ssl'],  # Liste des modules supplémentaires à inclure
        'excludes': [],
        'packages': ['string', 'random'],
        'include_files': [],  # Liste des fichiers supplémentaires à inclure (ex. : des icônes, des images, etc.)
        'compress': False  # Désactiver la compression UPX
    }
}

# Appel à la fonction de setup
setup(
    name='Password Generator',
    version='1.0',
    description='Generate secure passwords',
    executables=[executable],
    options=options
)