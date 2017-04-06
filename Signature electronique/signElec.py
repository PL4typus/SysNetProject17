#!/usr/bin/python

from M2Crypto import RSA, EVP
import os
import base64, hashlib, sys


def SIGNelec(user,doc):
    chemin="../Signature\ electronique/"
    print("<<<<<<<<<<< Module de Signature electronique >>>>>>>>>>>")
    buf=os.popen("ls ../Signature\ electronique/clePriveUser")
    buf=buf.read()
    print ("Repertoire des cle prive : \n")
    print (buf)
    os.popen("mkdir ../Signature\ electronique/DocumentSigne/"+doc)

    if (user+".pem") not in buf:
        os.popen("openssl genrsa -out ../Signature\ electronique/clePriveUser/"+user+".pem 2048")
        print(user+" ne possede pas encore de cle prive")

    os.popen("openssl rsa -in ../Signature\ electronique/clePriveUser/"+user+".pem -pubout > ../Signature\ electronique/DocumentSigne/"+doc+"/"+user+"_clePub.pub")
    pkey = RSA.load_key("../Signature electronique/clePriveUser/"+user+".pem")
    signText = pkey.sign(hashlib.sha256("user/"+doc+".txt").digest())
    print ("Empreinte de: "+doc+".txt generee")

    f=open("../Signature electronique/DocumentSigne/"+doc+"/"+doc+"_empreinte.txt","w")
    f.write(base64.b64encode(signText))
    #print (base64.b64encode(signText))
    print ("\n\n=======>"+doc+".txt signe")

SIGNelec(sys.argv[1],sys.argv[2])
