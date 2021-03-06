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

#[[nom1,mdp1],[nom2,mdp2]....]

def lecture_fichier(fichier) : #[[nom1,mdp1],[nom2,mdp2]....]
	f = open(fichier,'r')
	fo = f.read(2048)
	l=fo.splitlines()
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	f.close()
	return l

def verification_nom_utilistaeur(nom, fichier):
	liste = lecture_fichier(fichier)
	print(liste)
	for e in liste :
		print(e[0])
		if e[0] == nom :
			return 0
	return 1

## Fonction pour blacklister queqlu'un #######################
def failPassword(nom):
	f = open("blacklist.txt",'a')
	f.write(nom+";")



## Fonction pour verifier si une personne n'est pas dans la blackliste #####
def verifBlacklist(nom):

	f=open("blacklist.txt",'r')
	lecture=f.read(1024).rstrip()
	bl=lecture.split(";")
	
	if nom in bl:
		return 0
	else:
		return 1


##########################################################################


def SIGNUP():

	user=s.recv(30).decode()
	print("l'utilisateur est : ", user)
	if user == "administrateur" :
		user1="admin"
		s.send(user1.encode())

		tout=False
		mdp_admin1 =''
		while mdp_admin1 != 'correct' :
			mdp_admin=s.recv(32).decode()
			print(mdp_admin)

			if mdp_admin=='root':
				print("mdp correct !")
				mdp_admin1='correct'
				s.send(mdp_admin1.encode())
				tout =True

			elif mdp_admin=='annuler':
				mdp_admin1='annuler'
				s.send(mdp_admin1.encode())
				print("Le client veut annuler")
				break

			elif mdp_admin != 'annuler' or mdp_admin != 'root':
				print(mdp_admin)
				mdp_admin1='non'
				s.send(mdp_admin1.encode())
				print("le client a fait n'importe quoi")


		while tout :

				choix=s.recv(32).decode()
				print(choix)

				if choix=='fin' :
					tout=False
					break

				elif choix == "signup" :
					choix1 = "signup1"
					print("go signup")
					s.send(choix1.encode())

					service = s.recv(32).decode()
					print("Le service choisi est : ", service)

					if service == 'Medecin' :
						service1="okMed"
						print("go signup Medecin")
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
							f.write(hash_mdp+"\n")
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
								if verification_nom_utilistaeur(nom, 'passwordInf.txt') == 1:
									f = open('passwordInf.txt','a')
									f.write(nom+":")
									oknom="okNom"
									invalide = False
								else :
									oknom="nop"
									s.send(oknom.encode())

							s.send(oknom.encode())

							hash_mdp = s.recv(64).decode()
							f = open('passwordInf.txt','a')
							f.write(hash_mdp+"\n")
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
								if verification_nom_utilistaeur(nom, 'passwordInt.txt') == 1:
									f = open('passwordInt.txt','a')
									f.write(nom+":")
									oknom="okNom"
									invalide = False
								else :
									oknom="nop"
									s.send(oknom.encode())

							s.send(oknom.encode())

							hash_mdp = s.recv(64).decode()
							f = open('passwordInt.txt','a')
							f.write(hash_mdp+"\n")
							print("Fin enregistrement")

						
						else:
							clé="Pas la bonne clé pour le service Interne."
							print ("Inscription impossible")

					else :
						service_erreur="Ce service n'existe pas"
						s.send(service_erreur.encode())
						print ("Ce service n'existe pas.")

				elif choix=="blacklist" :
					choix1 = "blacklist"
					print("go blacklist")
					s.send(choix1.encode())
					black='go'
					nom_blackliste=''

					while black=='go' and nom_blackliste !='retour' :

						nom_blackliste = s.recv(32).decode()
						print("L'utilisateur blacklisté est : ", nom_blackliste)
						
						if nom_blackliste == 'fin' :
								a='stop'
								print(a)
								s.send(a.encode())
								nom_blackliste='retour'
								black='stop'

						else :
							verifBlacklist(nom_blackliste)
							if verifBlacklist(nom_blackliste) == 0 :
								print("Utilisateur dans blacklist")
								a='oui'
								s.send(a.encode())

								delet=s.recv(64).decode()
								delet=delet.split(' ')
								print(delet[0])
								print(delet[1])

								if delet[0] == 'delet' and len(delet)==2 and verifBlacklist(delet[1])==0 and delet[0]!='fin' :
									a='okDelet'
									s.send(a.encode())
									print("Vous allez effacer l'utilisateur "+delet[1]+" de la blacklist")
									b=s.recv(16).decode()
									print(b)

									f=open("blacklist.txt",'r')
									lecture=f.read(1024)
									lecture=lecture.rstrip()
									bl=lecture.split(";")
									bl.pop()
									print(bl)
									bl.remove(delet[1])
									print(bl)
									f.close()

									f=open("blacklist.txt",'w')
									for e in bl:
										f.write(e+";")
									
									a='Utilistateur enlevé de la Blacklist'
									s.send(a.encode())
									f.close()
									

								elif delet[0] == 'delet' and len(delet)==2 and verifBlacklist(delet[1])==1 :
									a="not In Blacklist"
									s.send(a.encode())
								
								else :
									a='Mauvaise Commande'
									s.send(a)

							elif verifBlacklist(nom_blackliste) == 1 :
								print("L'utilisateur n'est pas dans la Blacklist")
								a='non'
								s.send(a.encode())

							else :
								print("Erreur !!")
								a='erreur'
								s.send(a.encode())
					print("fin boucle while blacklist")




				else :
					print("On est dans l'avant dernier else")
					choix1="Ce choix n'est pas possible"
					s.send(choix1.encode())
					print ("Ce n'est pas un bon choix")

	else :
		user1="Commande inconnue"
		s.send(user1.encode())


SIGNUP()
print("Fin serveur")
print("")
print("")


"""print(lecture_fichier('passwordMed.txt'))
print("")
print("")"""

"""a=verification_nom_utilistaeur('Alo', 'passwordMed.txt')
print(a)
print("")
print("")

print("Paul")
a=verification_nom_utilistaeur('Paul', 'passwordMed.txt')
print(a)
print("")
print("")


print("Aller")
a=verification_nom_utilistaeur('Aller', 'passwordMed.txt')
print(a)"""