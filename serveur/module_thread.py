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
  				os.popen("chmod +w $PWD")
  			else :
  				os.popen("chmod -w $PWD")
  			print (data)
  			if data == "1":
    				break 
  
  			rep = os.popen(data+" 2>&1")
  			reponse="reponse: \n"+rep.read()
  			self.conn.send(reponse.encode())
		
