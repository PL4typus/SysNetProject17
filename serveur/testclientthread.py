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
	with open(file_name,'wb') as _file:
		_file.write(r)
	print ('Le fichier a été correctement copié dans ', file_name)
	file_name = "exit"
	s.send(file_name.encode())
s.close()
