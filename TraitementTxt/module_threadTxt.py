#!/usr/bin/env python3.4
# coding: utf-8

import sys,socket,os,threading

class ClientThread(threading.Thread):
  	
  	def __init__(self, ip, port, clientsocket):
  		self.BUFFER_SIZE = 2048
  		threading.Thread.__init__(self)
  		self.ip = ip
  		self.port = port
  		self.conn = clientsocket
  		print('## Nouveau thread pour ', self.ip,': ', self.port)
  
  	def run(self):

  		data = self.conn.recv(self.BUFFER_SIZE)
  		droit=data.decode()
  		while 1 :
  			data = self.conn.recv(self.BUFFER_SIZE)
  			data= data.decode()
  			if droit == "m" :
  				os.popen("cd user/;chmod +w $PWD")
  			else :
  				os.popen("cd user/;chmod -w $PWD")
  			print (data)
  			l = data.split(" ")

#----------------------------------------------
  			if l[0]== "edit":
  				r = os.popen("cd user/;cat "+l[1])
  				self.conn.send((r.read()).encode())
  				num = self.conn.recv(self.BUFFER_SIZE)
  				num = num.decode()
  				edit = self.conn.recv(self.BUFFER_SIZE)
  				edit = edit.decode()
  				f=open(l[1]+"b",'r')
  				fiche=f.read()
  				f.close()
  				tabfich = fiche.split("*")
  				tabfich[int(num)]= edit
  				texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n (3)Allergies: "+tabfich[3]+"\n(4)Symptomes: " +tabfich[4]+"\n(5)Diagnostique: "+tabfich[5]+"\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]
  				f=open(l[1],'w')
  				f.write(texte)
  				f.close()
  				os.popen("mv "+l[1]+" user/");
  				f=open(l[1]+"b",'w')
  				f.write("*".join(tabfich))
  				f.close()
  				r = os.popen("cd user/;cat "+l[1])
  				self.conn.send((r.read()).encode())
#---------------------------------------------------------

  			elif l[0] == "creer" :
  				i=0
  				tabfich = []
  				while (i<=7) :
  					tabfich.append(1)
  					donne = self.conn.recv(self.BUFFER_SIZE)
  					tabfich[i]= donne.decode()+" "
  					i = i+1
  				print (tabfich)
  				texte = "(0)Nom: "+tabfich[0]+" (1)Prénom: "+tabfich[1]+" (2)Age: "+tabfich[2]+"\n (3)Allergies: "+tabfich[3]+"\n(4)Symptomes: " +tabfich[4]+"\n(5)Diagnostique: "+tabfich[5]+"\n(6)Commentaire: "+tabfich[6]+"\n\n(7)Date d'entrée à l'hôpital : "+tabfich[7]
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
  				self.conn.send(reponse.encode())


























