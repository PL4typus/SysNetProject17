#!/usr/bin/python

from M2Crypto import RSA, EVP
import os
import base64, hashlib



def SIGNelec(user,doc):

    print("<<<<<<<<<<< Module de Signature electronique >>>>>>>>>>>")
    buf=os.popen("ls clePriveUser/")
    buf=buf.read()
    print ("Repertoire des cle prive : \n")
    print (buf)
    os.popen("mkdir DocumentSigne/"+doc)

    if (user+".pem") not in buf:
        os.popen("openssl genrsa -out clePriveUser/"+user+".pem 2048")
        print(user+" ne possede pas encore de cle prive")

    os.popen("openssl rsa -in clePriveUser/"+user+".pem -pubout > DocumentSigne/"+doc+"/"+user+"_clePub.txt")
    pkey = RSA.load_key("clePriveUser/"+user+".pem")
    signText = pkey.sign(hashlib.sha256(doc+".txt").digest())
    print ("Empreinte de: "+doc+".txt generee")

    f=open("DocumentSigne/"+doc+"/"+doc+"_empreinte.txt","w")
    f.write(base64.b64encode(signText))
    #print (base64.b64encode(signText))
    print ("\n\n=======>"+doc+".txt signe")

SIGNelec("Adele","patient5")
SIGNelec("PL","patient6")
