#!/usr/bin/python3.4
#client authentification
import os
from getpass import getpass
#coding: utf8

import socket

localhost = '127.0.0.1'
port = 6262
BUFFER_SIZE=100

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port
s.connect((localhost,port))

saisie=""

print("=====================================================================================")
print("<<<<<<<<<<<<<<<<<<<<<<<<<Bienvenu sur le serveur de l'hopital>>>>>>>>>>>>>>>>>>>>>>>>")
print("Voulez vous:\n\t¤Vous inscrire (signup)?\n\t¤Vous connecter(login)?\n\t¤Quitter(exit)?")

while saisie!= "exit":
	service=True
	session=True
	tout=True
	verrouille=True

	saisie=input(">> ")
	
	#if saisie == "signup":
	if saisie == "login":
		
		while tout:
			user=''
			while service:
				saisie=input("Quel service? (Medecin, Infirmier, Interne)")
				saisie=saisie.encode()
				s.send(saisie)

				data=s.recv(10)
				data=data.decode()
				data=int(data)
		
				if data == 1:
					print("Vous etes un Médecin")
					service=False
				elif data == 2:
					print("Vous etes un Infirmier")
					service=False
				elif data == 3:
					print("Vous etes un Interne")
					service=False
				else:
					print(data)
					print("Service inconnu")

			while session and user != 'retour':

				user=input("Utilisateur: ")
				user=user.encode()
				s.send(user)
		
				data2=s.recv(30)
				data2=data2.decode()	
				print("on a reçu :", data2)
				if data2 == "1":
					session=False
					tout = False
					print("Utilisateur reconnu")
				elif data2 == "return":
					service=True
					break
				else:
					print ("Utilisateur inconnu")

			while verrouille and tout == False :
				s.send(b"OK")
				Timeline=s.recv(30)
				Timeline=Timeline.decode()
				print(Timeline)
				
				if  Timeline == "Reste 0 essai":
					print("Plus d'essai disponible")
					break
				else:
					saisie=getpass("Mot de passe: ")
					saisie=saisie.encode()
					s.send(saisie)
				
				verif=s.recv(10)
				verif=verif.decode()
				if verif == "1":
					print("Session ouverte")
					verrouille = False
				else:
					print("Mot de passe incorrect")
			
	
print("<<<<<<<<<<<<<<<<<<<<<<<<<Déconnexion du serveur de l'hopital>>>>>>>>>>>>>>>>>>>>>>>>")
print("=====================================================================================")

s.close()
