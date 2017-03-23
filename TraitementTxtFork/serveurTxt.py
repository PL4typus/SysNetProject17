#!/usr/bin/env python3.4
#-*- coding: utf-8 -*-

import socket,sys,os
from getpass import getpass
import hashlib

TCP_IP  = '127.0.0.1'
TCP_PORT = 6262
BUFFER_SIZE = 2048

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((TCP_IP,TCP_PORT))




############################################################################################
## Fonction qui renvoie une liste de liste de la forme : [[user1,mdp1],[user2,mdp2]] ##
def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(1024)
	fo=fo.rstrip()
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	return l


###########################################################################################

def LOGIN(conn):
	tout = True
	session = True
	metier = True
	verrouille = True
	
	

	while tout :
		user = ''
		time=4
		while metier:
			
			service=conn.recv(30)
			service=service.decode()
			print (service)
			if service == "Medecin":
				DROIT="M"
				l=lecture_fichier("passwordMed.txt")
				metier = False
				conn.send(b"1")
			elif service == "Infirmier":
				DROIT="INF"
				l=lecture_fichier("passwordInf.txt")
				metier = False
				conn.send(b"2")	
			elif service == "Interne":
				DROIT="I"
				l=lecture_fichier("passwordInt.txt")
				metier = False
				conn.send(b"3")
			else:
				conn.send(b"0")
			
		while session and user != 'retour':

			user= conn.recv(20)
			user=user.decode()

			print ("user",user)
			if user == "retour" :
				metier = True
				conn.send(b"return")
				print ("Boucle retour")
				break
			else :
		
				for i in range(len(l)):
					if user == l[i][0]:
						conn.send(b"1")
						session = False
						tout = False
						print ( "j'ai trouvé",user)
				if session == True:
					conn.send(b"0")
					print ( "je n'ai pas trouvé",user)	
			
		while verrouille and tout == False :

			verif=conn.recv(20)
			print (verif.decode())
			time-=1
			Timeline="Reste "+str(time)+" essai"
			Timeline=Timeline.encode()
			conn.send(Timeline)
			
			if time == 0:
				#s.send(b"0")
				print("plus d'essai")
				tout = True
				metier=True
				session=True
				break
			else:
				saisie = conn.recv(30)
				saisie=saisie.decode()
				hash_mdp = hashlib.sha256(saisie.encode()).hexdigest()

			
				for i in range(len(l)):
					if user == l[i][0]:
						if hash_mdp == l[i][1]:
							verrouille=False
							conn.send(b"1")
						else:
							conn.send(b"0")

	return DROIT

def command_checker(command, status,conn, ip, port):

	command = command.split(' ')
	buf=os.popen("ls user")
	buf= buf.read()

	if command[0] == "ls":#modifier options
		rep=os.popen("ls user -go")
		reponse =rep.read()
		conn.send(reponse.encode())
	elif command[0] == "cat":
		if command[1] not in buf:
			reponse = "Vous n'avez pas l'autorisation de faire ça, ou le fichier demandé n'existe pas!\n"
		else:
			cccp="cat user/"+command[1]
			rep=os.popen(cccp)
			reponse=rep.read()
		conn.send(reponse.encode())
	elif command[0] == "rm":
		if status=="M": #a modifier avec login()
			if command[1] not in buf:
				reponse = "Vous n'avez pas l'autorisation de faire ça, ou le fichier demandé n'existe pas!\n"
			else:
				reponse = "Etes-vous sûr(e) de vouloir supprimer le fichier "+command[1] +"?   O/N ? \t Il ne sera pas recuperable."
				ok = False
				while ok == False:				
					conn.send(reponse.encode())
					data=conn.recv(2048).decode()
					if data in {"yes","oui","o","ouais","y","O","YES","Y","OUI","OUAIS"}:
						cccp="rm -vf user/"+command[1]
						print(cccp)
						rep=os.popen(cccp)
						reponse=rep.read()
						ok = True
					elif data in {"no","non", "n","NON","N","NO","NEIN"}:
						reponse = "Ok, fichier non supprimé!"
						ok = True
		else:#modifier avec login()
			reponse="Vous n'avez pas l'autorisation de supprimer des fichiers!"
		conn.send(reponse.encode())

	elif command[0] == "mkdir":
		#wip
		print("lol")
	elif command[0] == "edit": #nom du fichier
		#wip
		EDIT(conn, command[1])

	elif command[0] == "creer": #nom du fichier
		#wip
		CREER(conn,command[1])

