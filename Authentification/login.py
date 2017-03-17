#!/usr/bin/python3.4
#Client authentification
#coding: utf8
import os
from getpass import getpass
import hashlib


import socket
TCP_IP = '127.0.0.1'
TCP_PORT=6262
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

s, addr = s.accept()

print ("Connection adresse:",addr)

DROIT=""

def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(1024)
	fo=fo.rstrip()
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	return l


def LOGIN():
	tout = True
	session = True
	metier = True
	verrouille = True
	time=4
	

	while tout :
		user = ''
		while metier:
			
			service=s.recv(30)
			service=service.decode()
			print (service)
			if service == "Medecin":
				DROIT="M"
				l=lecture_fichier("passwordMed.txt")
				metier = False
				s.send(b"1")
			elif service == "Infirmier":
				DROIT="INF"
				l=lecture_fichier("passwordInf.txt")
				metier = False
				s.send(b"2")	
			elif service == "Interne":
				DROIT="I"
				l=lecture_fichier("passwordInt.txt")
				metier = False
				s.send(b"3")
			else:
				s.send(b"0")
			
		while session and user != 'retour':

			
			user= s.recv(20)
			user=user.decode()
			print ("user",user)
			if user == "retour" :
				metier = True
				s.send(b"return")
				print ("Boucle retour")
				break
			else :
		
				for i in range(len(l)):
					
					if user == l[i][0]:
						s.send(b"1")
						session = False
						tout = False
						print ( "j'ai trouvé",user)
				if session == True:
					s.send(b"0")
					print ( "je n'ai pas trouvé",user)	
			
		while verrouille and tout == False :
			verif=s.recv(20)
			print (verif.decode())
			time-=1
			Timeline="Reste "+str(time)+" essai"
			Timeline=Timeline.encode()
			s.send(Timeline)
			
			if time == 0:
				s.send(b"0")
				break
			else:
				saisie = s.recv(30)
				saisie=saisie.decode()
				hash_mdp = hashlib.sha256(saisie.encode()).hexdigest()

			
			for i in range(len(l)):
				
				if user == l[i][0]:
					if hash_mdp == l[i][1]:
						verrouille=False
						s.send(b"1")
					else:
						s.send(b"0")
	s.close()

LOGIN()
print("Fin serveur")


