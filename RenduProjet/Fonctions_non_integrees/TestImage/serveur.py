#!/usr/bin/env python
#-*- coding: utf_8 -*-

import socket
import os
import signal

TCP_IP = '127.0.0.1'
TCP_PORT=6263
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print ("Connection adresse:",addr)

while 1:
	print("----------------------------------------------------------------")
	print ("\n\t<<<<<<<<<<<Bienvenu sur le serveur de test>>>>>>>>>>>>")
	
	data = conn.recv(BUFFER_SIZE)
	data=data.decode()

	ls=os.popen("ls image/")
	ls=ls.read()
	print(ls)
	ls=ls.encode()
	print(ls)


	if data=="v":
		print("Je vais visionner")
		os.popen("x11vnc -many -rfbauth -viewonly ~/.vnc_passwd")
		os.popen("eog -f image/BigPanda.jpg")
		
	else:
		print ("received data:", data)


print ("\n\t<<<<<<<<<<Deconnexion du serveur de test>>>>>>>>>>>>\n")
print("----------------------------------------------------------------")



