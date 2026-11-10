from flask import Flask, request
import os
from datetime import datetime

# Dossier dans lequel les images seront enregistrées
UPLOAD_FOLDER = r"images_recues"
# Crée le dossier s'il n'existe pas encore
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialise l'application Flask
app = Flask(__name__)

# Route pour recevoir les fichiers envoyés en HTTP POST
@app.route('/upload', methods=['POST'])
def upload_image():
    # Vérifie que le champ 'image' existe dans les fichiers envoyés
    if 'image' not in request.files:
        return "Aucune image reçue", 400  # Répond avec une erreur HTTP 400

    # Récupère le fichier envoyé
    img = request.files['image']

    # Crée un nom de fichier unique basé sur la date et l’heure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(UPLOAD_FOLDER, f"{timestamp}.jpg")

    # Enregistre le fichier dans le dossier spécifié
    img.save(filepath)

    # Affiche une confirmation dans la console
    print(f"Image reçue : {filepath}")

    # Répond au client que l’image a été bien reçue
    return "Image OK", 200

# Point d’entrée du script
if __name__ == '__main__':
    # Démarre le serveur Flask
    # host='0.0.0.0' permet d'accepter les connexions depuis d'autres machines du réseau local
    # port=5000 : port utilisé pour recevoir les images (doit être le même côté Raspberry Pi)
    app.run(host='0.0.0.0', port=5000)