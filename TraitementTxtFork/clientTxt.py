#!/usr/bin/env python4.4
#coding: utf8


import socket
from getpass import getpass


TCP_IP ='127.0.0.1'

TCP_PORT = 6262

BUFFER_SIZE = 1024



s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((TCP_IP,TCP_PORT))
saisie=""

def PlsrLignes ():
	a = " "
	b = ""
	while str(b) != "§":
		b = input("> ")
		if str(b) != "§" :
			a = a + "\n"+str(b)
	return a


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
				print (data)
				if data == "1":
					print("Vous etes un Médecin")
					service=False
				elif data == "2":
					print("Vous etes un Infirmier")
					service=False
				elif data == "3":
					print("Vous etes un Interne")
					service=False
				else:
	
					print("Service inconnu")

			while session and user != 'retour':

				user=input("Utilisateur: ")
				user=user.encode()
				s.send(user)
		
				data2=s.recv(30)
				data2=data2.decode()	
				print(data2)
				
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
					print("Session ouverte")
					verrouille = False
				else:
					print("Mot de passe incorrect")
		while 1 :
			cmd=input("Saisir la commande ")
			l = cmd.split(" ")
			if l[0]== "edit" :
				if len(l) < 2 :
					print ("Erreur : argument manquant")
				else :
					s.send(cmd.encode())
					print ("Voici l'affichage du fichier que vous voulez editer :\n")
					rep=s.recv(BUFFER_SIZE)
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
    
			elif l[0]=="creer" :
				if len(l) < 2 :
					print ("Erreur : argument manquant")
				else :
					s.send(cmd.encode())
					rep = s.recv(BUFFER_SIZE)
					rep=rep.decode()
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

						hop=input("Saisie de la date d'entrée à l'hôpitale: ")
						hop=str(hop)+" "
						s.send(hop.encode())
					else :
						err = "ERREUR"
						s.send(err.encode())
					print("Fin de la saisie")

			elif l[0] == "1" :
				break
			else :
				s.send(cmd.encode())
				rep=s.recv(BUFFER_SIZE)
				print (rep.decode())




