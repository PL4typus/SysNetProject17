******* Projet Réseau **********

Chef de projet : Pierre-Louis Palant
Membres du projet : Charlotte Rambourg, Aloïse Depelley, Adèle Journée

***************

Dans le dossier "Fonctions_non_integrees" se trouvent des fonctions que nous avons fait à part du projet mais qui n'ont pas eu le temps d'être intégrés.
Pour le dossier "TestImage" un serveur VNC sur la machine serveur est necessaire pour le bon fonctionnement du code.
Dans le dossier gestionDroits on trouve les fichiers et codes permettant la gestion dynamique des droits. Cette fonctionnalité n'est pas implémentée dans la version finale mais est presque terminée.
***************

Le rendu final de notre projet se trouve dans le dossier "RenduFinal". Vous trouverez un dossier "Client" qui contient le client "clientTxt.py" de notre projet, ainsi qu'un dossier "Serveur" qui contient le code du serveur "serveurTxt.py" et le dossier "user" qui sera le repertoire courant partagé entre les utilisateurs (il y aura aussi beaucoup de fichiers texte qui servent au bon fonctionnement du serveur) .
Pour le bon fonctionnement, le serveur doit être sur un poste qui possède les module suivant : M2crypto, Python2.7, Python3.4
Veillez également à lancer le serveur et le client depuis leur dossiers respectifs. 
****************

Voici les mot de passe utiles pour utiliser notre solution :

administrateur : 
	pseudo : admin
	mdp: root

Medecin :
	pseudo: Paul
	mdp: paulo

Infirmier :
	pseudo : simon
	mdp: cahier

Interne:
	pseudo : jules
	mdp : ipad
******************

Pour l'inscription d'un nouvel utilisateur, l'administrateur doit donner une clé selon le type d'utilisateur, les voici:

Medecin : bouteille
Infirmier : livre
Interne : portable

******************

Une fois connecté , vous pouvez faire 'help' pour obtenir un récapitulatif des commandes possible dans notre solution.

******************

organisation du projet :
Aloïse :  
	implementation des fonctions login et signup
	implémentation de l'interface administrateur
Charlotte:
	implementation des fonctions login et signup
	implementation du module de signature electronique
	Essai de tranfert de flux graphique sécurisé
Pierre-Louis:
        implémentation des commandes suivantes: ls , cat, rm
        implémentation du gestionnaire de clients
        Essai de réalisation de droits dynamiques types acl.

Adèle:
	implementation de la création et l'edition de fichier par formulaire, ainsi que des droits minimaux
	implementation des commandes suivantes : whereis,cp,cd,mkdir,help,clear,historique








