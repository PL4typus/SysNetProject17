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

	if Droit=="M":
		while True:
			print("Voulez vous ajouter des droits ou en retirer ?  ")
			print(" (A)jouter \t (R)etirer \t (Q)uitter")
			ans=conn_client.recv().decode()
			if ans in {"A","a"}:
				print("Ajout de droits: A qui voulez vous ajouter des droits ? ")
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
                        print("entrez un nom de fichier ou repertoire suivi de r pour lecture ou r/w pour ecriture")
                        print("Exemple : pour authoriser ", adoube," à modifier le fichier fiche_michu, écrire:\"fiche_michu w\"")
                        print("Pour authoriser les droits de lecture et d'écriture, sur deux fichiers écrire:\"fiche_michu w\" puis taper [entrée] et écrivez un autre fichier. Pour terminer,entrer \"§\" ")
                        print("Vous avez choisi ",adoube,", quels droits voulez vous lui rajouter ?")
                        while fich != "§":
                            fich= conn_client.recv().decode()
                            if fich!="§":
                                fich=fich.rsplit(" ")
                                tab_droits[fich[0]]=fich[1]
                        f=open(PATH_DROITS+"_"+adoube,"r")
                        fich=f.read()
                        f.close()
                        fich=fich.rsplit(" ")
                        for i in tab_droits[]:
                            if i ==

			if ans in {"R","r"}:

			if ans in {"Q","q"}:
				break

	else:
		print("Vous n'avez pas l'autorisation de faire ça. Cet incident va être enregistré.")
		date=time.localtime()
		f=open("reports.log","a")
		report="user "+loginName+" a essayé de changer ses droits le "+ date.tm_mday+"/"+date.tm_mon+"/"+date.tm_year+" à "+date.tm_hour+":"+date.tm_min+":"+date.tm_sec+" .\n"


