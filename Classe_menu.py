 #-------------------------------------------------------------------------------
# Name:        Classe_main.py
# Purpose:
#
# Author:		JosephVPetit
#
# Created:     15/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------
from Classe_root import root 

jeu = root()
print("=================PyManille=================\n")

while True :
	r = 0
	while(r!=1 and r!=2 and r!=3) :
			r = int(input("\
1: Créer un compte\n\
2: Lister les comptes\n\
3: Start\n"))

	if(r == 1) :
		jeu.creerCompte()	#Tip reseau : Pour les 3 condition qui suivent faire un genre de menus. Première page d'accueil
	elif(r == 2) :
		jeu.listerCompte()
	elif (r == 3) :
		jeu.startGame()