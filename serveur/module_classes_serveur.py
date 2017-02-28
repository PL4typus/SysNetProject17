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

		print('Connection de ',self.ip,': ',self.port)
		
		r = self.clientsocket.recv(2048)
		print('Ouverture du fichier: ', r, '...')
		fp = open(r, 'rb')
		self.clientsocket.send(fp.read())
		
		print ('Client déconnecté...')

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("192.168.1.35",6262))

while True:
	tcpsock.listen(10)
	print('En écoute...')
	(clientsocket, (ip,port)) = tcpsock.accept()
	newthread = ClientThread(ip, port, clientsocket)
	newthread.start()
