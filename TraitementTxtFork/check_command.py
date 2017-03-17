#!/usr/bin/env python3.4
#coding: utf-8

import os,sys,

def command_checker(command, status,conn, ip, port):

	command = command.split(' ')
	buf=os.popen("ls user")
	buf= buf.read()

	if command[0] == "ls":#modifier options
		rep=os.popen("ls user -go")
		reponse =rep.read()

	elif command[0] == "cat":
		if command[1] not in buf:
			reponse = "Vous n'avez pas l'autorisation de faire ça, ou le fichier demandé n'existe pas!\n"
		else:
			cccp="cat user/"+command[1]
			rep=os.popen(cccp)
			reponse=rep.read()

	elif command[0] == "rm":
		if status=="m": #a modifier avec login()
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


	elif command[0] == "mkdir":
		#wip
		print("lol")
	elif command[0] == "edit": #nom du fichier
		#wip
		serveurTxt.EDIT(conn, command[1])
	elif command[0] == "creer": #nom du fichier
		#wip
		serveurTxt.CREER(conn,command[1])
	conn.send(reponse.encode())
