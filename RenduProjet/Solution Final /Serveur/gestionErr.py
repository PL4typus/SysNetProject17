#!/usr/bin/python3.4


def failPassword(nom):

	f = open("blacklist.txt",'a')
	f.write(nom+";")

def verifBlacklist(nom):

	f=open("blacklist.txt",'r')
	lecture=f.read(1024)
	lecture=lecture.rstrip()
	bl=lecture.split(";")
	
	if nom in bl:
		return 0
	else:
		return 1


#failPassword("Emma")
#print (verifBlacklist("Paul"))
#print (verifBlacklist("Emma"))
#print (verifBlacklist("simon"))

