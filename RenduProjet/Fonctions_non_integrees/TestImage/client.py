#!/usr/bin/env python
#-*- coding: utf_8 -*-

import socket
import os

localhost = '127.0.0.1'
port = 6263
BUFFER_SIZE=100

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port
s.connect((localhost,port))

# Protocol exchange - sends and receives
print("----------------------------------------------------------------")
print ("\n\t<<<<<<<<<<<Bienvenu sur le serveur de test>>>>>>>>>>>>")

msg_envoye = b""

while msg_envoye != ("EXIT"):
	print ("Que voulez vous faire?\n- v pour visionner\n")
	msg_envoye=input(">> ")
	print(msg_envoye)
	s.send(msg_envoye.encode())

	if msg_envoye=="v":
		print("Je vais visionner mon image")
		os.popen("gvncviewer "+localhost+":0")

	else:
		
		s.send(msg_envoye.encode())
		

print ("\n\t<<<<<<<<<<Deconnexion du serveur de test>>>>>>>>>>>>\n")
print("----------------------------------------------------------------")
