#Caméra de surveillance RaspberryPi
import time
import requests
from picamera2 import Picamera2
from datetime import datetime

SERVER_URL = "http://192.168.0.22:5000/upload"  # Exemple d'IP locale

# Initialisation caméra
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()
time.sleep(2)  # Laisse le temps à la caméra de s'ajuster

try:
    while True:
        # Nom de fichier basé sur l'heure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.jpg"

        # Capture
        picam2.capture_file(filename)
        print(f"[{timestamp}] Image capturée.")

        # Envoi
        with open(filename, 'rb') as img:
            files = {'image': (filename, img, 'image/jpeg')}
            try:
                response = requests.post(SERVER_URL, files=files)
                if response.ok:
                    print(f"Image envoyée avec succès.")
                else:
                    print(f"Échec d'envoi: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Erreur réseau: {e}")

        # Pause 5 secondes
        time.sleep(5)

except KeyboardInterrupt:
    picam2.stop()
    print("\nArrêt du programme.")

