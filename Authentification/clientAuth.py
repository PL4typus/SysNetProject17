#!/usr/bin/python
#Client authentification
import os
from getpass import getpass


mdpMed="azerty"
Med="medecin"

cleMed="bouteille"
cleInf="livre"
cleInt="portable"


def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(1024)
	fo=fo.rstrip()
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	return l

def SIGNUP():

	user=input("Utilisateur : ")

	service = input("Sous quel service voulez vous vous enregistrer (Medecin, Infirmier, Interne)? ")

	if service == 'Medecin' :

		saisie=input("Cle Medecin : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordMed.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")
	
	elif service == 'Infirmier' :
		saisie=input("Cle Infirmier : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordInf.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	elif service == 'Interne' :
		saisie=input("Cle Interne : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordInt.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	else :
		print ("Ce service n'existe pas.")



def LOGIN():
	tout = True
	session = True
	service = True
	verrouille = True
	time=4
	

	while tout :
		print("tout")
		user = ''
		while service:
			print ("service")
			service=input("Service (Medecin, Infirmier, Interne):")
			if service == "Medecin":
				l=lecture_fichier("passwordMed.txt")
				service = False
			elif service == "Infirmier":
				l=lecture_fichier("passwordInf.txt")
				service = False
			elif service == "Interne":
				l=lecture_fichier("passwordInt.txt")
				service = False
			else:
				print("Ce service n'existe pas")
			
		while session and user != 'retour':
			print("session")
			user= input("Utilisateur:")
			if user == 'retour' :
				service = True
				break
			else :
		
				for i in range(len(l)):
					for j in range(len(l[i])):
						if user == l[i][0]:
							print ("Utilisateur reconnu")
							session = False
							tout = False
				if session == True:	
					print("Utilisateur inconnu")		
	
		while verrouille and tout == False :
			print("verou")
			time-=1
			print("Reste",time,"essai")
			
			if time ==0:
				print("Plus d'essai disponible")
				break
			else:
				saisie = getpass("Mot de passe:")
			
			for i in range(len(l)):
				for j in range(len(l[i])):
					if user == l[i][0]:
						if saisie== l[i][1]:
							verrouille=False
							print("Session ouverte")
						else:
							print("Mot de passe incorrect")
						
	
	

#SIGNUP()
LOGIN()
