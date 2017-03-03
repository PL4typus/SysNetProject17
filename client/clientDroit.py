#!/usr/bin/python



import socket



TCP_IP ='127.0.01'

TCP_PORT = 6262

BUFFER_SIZE = 1024



s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((TCP_IP,TCP_PORT))

d=raw_input("Etes vous medecin ou infirmiere (m/i) : ")

s.send(d)

while 1 :
  cmd=raw_input("Saisir la commande ")
  if cmd == "1" :
    break

  s.send(cmd)
  rep=s.recv(BUFFER_SIZE)
  print rep

