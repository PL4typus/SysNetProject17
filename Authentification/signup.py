#!/usr/bin/python
#Client authentification
#coding: utf8

import os
from getpass import getpass
import hashlib



mdpMed="azerty"
Med="médecin"

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
			hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
			f = open('passwordMed.txt','a')
			f.write(user+":"+hash_mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")
	
	elif service == 'Infirmier' :
		saisie=input("Cle Infirmier : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
			f = open('passwordInf.txt','a')
			f.write(user+":"+hash_mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	elif service == 'Interne' :
		saisie=input("Cle Interne : ")
		if saisie == cleMed:
			mdp = getpass("Mot de passe :")
			hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
			f = open('passwordInt.txt','a')
			f.write(user+":"+hash_mdp+";")
		
		else:
			print ("Cle errone, inscription impossible")

	else :
		print ("Ce service n'existe pas.")


SIGNUP()




