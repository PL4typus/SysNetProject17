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
  l = cmd.split(" ")
  if l[0]== "edit" :
    s.send(cmd.encode())
    print ("Voici l'affichage du fichier que vous voulez editer :\n")
    rep=s.recv(BUFFER_SIZE)
    rep = rep.decode()
    if rep != "1" :
      print (rep)
      num = "8"
      while num < "0" or num > "7" :
        num = input("\n\nATTENTION : Quand vous editez un champs vous réecrivez par dessus !\n\nQuelle champs voulez vous editer ? (mettre le n°) : ")
      s.send(num.encode())
      edit=input("Ecrivez ce que vous voulez ecrire dans ce champs : ")
      s.send(edit.encode())
      print ("Voici l'affichage du fichier après edition :\n")
      rep=s.recv(BUFFER_SIZE)
      print (rep.decode())
    else :
      print (rep)
      print ("Erreur le fichier ", l[1], " n'existe pas\n")
    
  elif l[0]=="creer" :
    s.send(cmd.encode())
    rep = s.recv(BUFFER_SIZE)
    rep=rep.decode()
    if rep == "0":
      ecrase = input("Un fichier du même nom existe déjà voulez vous l'écraser ? (non:0/oui:1)\n")
    if (rep != "0") or ecrase==1 :
      print ("\nEntrez les informations concernant le patient\n")
      nom=input("Saisir le nom : ")
      s.send(nom.encode())
      prenom=input("Saisir le prenom : ")
      s.send(prenom.encode())
      age=input("Saisir l'age: ")
      s.send(age.encode())
      aller=input("Saisir ses allergies: ")
      s.send(aller.encode())
      symp=input("Saisir ses symptomes: ")
      s.send(symp.encode())
      diag=input("Saisie du diagnostique: ")
      s.send(diag.encode())
      com=input("Saisie des commentaires: ")
      s.send(com.encode())
      hop=input("Saisie de la date d'entrée à l'hôpitale: ")
      s.send(hop.encode())
    else :
      err = "ERREUR"
      s.send(err.encode())
    print("Fin de la saisie")

  elif l[0] == "1" :
    break
  else :
    s.send(cmd.encode())
    rep=s.recv(BUFFER_SIZE)
    print (rep.decode())

