#!/usr/bin/env python
#-*- coding: utf_8 -*-

import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT=6262
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print ("Connection adresse:",addr)

while 1:

	data = conn.recv(BUFFER_SIZE)
	data=data.decode()

	ls=os.popen("ls image/")
	ls=ls.read()
	print(ls)
	ls=ls.encode()
	print(ls)

	"""if data == "importer":
		#On récupère les 8 premier octets
		tailleImage = conn.recv(8)
		#On convertit la taille de l'image en entier (en octets)
		tailleImage = int(tailleImage.decode())
		#Contenu téléchargé en octets
		contenuTelecharge = 0
		#Le fichier qui va contenir l'image
		fichierImage = open("imageImporter/RedPanda.jpg","wb")
		 
		#On a la taille de l'image, jusqu'à ce qu'on ait tout téléchargé
		while contenuTelecharge < tailleImage:
		    #On lit les 1024 octets suivant
		    contenuRecu = conn.recv(1024)
		    #On enregistre dans le fichier
		    fichierImage.write(contenuRecu)
		    #On ajoute la taille du contenu reçu au contenu téléchargé
		    contenuTelecharge += len(contenuRecu)
		    print(">", end='')
	 
		fichierImage.close()
		print("Importation terminée")"""

	if data == "t":

		conn.send(ls)
		choix=conn.recv(BUFFER_SIZE);
		choix=choix.decode()
		print("Choix= ",choix)
		print("Download...")
		#Chemin vers l'image
		cheminImage = "image/"+choix+".jpg"

		fichierImage = open(cheminImage, "rb")
		 
		#On récupère la taille du fichier image en octets que l'on convertit en chaine de caractères
		tailleImage = str(os.path.getsize(cheminImage))
		#On rajoute des 0 devant la taille jusqu'à que la chaine fasse 8 caractères
		for i in range(8-len(tailleImage)):
		    tailleImage = "0"+ tailleImage
		 
		#On a la taille de l'image, on l'envoie au client
		conn.send(tailleImage.encode())
		 
		#On envoit le contenu du fichier
		conn.send(fichierImage.read())

		print("Telechargement terminee")

	elif data=="v":
		print("Je vais visionner")

		conn.send(ls)
		choix=conn.recv(BUFFER_SIZE);
		choix=choix.decode()
		print("Choix= ",choix)

		cheminImage = "image/"+choix+".jpg"
		conn.send(os.popen("eog "+cheminImage))

	else:
		print ("received data:", data)
		



