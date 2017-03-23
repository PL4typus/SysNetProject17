#!/usr/bin/python3.4
#Client authentification
#coding: utf8
import os
from getpass import getpass
import hashlib


import socket
TCP_IP = '127.0.0.1'
TCP_PORT=6265
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

s, addr = s.accept()

print ("Connection adresse:",addr)

DROIT=""


mdpMed="azerty"
Med="médecin"

cleMed="bouteille"
cleInf="livre"
cleInt="portable"

#################### Fonction pour la liste des utilisateur avec leur mots de pass ########

def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(2048)
	fo=fo.rstrip()
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	return l

def verification_nom_utilistaeur(nom, fichier):
	liste = lecture_fichier(fichier)
	for e in liste :
		if e[0] == nom :
			return 0
		else :
			return 1



##########################################################################


def SIGNUP():

	user=s.recv(30).decode()
	print("l'utilisateur est : ", user)
	if user == "administrateur" :
		user1="admin"
		s.send(user1.encode())

		tout =True

		while tout :

			choix=s.recv(32).decode()
			print(choix)

			if choix=='annuler' :
				break

			elif choix == "signup" :
				choix1 = "signup1"
				s.send(choix1.encode())

				service = s.recv(32).decode()
				print("service : ", service)

				if service == 'Medecin' :
					service1="okMed"
					s.send(service1.encode())

					saisie=s.recv(32).decode()
					if saisie == cleMed:
						clé="okCle"
						s.send(clé.encode())

						invalide=True
						while invalide :
							nom=s.recv(24).decode()
							if verification_nom_utilistaeur(nom, 'passwordMed.txt')== 1 :
								f = open('passwordMed.txt','a')
								f.write(nom+":")
								oknom="okNom"
								invalide = False
							else :
								oknom="nop"
								s.send(oknom.encode())


						s.send(oknom.encode())

						hash_mdp = s.recv(64).decode()
						f = open('passwordMed.txt','a')
						f.write(hash_mdp+";")
						tout=False
						print("Fin enregistrement")

					
					else:
						clé="Pas la bonne clé pour le service médecin"
						s.send(clé.encode())
						print ("Cle errone, inscription impossible")
				

				elif service == 'Infirmier' :
					service1="okInf"
					s.send(service1.encode())

					saisie=s.recv(32).decode()
					if saisie == cleInf:
						clé="okCle"
						s.send(clé.encode())

						invalide=True
						while invalide :
							nom=s.recv(24).decode()
							if verification_nom_utilistaeur(nom, 'passwordMed.txt') == 1:
								f = open('passwordMed.txt','a')
								f.write(nom+":")
								oknom="okNom"
								invalide = False
							else :
								oknom="nop"
								s.send(oknom.encode())

						s.send(oknom.encode())

						hash_mdp = s.recv(64).decode()
						f = open('passwordInf.txt','a')
						f.write(hash_mdp+";")
						tout=False
						print("Fin enregistrement")
					
					else:
						clé="Pas la bonne clé pour le service Infirmier"
						s.send(clé.encode())					
						print ("Inscription impossible")

				elif service == 'Interne' :
					service1="okInt"
					s.send(service1.encode())

					saisie=s.recv(32).decode()
					if saisie == cleInt:
						clé="okCle"
						s.send(clé.encode())

						invalide=True
						while invalide :
							nom=s.recv(24).decode()
							if verification_nom_utilistaeur(nom, 'passwordMed.txt') == 1:
								f = open('passwordMed.txt','a')
								f.write(nom+":")
								oknom="okNom"
								invalide = False
							else :
								oknom="nop"
								s.send(oknom.encode())

						s.send(oknom.encode())

						hash_mdp = s.recv(64).decode()
						f = open('passwordInt.txt','a')
						f.write(hash_mdp+";")
						tout=False
						print("Fin enregistrement")

					
					else:
						clé="Pas la bonne clé pour le service Interne."
						print ("Inscription impossible")

				else :
					service_erreur="Ce service n'existe pas"
					s.send(service_erreur.encode())
					print ("Ce service n'existe pas.")

			else :
				choix1="Ce choix n'est pas possible"
				s.send(choix1.encode())
				print ("Ce n'est pas un bon choix")

	else :
		user1="Commande inconnue"
		s.send(user1.encode())


SIGNUP()
print("Fin serveur")



