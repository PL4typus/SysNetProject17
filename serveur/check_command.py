#!/usr/bin/env python3.4
#coding: utf-8

import os,sys

def check_command(command, status,conn, ip, port):

	command = command.split('')
	buf=os.popen("ls user")
	buf= buf.read()

	if command[0] == "ls":
		rep=os.popen("ls user -go")
		reponse =rep.read()

	elif command[0] == "cat":
		if command[1] not in buf:
			reponse = "Vous n'avez pas l'autorisation de faire ça!\n"
		else:
			rep=os.popen("cat user/"+command[2])
			reponse=rep.read()

	elif command[0] == "rm":
		if status="m": #a modifier avec login()
			if command[1] not in buf:
				reponse = "Vous n'avez pas l'autorisation de faire ça, ou le fichier demandé n'existe pas!\n"
			else:
				reponse = "Etes-vous sûr(e) de vouloir supprimer le fichier "+command[1] +"?   O/N ? \t Il ne sera pas recuperable."
				while ok == False:				
					conn.send(reponse.encode())
					data=conn.recv(2048).decode()
					if data in {"yes","oui","o","ouais","y","O","YES","Y","OUI","OUAIS"}:
						rep=os.popen("rm -vf"+command[1])
						reponse=rep.read()
						ok = True
					elif data in {"no","non", "n","NON","N","NO","NEIN"}
						reponse = "Ok, fichier non supprimé!"
						ok = True
		else:#modifier avec login()
			reponse="Vous n'avez pas l'autorisation de supprimer des fichiers!"
	elif command[0] == "mkdir":
		#todo
	elif command[0] == "edit": #nom du fichier
		#todo
	elif command[0] == "creer": #nom du fichier
		#todo
			
