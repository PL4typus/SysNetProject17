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
	#fo = fo.rstrip()			#enleve les \n
	l = fo.split(';') 
	print l
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
