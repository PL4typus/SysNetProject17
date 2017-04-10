#!/usr/bin/env python3.4
# coding: utf-8

import sys, socket, os, time,numpy

def lecture_fichier(fichier) :
	f = open(fichier,'r')
	fo = f.read(1024)
	fo=fo.rstrip()
	l = fo.split(';')
	for i in range(len(l)) :
		l[i] = l[i].split(':')

	return lv


def rights(Droit,user):
    PATH_INF="../../Authentification/passwordInf.txt"
    PATH_INT="../../Authentification/passwordInt.txt"
    PATH_MED="../../Authentification/passwordMed.txt"
    PATH_DROITS_Inf="fichier_droitsInf.plp"
    PATH_DROITS_Int="fichier_droitsInt.plp"
    tab_droits={}
    ans=" "
    adoube=" "
    fich=" "
    ls = " "
    check=False

    if Droit=="M":
        while True:
            print("Modifier les droits de qui ?")
            print("")
            while ans not in {"Inf","I","INF","inf","i","q","Q"}:
                print("(Inf)irmier \t (I)nterne \t (Q)uitter")
                ans = input(">") #conn_client.recv().decode()
            if ans in {"Inf","INF"}:
                print("Quelle personne ?")
                l=lecture_fichier(PATH_INF)

               	for i in range(len(l)):
                    print(l[i][0])
                while check==False:
                    print("Veuillez choisir quelqu'un dans la liste ou Q pour quitter")
                    adoube=input(">>") #conn_client.recv().decode()
                    for i in range(len(l)):
                        if adoube == l[i][0]:
                            check = True

                if adoube not in {"q","Q"}:
                    ls= os.popen("ls user").read()
                    while fich not in ls:
                        print("Entrez un nom de fichier valide:")
                        fich =input(">>>") # conn_client.recv().decode()
                    print("Vous avez choisi ", fich)
                    print("Les droits sur ce fichier sont actuellement:")
                    rights=numpy.loadtxt(PATH_DROITS_Inf,dtype={'name': ('file','rights')},delimiter=";")
                    print(rights)


rights("M","user")
