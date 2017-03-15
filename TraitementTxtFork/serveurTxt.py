#!/usr/bin/env python3.4
#-*- coding: utf-8 -*-

import socket,sys,os

TCP_IP  = '127.0.0.1'
TCP_PORT = 6262
BUFFER_SIZE = 2048

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((TCP_IP,TCP_PORT))

def barman(conn,ip,port):
	print("child process PID = ",os.getpid()," is client with ",ip," : ",port)
	data = conn.recv(BUFFER_SIZE)
	droit=data.decode()
	while 1 :
			data = conn.recv(BUFFER_SIZE)
			data= data.decode()
			if droit == "m" :
				os.popen("cd user/;chmod +w $PWD")
			else :
				os.popen("cd user/;chmod -w $PWD")
			print (data)
			l = data.split(" ")

#----------------------------------------------
			if l[0]== "edit" and droit == "m":
				r = os.popen("cd user/;cat "+l[1]+" 2>&1")
				err = os.popen("cd user/;cat "+l[1]+" 1>&2;echo $?");
				err= err.read()[0]
				print ("\nerr :", err)
				if err == "0" :
					conn.send((r.read()).encode())
					num = conn.recv(BUFFER_SIZE)
					num = num.decode()
					edit = conn.recv(BUFFER_SIZE)
					edit = edit.decode()
					f=open(l[1]+"b",'r')
					fiche=f.read()
					f.close()
					tabfich = fiche.split("*")
					tabfich[int(num)]= edit
					texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n(3)Allergies: "+tabfich[3]+"\n(4)Symptomes: " +tabfich[4]+"\n(5)Diagnostique: "+tabfich[5]+"\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]
					f=open(l[1],'w')
					f.write(texte)
					f.close()
					os.popen("mv "+l[1]+" user/");
					f=open(l[1]+"b",'w')
					f.write("*".join(tabfich))
					f.close()
					r2 = os.popen("cd user/;cat "+l[1])
					conn.send((r2.read()).encode())
				else :
					sr = "1"
					conn.send(sr.encode())
#---------------------------------------------------------

			elif l[0] == "creer" and droit == "m":
				err = os.popen("cd user/;cat "+l[1]+" 1>&2;echo $?");
				err = err.read()[0]
				conn.send(err.encode())
				i=1
				tabfich = []
				donne = conn.recv(BUFFER_SIZE)
				if donne.decode() != "ERREUR":
					tabfich.append(1)
					tabfich[0]= donne.decode()+" "
					while (i<=7) :
						tabfich.append(1)
						donne = conn.recv(BUFFER_SIZE)
						tabfich[i]= donne.decode()+" "
						i = i+1
					print (tabfich)
					texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n(3)Allergies: "+tabfich[3]+"\n(4)Symptomes: " +tabfich[4]+"\n(5)Diagnostique: "+tabfich[5]+"\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]
					f=open(l[1],'w')
					f.write(texte)
					f.close()
					os.popen("mv "+l[1]+" user/");
					f=open(l[1]+"b",'w')
					f.write("*".join(tabfich))
					f.close()
  				
#---------------------------------------------------------
			elif l[0] == "1":
				break 
			else :
				rep = os.popen("cd user/;"+data+" 2>&1")
				reponse="reponse: \n"+rep.read()
				conn.send(reponse.encode())
while True:
	s.listen(5)
	print('En écoute sur ', TCP_PORT,'...')
	(conn, (ip,port)) = s.accept()
	child_pid=os.fork()
	if child_pid == 0:#si pid = 0 ça veut dire qu'on est dans le child process

		barman(conn,ip,port )
	

s.close()
