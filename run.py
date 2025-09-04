#!/usr/bin/env python3
"""
Script de lancement pour l'application GbGescom
"""
import subprocess
import sys
import os

def install_requirements():
    """Installe les dépendances requises"""
    try:
        print("Installation des dépendances...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dépendances installées avec succès!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erreur lors de l'installation des dépendances: {e}")
        return False

def run_app():
    """Lance l'application Flask"""
    try:
        print("\n" + "="*50)
        print("🏪 LANCEMENT DE GBGESCOM")
        print("="*50)
        print("📍 URL: http://localhost:5000")
        print("🔧 Mode: Développement")
        print("📊 Base de données: SQLite (supermarche.db)")
        print("="*50 + "\n")
        
        # Importer et lancer l'application
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"✗ Erreur d'importation: {e}")
        print("Assurez-vous que toutes les dépendances sont installées.")
        return False
    except Exception as e:
        print(f"✗ Erreur lors du lancement: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Démarrage de GbGescom - Gestion de Supermarché")
    print("-" * 50)
    
    # Vérifier si les dépendances sont installées
    try:
        import flask
        import flask_sqlalchemy
        print("✓ Dépendances déjà installées")
    except ImportError:
        print("⚠️  Installation des dépendances requise...")
        if not install_requirements():
            sys.exit(1)
    
    # Lancer l'application
    run_app()
