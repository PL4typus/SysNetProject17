#!/usr/bin/env python3.4
# coding: utf-8

import sys, socket, os, time,numpy

## Fonction qui renvoie une liste de liste de la forme : [[user1,mdp1],[user2,mdp2]] ##
def lecture_fichier(fichier) : #[[nom1,mdp1],[nom2,mdp2]....]
	f = open(fichier,'r')
	fo = f.read(2048)
	l=fo.splitlines()
	for i in range(len(l)) :
		l[i] = l[i].split(':')
	f.close()
	return l



def rightsManager(Droit,user):
    PATH_INF="/home/squirrel/Documents/projets/NETWORK/projetreseau17/Authentification/passwordInf.txt"
    PATH_INT="/home/squirrel/Documents/projets/NETWORK/projetreseau17/Authentification/passwordInt.txt"
    PATH_MED="/home/squirrel/Documents/projets/NETWORK/projetreseau17/Authentification/passwordMed.txt"
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
            if ans in {"Inf","INF","inf"}:
                print("Quelle personne ?")
                l=lecture_fichier(PATH_INF)
               	for i in l:
                    print(i[0])
                while check==False:
                    print("Veuillez choisir quelqu'un dans la liste ou Q pour quitter")
                    adoube=input(">>") #conn_client.recv().decode()
                    for i in l:
                        if (adoube == i[0]) or (adoube in {"q","Q"}):
                            check = True
                if adoube not in {"q","Q"}:
                    print(adoube," a actuellement les droits suivants:")
                    f = open(PATH_DROITS_Inf,"r")
                    rights=f.read().splitlines()
                    f.close()
                    saved_i=0
                    for i in range(len(rights)):
                        rights[i]=rights[i].split(";")
                    for i in range(len( rights)):
                        if rights[i][0]==adoube:
                            print("Par defaut, ",rights[i][2])
                            saved_i=i
                            for j in range(len(rights[i])):
                                if j%2==1:
                                    print("Pour le fichier ",rights[i][j],": ",rights[i][j+1])
                    print("Entrez un nom de fichier puis les nouveaux droits. Ex: ficheMichu rw")
                    print("r : droits de lecture \t w : droits d'écriture (la personne verra le contenu du fichier lors de l'édition")
                    print("Entrez § pour terminer")
                    verdict=" "
                    t_verdict=rights[saved_i][1]+" "+rights[saved_i][2]
                    k=0
                    while verdict != "§":
                        verdict=input(">>>>>:")
                        if verdict != "§":
                            t_verdict = t_verdict+ ";"+verdict
                    t_verdict=t_verdict.split(";")
                    for i in range(len(t_verdict)):
                        t_verdict[i]=t_verdict[i].split(" ")
                    di_verdict={}
                    for i in range(len(t_verdict)):
                        for j in range(len(t_verdict[i])):
                            di_verdict[t_verdict[i][0]]=t_verdict[i][1]
                    for key in di_verdict.keys():
                        if key not in rights[saved_i]:
                                rights[saved_i]=(di_verdict.get(key))
                        for i in range(len(rights[saved_i])):
                            if rights[saved_i][i]==key:
                                print(rights[saved_i][i],rights[saved_i][i+1])
                                rights[saved_i][i+1]=di_verdict.get(key,"r")
                    # j'aurais du mettre des commentaires je sais plus trop ce que j'ai voulu faire
                    print(di_verdict)
                    print(rights)







           



rightsManager("M","/home/squirrel/Documents/projets/NETWORK/projetreseau17/TraitementTxtFork/user")

