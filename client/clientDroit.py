#!/usr/bin/env python3.4



import socket



TCP_IP ='127.0.01'

TCP_PORT = 6262

BUFFER_SIZE = 1024



s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((TCP_IP,TCP_PORT))

d=input("Etes vous medecin ou infirmiere (m/i) : ")

s.send(d.encode())

while 1 :
  cmd=input("Saisir la commande ")
  if cmd == "1" :
    break

  s.send(cmd.encode())
  rep=s.recv(BUFFER_SIZE)
  print (rep.decode())

