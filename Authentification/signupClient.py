#!/usr/bin/python3.4
#client authentification
import os
from getpass import getpass
#coding: utf8
import hashlib

import socket

localhost = '127.0.0.1'
port = 6265
BUFFER_SIZE=100

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port
s.connect((localhost,port))

saisie=""

print("===========================================================")
print("<<<<<<<<<<<<< Serveur pour administratuer >>>>>>>>>>>>>>>>>")
print("===========================================================")


user=input("Utilisateur : ")
s.send(user.encode())
user1=s.recv(16).decode()
print(user1)

if user1 == "admin" :

	mdp_admin1=''
	while mdp_admin1 != 'correct' :
		mdp_admin=input("mot de passe administrateur : ")
		s.send(mdp_admin.encode())
		mdp_admin1=s.recv(16).decode()
		print(mdp_admin1)

		if mdp_admin1=="annuler" :
				mdp_admin1='correct'
				tout=False

		elif mdp_admin1=='correct' :
			tout=True

		else :
			continue

	while tout :

			print("Vous êtes connecté en tant qu'administrateur.")
			print("Que voulez vous faire ?")
			print("	- enregistrer une nouvelle personne (signup)")
			print(" 	- modifier la blacklist (blacklist)")
			print(" ")
			choix = input(">> ") #signup ou blacklist
			s.send(choix.encode())

			if choix=="annuler" :
				break

			else :
				choix1 = s.recv(32).decode()
				if choix1 == "signup1" : #le serveur montre qu'il suit vers signup
					print(choix1)
					service = input("Sous quel service voulez vous enregistrer le nouvel utilisateur ? (Medecin, Infirmier, Interne)? ")
					s.send(service.encode())

					if service == 'Medecin' :
						service1=s.recv(32).decode() 

						if service1 == "okMed":
							saisie=input("Cle Medecin : ")
							s.send(saisie.encode())

							clé=s.recv(64).decode()	#vérification que la clé correspond a la clé medecin
							if clé == "okCle":
								
								invalide=True
								while invalide :
									nom=input("Nom de l'utilisiteur : ")
									s.send(nom.encode())
									oknom=s.recv(16).decode()
									if oknom == 'okNom' :
										invalide = False

								
								mdp = getpass("Mot de passe :")
								hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
								s.send(hash_mdp.encode())
						
							else:
								print(clé)
								print ("Inscription impossible")
						

					elif service == 'Infirmier' :
						service1=s.recv(32).decode() 

						if service1 == "okInf":
							saisie=input("Cle Infirmier : ")
							s.send(saisie.encode())

							clé=s.recv(64).decode()
							if clé == "okCle" :

								invalide=True
								while invalide :
									nom=input("Nom de l'utilisiteur : ")
									s.send(nom.encode())
									oknom=s.recv(16).decode()
									if oknom == 'okNom' :
										invalide = False

								mdp = getpass("Mot de passe :")
								hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
								s.send(hash_mdp.encode())
								
							else:
								print(clé)
								print ("Cle errone, inscription impossible")

					elif service == 'Interne' :
						service1=s.recv(32).decode()


						if service1 == "okInt" :
							saisie=input("Cle Interne : ")
							s.send(saisie.encode())

							clé=s.recv(64).decode()
							if clé == "okCle" :
								
								invalide=True
								while invalide :
									nom=input("Nom de l'utilisiteur : ")
									s.send(nom.encode())
									oknom=s.recv(32).decode()
									if oknom == 'okNom' :
										invalide = False

								mdp = getpass("Mot de passe :")
								hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
								s.send(hash_mdp.encode())
								
							else:
								print(clé)
								print ("Cle errone, inscription impossible")

					else :
						service_erreur=s.recv(64).decode()
						print(service_erreur)

				else :
					print(choix1)

else :
	print("nop pas admin")
