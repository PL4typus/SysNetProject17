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
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	return l

def SIGNUP():

	user=raw_input("Utilisateur : ")

	service = raw_input("Sous quel service voulez vous vous enregistrer ? ")

	if service == 'medecin' :

		saisie=raw_input("Cle Medecin : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordMed.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")
	
	elif service == 'infirmier' :
		saisie=raw_input("Cle Infirmier : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordInf.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	elif service == 'interne' :
		saisie=raw_input("Cle Interne : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			f = open('passwordInt.txt','a')
			f.write(user+":"+mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	else :
		print ("Ce service n'existe pas.")



def LOGIN():
	session = True
	service = True
	verrouille = True
	time=4
	
	
	
	while service:
	
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
			
	while session:
		
		user= input("Utilisateur:")
		for i in range(len(l)):
			for j in range(len(l[i])):
				if user == l[i][0]:
					print ("Utilisateur reconnu")
					session = False
		if session == True:	
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
	
	

#SIGNUP()
LOGIN()
