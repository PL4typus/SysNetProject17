#!/usr/bin/python
#Client authentification
import os
from getpass import getpass

mdpMed="azerty"
Med="medecin"

cleMed="bouteille"


def SIGNUP():

	user=input("Utilisateur")
	saisie=input("Cle Medecin:")
	if saisie == cleMed:
		mdp = getpass("Mot de passe:")
		f = open('passwordMed.txt','a')
		f.write(user+":"+mdp+"\n")
		
		
	else:
		print ("Cle errone, inscription impossible")
	


def LOGIN():
	session = True
	verrouille = True
	time=4
	
	service=input("Service (Medecin, Infirmier, Interne):")
	
	while session:
	
		user= input("Utilisateur:")

		if service == "Medecin":
			f=open('passwordMed.txt','a')
		elif service == "Infirmier"
			f=open('passwordInf.txt','a')
		elif service == "Interne"
			f=open('passwordInt.txt','a')

		
			session = False
		else:

			print("Utilisateur inconnue")
		

	while verrouille:
		time-=1
		print("Reste",time,"essai")
		
		if time ==0:
			print("Plus d'essai disponible")
			break
		else:
			saisie = getpass("Mot de passe:")
			if saisie == mdpMed:
				verrouille=False
				print("Session ouverte")
			else:
				print("Mot de passe incorrect")
	
	

SIGNUP()
LOGIN()
