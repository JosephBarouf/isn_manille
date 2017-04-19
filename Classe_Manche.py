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
from Classe_Tour import Tour
from Classe_Joueur import Joueur
from Classe_JeuDeCarte import JeuDeCarte

class Manche : 
	def __init__ (self, bouton_press, kijou, nom_joueur1, nom_joueur2, decount, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) :
		self.bouton_press = bouton_press
		self.kijou = kijou
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.decount = decount
		self.carte_main_joueur1 = carte_main_joueur1
		self.carte_main_joueur2 = carte_main_joueur2
		self.carte_show_joueur1 = carte_show_joueur1
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1
		self.carte_hide_joueur2 = carte_hide_joueur2

	def prepareManche(self) : 
		from Classe_root import root
		if self.bouton_press == "" :
			distribuer_carte = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			distribuer_carte.distribuer()
		else : 
			"""problème, ne revient pas dans root.../:"""
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
					jeu.startGame()

	def startManche(self) :
		terrain = 0
		carte_terrain = []
		debut_tour = Tour(kijou = self.kijou, atout = 0, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 1, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self. carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self. carte_hide_joueur2)
		debut_tour.joueCarte(terrain = terrain, carte_terrain = carte_terrain)
