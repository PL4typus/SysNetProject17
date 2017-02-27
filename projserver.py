#!/usr/bin/python



import socket

import os

import sys



TCP_IP  = '127.0.0.1'

TCP_PORT = 6262



BUFFER_SIZE = 20



s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((TCP_IP,TCP_PORT))

s.listen(1)



conn, addr = s.accept()



data = conn.recv(BUFFER_SIZE)

print s.fileno

rep = os.popen(data)

conn.send(rep.read())





conn.close()




