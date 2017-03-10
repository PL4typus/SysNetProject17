#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

from module_thread import *
import socket,sys,os

TCP_IP  = '127.0.0.1'
TCP_PORT = 6262
BUFFER_SIZE = 2048

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((TCP_IP,TCP_PORT))

def barman(conn,ip,port):
	print("child process PID = "+os.getpid()+" is client with "+ip+" : "+port)
	data = conn.recv(BUFFER_SIZE)
	droit = data.decode()
	while True:
		data = conn.recv(BUFFER_SIZE)
		data = data.decode()
		if droit == "m" :
			os.popen("chmod +w $PWD")
		else:
			os.popen("chmod -w $PWD")
		print(data)
		if data== "1":
			break
		rep = os.popen(data+" 2>&1")
		reponse="reponse : \n"+rep.read()
		conn.send(reponse.encode())
	conn.close()
while True:
	s.listen(5)
	print('En écoute sur ', TCP_PORT,'...')
	(conn, (ip,port)) = s.accept()
	child_pid=os.fork()
	if child_pid == 0:#si pid = 0 ça veut dire qu'on est dans le child process
		print("\nConnection avec client sur "+ port)
		barman(conn,ip,port )
	

s.close()




