#-------------------------------------------------------------------------------
# Name:        Classe_JeuDeCarte.py
# Purpose:
#
# Author:		Joseph Petit
#
# Created:     22/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------
from Classe_Tour import whoBegin 

class Manche : 
	def __init__ (self, bouton_presse, first_joueur, decount) :
		self.bouton_presse = bouton_presse
		self.first_joueur = first_joueur
		self.decount = decount

	def startManche(self) : 
		if self.bouton_presse == "\n" :
			lancer_premier_tour = Tour(first_joueur = self.first_joueur, decount = decount)
			lancer_premier_tour.whoBegin()
		else :
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
				jeu.creerCompte()
			elif(r == 2) :
				jeu.listerCompte()
			elif (r == 3) :
				jeu.start()
