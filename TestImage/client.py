#!/usr/bin/env python

import socket
import os

localhost = '127.0.0.1'
port = 6262
BUFFER_SIZE=100

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port
s.connect((localhost,port))

# Protocol exchange - sends and receives
print("----------------------------------------------------------------")
print ("\n\t<<<<<<<<<<<Bienvenu sur le serveur de test>>>>>>>>>>>>")

msg_envoye = b""

while msg_envoye != ("EXIT"):
	print ("Que voulez vous faire?\n")
	msg_envoye=input(">> ")
	print(msg_envoye)


	if msg_envoye =="importer":
		
		msg_envoye=msg_envoye.encode()
		s.send(msg_envoye)

		lsretour=s.recv(BUFFER_SIZE)

		print("Vous pouvez importer les images suivante:\n",lsretour)
		
		#Chemin vers l'image
		cheminImage = "RedPanda.jpg"
		fichierImage = open(cheminImage, "rb")
		 
		#On récupère la taille du fichier image en octets que l'on convertit en chaine de caractères
		tailleImage = str(os.path.getsize(cheminImage))
		#On rajoute des 0 devant la taille jusqu'à que la chaine fasse 8 caractères
		for i in range(8-len(tailleImage)):
		    tailleImage = "0"+ tailleImage
		 
		#On a la taille de l'image, on l'envoie au client
		s.send(tailleImage.encode())
		 
		#On envoit le contenu du fichier
		s.send(fichierImage.read())

		print("Importation terminée")

	elif msg_envoye == "telecharger":

		print(msg_envoye,"2")

		msg_envoye=msg_envoye.encode()
		s.send(msg_envoye)

		print("Download...")
		#On récupère les 8 premier octets
		tailleImage = s.recv(8)
		#On convertit la taille de l'image en entier (en octets)
		tailleImage = int(tailleImage.decode())
		#Contenu téléchargé en octets
		contenuTelecharge = 0
		#Le fichier qui va contenir l'image
		fichierImage = open("imageTelecharger/RedPanda.jpg","wb")
		 
		#On a la taille de l'image, jusqu'à ce qu'on ait tout téléchargé
		while contenuTelecharge < tailleImage:
		    #On lit les 1024 octets suivant
		    contenuRecu = s.recv(1024)
		    #On enregistre dans le fichier
		    fichierImage.write(contenuRecu)
		    #On ajoute la taille du contenu reçu au contenu téléchargé
		    contenuTelecharge += len(contenuRecu)
		    print(">",)
	 
		fichierImage.close()

		print("Telechargement terminée")

	else:
		print(msg_envoye,"3")
		msg_envoye=msg_envoye.encode()
		s.send(msg_envoye)

print ("\n\t<<<<<<<<<<Deconnexion du serveur de test>>>>>>>>>>>>\n")
print("----------------------------------------------------------------")