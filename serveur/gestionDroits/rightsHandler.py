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
	return l

def rights(Droit,user):
	if Droit=="M":
		while True:
			print("Voulez vous ajouter des droits ou en retirer ?  ")
			print(" (A)jouter \t (R)etirer \t (Q)uitter")
			ans=input(">")
			if ans in {"A","a"}:
				print("Ajout de droits: A qui voulez vous ajouter des droits ? ")
				while ans not in {"Inf","I","INF","inf","i","q","Q"}:
					print("(Inf)irmier \t (I)nterne \t (Q)uitter")
					ans = input("\t>")
				if ans in {"Inf","INF"}:
					print("Quelle personne ?")
					
					l=lecture_fichier("../../Authentification/passwordInf.txt")
					for x in l[i][0]:
						
						 
				
			if ans in {"R","r"}:
				
			if ans in {"Q","q"}:
				break
	
	else:
		print("Vous n'avez pas l'autorisation de faire ça. Cet incident va être enregistré.")
		date=time.localtime()
		f=open("reports.log","a")
		report="user "+loginName+" a essayé de changer ses droits le "+ date.tm_mday+"/"+date.tm_mon+"/"+date.tm_year+" à "+date.tm_hour+":"+date.tm_min+":"+date.tm_sec+" .\n"
		
		
