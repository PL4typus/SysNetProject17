# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 6262))
file_name = " "
while file_name != "exit":
	file_name =input(">>")
	s.send(file_name.encode())
	file_name = "recu.py"
	r = s.recv(1024)
	print(r.decode())
s.close()
