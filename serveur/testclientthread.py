# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 6364))
file_name = "projserver.py" # utilisez raw_input() pour les anciennes versions python
s.send(file_name.encode())
file_name = "recu.py"
r = s.recv(1024)
with open(file_name,'wb') as _file:
    _file.write(r)
print ('Le fichier a été correctement copié dans ', file_name)

