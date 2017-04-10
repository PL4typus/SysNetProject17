#!/usr/bin/python3.4
#client authentification
#coding: utf8
import os
from getpass import getpass
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


print("===========================================================")
print("<<<<<<<<<<<<< Serveur pour administratuer >>>>>>>>>>>>>>>>>")
print("===========================================================")

saisie=""
user=input("Utilisateur : ")
s.send(user.encode())
user1=s.recv(16).decode()
print(user1)

if user1 == "admin" :

	mdp_admin1=''
	while mdp_admin1 != 'correct' :
		mdp_admin=getpass("mot de passe administrateur : ")
		s.send(mdp_admin.encode())
		mdp_admin1=s.recv(16).decode()
		print("reponse : " ,mdp_admin1)

		if mdp_admin1=='annuler' :
			print("Vous voulez annuler")
			mdp_admin1='correct'
			tout=False
			break

		elif mdp_admin1=='correct' :
			print("Code bon")
			tout=True

		else :
			print("Veuillez réessayez")

	while tout :

			print("Vous êtes connecté en tant qu'administrateur.")
			print("Voulez vous:\n\t¤Enregistrer un nouvel utilisateur (signup) ?\n\t¤Modifier la blacklist (blacklist) ?\n\t¤Quitter (fin)?")
			print(" ")
			choix = input(">> ") #signup ou blacklist
			s.send(choix.encode())

			if choix=="fin" :
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
									else :
										print("Ce nom d'utilisateur existe déjà...")

								
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
								print(clé)

								invalide=True
								while invalide :
									nom=input("Nom de l'utilisiteur : ")
									s.send(nom.encode())
									oknom=s.recv(16).decode()
									if oknom == 'okNom' :
										invalide = False
									else :
										print("Ce nom d'utilisateur existe déjà...")

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
									else :
										print("Ce nom d'utilisateur existe déjà...")

								mdp = getpass("Mot de passe :")
								hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
								s.send(hash_mdp.encode())
								
							else:
								print(clé)
								print ("Cle errone, inscription impossible")

					else :
						service_erreur=s.recv(64).decode()
						print(service_erreur)


				elif choix1=='blacklist' :
					black='go'
					while black=='go' :
						nom_blackliste=input("Utilisateur blacklisté : ")
						s.send(nom_blackliste.encode())
						a=s.recv(16).decode()

						if a=='stop':
								print("Vous voulez finir les modifs blacklist")
								black='stop'

						elif a == 'oui' :
							print("Cet utilisateur est dans la blackliste ")
							print("Pour retirer cet utilisateur de la blacklist taper la commande <delet nom_utilisateur>")
							delet=input(">> ")
							s.send(delet.encode())

							ok=s.recv(64).decode()
							if ok=='okDelet':
								print("Vous allez effacer l'utilisateur "+delet[1]+" de la blacklist")
								b='dansDelet'
								s.send(a.encode())
								a=s.recv(64).decode()
								print(a)
								print("L'utilisateur peut de nouveau se connecter")

							elif ok=='stop':
								print("Vous voulez finir les modifs blacklist")
								black='stop'

							else :
								print(ok)

						elif a == 'non' :
							print("Cet utilisateur n'est pas dans la Blacklist")

						else : 
							print("Erreur aucun truc bon....")




				else :
					print(choix1)

else :
	print("nop pas admin")

print("================================================================")
print("					Fin de connexion")
print("================================================================")