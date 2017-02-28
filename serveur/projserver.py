#!/usr/bin/python



import socket,sys,os

TCP_IP  = '127.0.0.1'
TCP_PORT = 6262
BUFFER_SIZE = 1024

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((TCP_IP,TCP_PORT))

s.listen(5)

conn, addr = s.accept()
print('Connection entrante :', addr)


data = conn.recv(BUFFER_SIZE)

print s.fileno

rep = os.popen(data)

conn.send(rep.read())





conn.close()




