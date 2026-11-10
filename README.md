# Reconnaissance faciale et commande de porte (Raspberry Pi)

Module de reconnaissance faciale et de commande de porte d'un sas de
laboratoire sécurisé. Projet de groupe de fin de BTS Cybersécurité,
Informatique et réseaux, Électronique (Lycée Frédéric Ozanam, Lille, 2025).

Le projet complet, réalisé à 4, comprenait aussi un lecteur RFID, un capteur
de mouvement et une caméra de surveillance, réalisés par mes coéquipiers.
Ce dépôt contient uniquement ma partie.

## Ma contribution
- Mise en œuvre d'un système de reconnaissance faciale : constitution du
  jeu de données, encodage des visages, reconnaissance en temps réel
  sur Raspberry Pi, activation d'une sortie GPIO pour les personnes autorisées.
- Pilotage de la porte : verrouillage par servomoteur et ouverture par
  moteur pas à pas 28BYJ-48 (lgpio).
- Conception et réalisation complètes, en autonomie, de la carte d'interface
  (PCB) du Raspberry Pi avec EasyEDA, fabriquée par JLCPCB : attribution des
  GPIO aux modules (RFID, PIR, clavier matriciel, servomoteur, moteur pas à pas),
  routage, soudure et définition des broches allouées à chaque coéquipier.
  
## Technologies
Python, OpenCV, face_recognition (dlib), Picamera2, gpiozero, lgpio

## Fichiers
| Fichier | Rôle |
|---|---|
| image_capture.py | Prise de photos par personne |
| model_training.py | Calcul des encodages des visages |
| facial_recognition.py | Reconnaissance en temps réel |
| facial_recognition_hardware.py | Idem + sortie GPIO pour les noms autorisés |
| Porte.py | Servomoteur de verrouillage + moteur pas à pas |

## Sources
La partie reconnaissance faciale s'appuie sur mes recherches effectuées avec mon professeur Mr.Letienne Thiery.

## Limites
- Le jeu de données et les encodages ne sont pas publiés (données biométriques).
- Pas de détection de vivacité : une photo présentée à la caméra pourrait être acceptée.
- Les noms autorisés sont écrits en dur dans le script.
- Code testé sur le matériel du projet uniquement.
