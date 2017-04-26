#!/usr/bin/env python3.4
#coding: utf8


import socket,sys,os
#from gestionErr.py import *
from getpass import getpass
import hashlib

if sys.argv[1]:
    TCP_IP =sys.argv[1]
else: 
    TCP_IP = '127.0.0.1'

if sys.argv[2]:
    TCP_PORT = int(sys.argv[2])
else:
    TCP_PORT = 6224

BUFFER_SIZE = 1024
historique = " "


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((TCP_IP,TCP_PORT))
decision=""

def PlsrLignes ():
	a = " "
	b = ""
	while str(b) != "§":
		b = input("> ")
		if str(b) != "§" :
			a = a + "\n"+str(b)
	return a

DROIT = ''

while decision!= "exit":
	print("=====================================================================================")
	print("<<<<<<<<<<<<<<<<<<<<<<<<<Bienvenu sur le serveur de l'hopital>>>>>>>>>>>>>>>>>>>>>>>>")
	print("Voulez vous:\n\t¤ Vous connectez en tant qu'Administrateur (admin) ?\n\t¤ Vous connecter(login)?\n\t¤ Quitter(exit)?")


	service=True
	session=True
	tout=True
	verrouille=True

	decision=input(">> ")
	s.send(decision.encode())



	if decision == "login":

		while tout:
			user=''
			while service:
				saisie=input("Quel service ? (Medecin, Infirmier, Interne) \n >> ")
				saisie=saisie.encode()
				s.send(saisie)

				data=s.recv(10)
				data=data.decode()
				print (data)
				if data == "1":
					print("Vous etes un Médecin \n")
					DROIT='M'
					service=False
				elif data == "2":
					print("Vous etes un Infirmier \n")
					DROIT=''
					service=False
				elif data == "3":
					print("Vous etes un Interne \n")
					DROIT=''
					service=False
				else:

					print("Service inconnu")

			while session and user != 'retour':

				user=input("Utilisateur : ")
				user=user.encode()
				s.send(user)

				data2=s.recv(30)
				data2=data2.decode()

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
				s.send(b"OKmdp")
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
				print (verif)
				if verif == "1":
					print("Session ouverte \n")
					verrouille = False
				else:
					print("Mot de passe incorrect")


		while 1 :
			cmd=input("Saisir la commande ")
			l = cmd.split(" ")
			i = 0
			maCom = " "
			while i<len(l) :
				maCom = maCom+l[i]
				i = i+1
			historique = historique +"\n"+ maCom
			if l[0]== "edit" :
				if len(l) < 2 :
					print ("Erreur : argument manquant\nuse : edit nomfichier")
				else :
					s.send(cmd.encode())
					print ("Voici l'affichage du fichier que vous voulez editer :\n")
					rep=s.recv(BUFFER_SIZE)
					rep = rep.decode()
					if DROIT == 'M':
						rep = rep.decode()
						if rep != "1" :
							print (rep)
							num = "8"
							while num < "0" or num > "7" :
								num = input("\n\nATTENTION : Quand vous editez un champs vous réecrivez par dessus !\n\nQuelle champs voulez vous editer ? (mettre le n°) : ")
							s.send(num.encode())
							if int(num) >= 3 and int(num) <= 6 :
								print("Ecrivez ce que vous voulez ecrire dans ce champs : ")
								edit = PlsrLignes()
							else :
								edit=input("Ecrivez ce que vous voulez ecrire dans ce champs : ")
							s.send(edit.encode())
							print ("Voici l'affichage du fichier après edition :\n")
							rep=s.recv(BUFFER_SIZE)
							print (rep.decode())
						else :
							print (rep)
							print ("Erreur le fichier ", l[1], " n'existe pas\n")
					else:
						print (rep)

			elif l[0]=="creer" :
				if len(l) < 2 :
					print ("Erreur : argument manquant\nuse : creer nomfichier")
				else :
					s.send(cmd.encode())
					rep = s.recv(BUFFER_SIZE)
					rep=rep.decode()
					if DROIT == 'M':
						if rep == "0":
							ecrase = input("Un fichier du même nom existe déjà voulez vous l'écraser ? (non:0/oui:1)\n")
						if (rep != "0") or ecrase==1 :
							print ("\nEntrez les informations concernant le patient\n")
							nom=input("Saisir le nom : ")
							nom=str(nom)+" "
							s.send(nom.encode())
							prenom=input("Saisir le prenom : ")
							prenom=str(prenom)+" "
							s.send(prenom.encode())
							age=input("Saisir l'age: ")
							age=str(age)+" "
							s.send(age.encode())
							print("Saisir ses allergies (§ pour terminer): ")
							aller=PlsrLignes()
							s.send(aller.encode())
							print("Saisir ses symptomes (§ pour terminer): ")
							symp= PlsrLignes()
							s.send(symp.encode())
							print("Saisie du diagnostique (§ pour terminer): ")
							diag=PlsrLignes()
							s.send(diag.encode())

							print("Saisie des commentaires (§ pour terminer): ")
							com = PlsrLignes()
							s.send(com.encode())

							hop=input("Saisie de la date d'entrée à l'hôpital: ")
							hop=str(hop)+" "
							s.send(hop.encode())
						else :
							err = "ERREUR"
							s.send(err.encode())
						print("Fin de la saisie")
				
					else:
						print(rep)
			elif l[0]=="signer":
				s.send(cmd.encode())
				erreur="ERR"
				repDoc=s.recv(BUFFER_SIZE)
				repDoc=repDoc.decode()
				print(user)
				s.send(user)
				print("Vous pouvez signer les documents suivants:\n")
				print (repDoc)
				doc=input("Quel document voulez vous signer?\n>>")
				if doc not in repDoc:
					print("Le document n'existe pas")
					s.send(erreur.encode())
				else:
					s.send(doc.encode())

			elif l[0]=="help":
				print("Voici les commandes :\n")
				print("ls :		affiche tous les fichiers du repertoire où vous vous trouvez)")
				print("cat :		affiche le fichier passé en paramètre (use : cat nomFichier)")
				print("rm :		efface le fichier passé en paramètre (use : rm nomFichier)")
				print("mkdir :		créé un dossier (use : mkdir nomdossier)")
				print("cd :		déplacement dans le dossier, mettre .. pour revenir au dossier parent (use : cd nomdossier ou cd ..)")
				print("cp:		copie un fichier dans un dossier (use : cp nomfichier nomdossier)")
				print("creer :		créé un fichier (use : creer nomfichier)")
				print("edit :		édite un fichier (use : edit nomfichier)")
				print("signer :	signe un fichier ")
				print("clear :		efface votre page ")
				print("historique :		affiche l'historique de vos commandes ")
				print("whereis :		trouve un fichier (use : whereis nomfichier) ")
				print("fin:		quitte et revient aux login")
			elif l[0]=="clear":
				print ("\033[H\033[2J")

			elif l[0]=="historique":
				print (historique)


			elif l[0] == "fin" :
				historique = " "
				fin='1'
				s.send(fin.encode())
				break
			else :
				s.send(cmd.encode())
				rep=s.recv(BUFFER_SIZE)
				print (rep.decode())


	elif decision=="admin":
		saisie=""
		user=input("Utilisateur : ")
		s.send(user.encode())
		user1=s.recv(32).decode()

		if user1 == "admin" :
			mdp_admin1=''
			while mdp_admin1 != 'correct' :
				mdp_admin=getpass("Entrez votre mot de passe administrateur : ")
				mdp_admin = hashlib.sha256(mdp_admin.encode()).hexdigest()
				s.send(mdp_admin.encode())
				mdp_admin1=s.recv(16).decode()

				if mdp_admin1=='Faux' :
					print(mdp_admin1+", mauvais mot de passe. Veuillez réessayez.")				

				elif mdp_admin1=='correct' :
					print("Code bon")
					print("Vous êtes connecté en tant qu'administrateur.")
					tout=True

				else :
					print("Veuillez réessayez")

			while tout :

				print("Voulez vous :\n\t¤ Enregistrer un nouvel utilisateur (signup) ?\n\t¤ Modifier la blacklist (blacklist) ?\n\t¤ Quitter (fin)?")
				print(" ")
				choix = input(">> ") #signup ou blacklist
				s.send(choix.encode())

				if choix=="fin" :
					choix1 = s.recv(32).decode()
					fin = '1' 
					s.send(fin.encode())
					break
					

				else :
					choix1 = s.recv(32).decode()
					if choix1 == "signup1" : #le serveur montre qu'il suit vers signup
						service = input("Sous quel service voulez vous enregistrer le nouvel utilisateur ? (Medecin, Infirmier, Interne)? \n >> ")
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
									print ("Clé erronée, inscription impossible \n")
							

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
									print ("Clé erronée, inscription impossible \n")

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
									print ("Clé erronée, inscription impossible \n")

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
									print("Vous avez fini les modifications sur la blacklist")
									black='stop'

							elif a == 'oui' :
								print("Cet utilisateur est dans la blacklist")
								print("Pour retirer cet utilisateur de la blacklist taper la commande \n \t\t<delet nom_utilisateur>")
								delet=input(">> ")
								s.send(delet.encode())

								ok=s.recv(64).decode()
								if ok=='okDelet':
									print("Vous allez effacer l'utilisateur "+delet[1]+" de la blacklist")
									b='dansDelet'
									s.send(a.encode())
									a=s.recv(64).decode()
									print("L'utilisateur peut de nouveau se connecter, il n'est plus dans la blacklist")

								elif ok=='stop':
									print("Vous avez fini les modifications su la blacklist")
									black='stop'

								else :
									print(ok)

							elif a == 'non' :
								print("Cet utilisateur n'est pas dans la Blacklist")

							else : 
								print("Erreur....")




					else :
						print(choix1)

