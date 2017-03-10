#!/usr/bin/python
#-*- coding: utf-8 -*-

from module_thread import *
import socket,sys,os

TCP_IP  = '127.0.0.1'
TCP_PORT = 6262
BUFFER_SIZE = 2048

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((TCP_IP,TCP_PORT))
while True:
	s.listen(5)
	print('En écoute sur ', TCP_PORT,'...')
	(clientsocket, (ip,port)) = s.accept()
	newthread = ClientThread(ip, port, clientsocket)
	newthread.start()


	
	
		
	
	




s.close()




