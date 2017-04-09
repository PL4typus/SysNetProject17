#!/usr/bin/env python3.4
# coding: utf-8

import sys, socket, os, time

def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(1024)
	fo=fo.rstrip()
	l = fo.split(';') 
	for i in range(len(l)) :
		l[i] = l[i].split(':')
    f.close()
	return l

def rights(conn_client,Droit,user):
    PATH_INF="../../Authentification/passwordInf.txt"
    PATH_INT="../../Authentification/passwordInt.txt"
    PATH_MED="../../Authentification/passwordMed.txt"
    PATH_DROITS="fichier_droits"
    tab_droits={}
    ans=" "
    adoube=" "
    fich=" "
    ls = " "
    if Droit=="M":
        while True:
            print("Modifier les droits de qui ?")
            print("")
            while ans not in {"Inf","I","INF","inf","i","q","Q"}:
                print("(Inf)irmier \t (I)nterne \t (Q)uitter")
                ans = conn_client.recv().decode()
            if ans in {"Inf","INF"}:
                print("Quelle personne ?")
                l=lecture_fichier(PATH_INF)
                for x in l[i][0]:
                    print(x)
          
                while (adoube not in l[i][0]) or (adoube not in {"q","Q"}):    
                    print("Veuillez choisir quelqu'un dans la liste ou Q pour quitter")
                    adoube=conn_client.recv().decode()

                if adoube not in {"q","Q"}:
                    ls= os.popen("ls user").read()
                    while fich not in ls:
                        print("Entrez un nom de fichier valide:")
                        fich = conn_client.recv().decode()
                    print("Vous avez choisi ", fich)
                    print("Les droits sur ce fichier sont actuellement