def EDIT (conn, nomF):
	r = os.popen("cd user/;cat "+nomF+" 2>&1")
	err = os.popen("cd user/;cat "+nomF+" 1>&2;echo $?");#pour voir si le fichier existe
	err= err.read()[0]
	print ("\nerr :", err)
	if err == "0" : #si le fichier existe
		conn.send((r.read()).encode())
		num = conn.recv(BUFFER_SIZE)#récupération du numéro a modifier
		num = num.decode()
		edit = conn.recv(BUFFER_SIZE)#récupération de la chaine de caractère à écrire
		edit = edit.decode()
		f=open(nomF+"b",'r')#récupération du fichier b qui sert récupérer les différents champs séparement
		fiche=f.read()
		f.close()
		tabfich = fiche.split("*")
		tabfich[int(num)]= edit
		texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n\n(3)Allergies: "+tabfich[3]+"\n\n(4)Symptomes: " +tabfich[4]+"\n\n(5)Diagnostique: "+tabfich[5]+"\n\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]+"\n"
		f=open(nomF,'w')
		f.write(texte)
		f.close()
		os.popen("mv "+nomF+" user/");#on écrit le fichier que l'utilisateur voit et on le met dans user/
		f=open(nomF+"b",'w')
		f.write("*".join(tabfich))#on écrit le fichier b
		f.close()
		r2 = os.popen("cd user/;cat "+nomF)
		conn.send((r2.read()).encode())#on renvoi l'affichage du fichier modifié
	else :#si le fichier existe pas
		sr = "1"
		conn.send(sr.encode())


def CREER (conn, nomF) :
	err = os.popen("cd user/;cat "+nomF+" 1>&2;echo $?");
	err = err.read()[0]
	conn.send(err.encode())#on envoie la retour de cat, si c'est 0 ça veut dire qu'un fichier du même nom existe et on va demander à l'utilisateur s'il veut l'écraser ou pas
	i=1
	tabfich = []
	donne = conn.recv(BUFFER_SIZE)
	if donne.decode() != "ERREUR":# si le fichier est ecrasé ou si il n'existe pas
		tabfich.append(1)# on ajoute un element à la liste
		tabfich[0]= donne.decode()+" "#on met la donné dans le tableau
		while (i<=7) :#on repète l'opération 6 fois
			tabfich.append(1)
			donne = conn.recv(BUFFER_SIZE)
			tabfich[i]= donne.decode()+" "
			i = i+1
		print (tabfich)
		texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n\n(3)Allergies: "+tabfich[3]+"\n\n(4)Symptomes: " +tabfich[4]+"\n\n(5)Diagnostique: "+tabfich[5]+"\n\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]+"\n"
		f=open(nomF,'w')
		f.write(texte)
		f.close()
		os.popen("mv "+nomF+" user/");#on ecrit le fichier utilisateur dans user/
		f=open(nomF+"b",'w')
		f.write("*".join(tabfich))#on écrit le fichier b
		f.close()
  				


def barman(conn,ip,port,DROIT):
	print("child process PID = ",os.getpid()," is client with ",ip," : ",port)
	# reception de m ou i pour savoir si c'est un médecin ou autre, à remplacer quand on mattra l'authentifictaion
	
	while 1 :
		data = conn.recv(BUFFER_SIZE)
		data= data.decode()
		print (DROIT)
		if DROIT == "M" : # attribution des droit
			os.popen("cd user/;chmod +w $PWD")
		else :
			os.popen("cd user/;chmod -w $PWD")
		print (data)
		command_checker(data,DROIT,conn,ip, port)
#----------------------------------------------
#			if l[0]== "edit" and droit == "m": #pour editer un texte seul les medecins peuvent
#				EDIT(conn,l[1])
#---------------------------------------------------------
#
#			elif l[0] == "creer" and droit == "m":
#				CREER(conn,l[1])
#---------------------------------------------------------
#			elif l[0] == "1":
#				break 
#			else :
#				rep = os.popen("cd user/;"+data+" 2>&1")
#				reponse="reponse: \n"+rep.read()
#				conn.send(reponse.encode())
while True:
	s.listen(5)
	print('En écoute sur ', TCP_PORT,'...')
	(conn, (ip,port)) = s.accept()
	child_pid=os.fork()
	if child_pid == 0:#si pid = 0 ça veut dire qu'on est dans le child process
		DROIT = LOGIN(conn)
		print ("droit ",DROIT)
		barman(conn,ip,port,DROIT)
	

s.close()
