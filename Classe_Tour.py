#-------------------------------------------------------------------------------
# Name:        Classe_JeuDeCarte.py
# Purpose:
#
# Author:		Joseph Petit
#
# Created:     12/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

from Classe_Carte import Carte

class Tour : 
	"""Classe organisant le déroulement d'un tour"""
	def __init__(self, kijou, atout, nom_joueur1, nom_joueur2, decount, tour, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) : 
		self.kijou = kijou
		self.atout = atout
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.decount = decount
		self.tour = tour
		self.carte_main_joueur1 = carte_main_joueur1
		self.carte_main_joueur2 = carte_main_joueur2
		self.carte_show_joueur1 = carte_show_joueur1
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1
		self.carte_hide_joueur2 = carte_hide_joueur2

	def joueCarte(self, terrain, carte_terrain) :
		from Classe_Joueur import Joueur
		while self.decount < 60 :
			if self.tour == 1 :
				#Cette condition est peut etre à mettre dans un autre méthode correspondant à choisir l'atout. 
				if self.kijou == 1 :
					voir = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2) #on va chercher la main du joueur en question dans la classe joueur
					voir.afficherCarteMainJoueur()
					voir.afficherCarteShowJoueur()
					choose_atout = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					choose_atout.atout(choix_atout = int(input("{0}, choisissez l'atout : \n 1 --> coeur \n 2 --> carreau \n 3 --> trèfle \n 4 --> pique\n".format(self.nom_joueur1))), carte_terrain = carte_terrain)
				else :
					voir = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2) #on va chercher la main du joueur en question dans la classe joueur
					voir.afficherCarteMainJoueur()
					voir.afficherCarteShowJoueur()
					choose_atout = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					choose_atout.atout(choix_atout = int(input("{0}, choisissez l'atout : \n 1 --> coeur \n 2 --> carreau \n 3 --> trèfle \n 4 --> pique\n".format(self.nom_joueur2))), carte_terrain = carte_terrain) #Choix de l'atout par le dealer qui mène à une initialisation de la puissance de chaque cartes
			else :
				if terrain == 2 : #Vérifie si les deux joueurs ont joué ou non
					print("\n Les deux joueurs ont sélectionné leurs cartes ! \n")
					afficher_terrain = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					afficher_terrain.afficherCarteTerrain(carte_terrain = carte_terrain)
					battle = self.battle(carte_terrain = carte_terrain, power_joueur1 = 0, power_joueur2 = 0, check = 0)
				else : #Lorsque tout les joueurs n'ont pas selectionné leur carte
					if self.kijou == 1 :
						print("{0}, c'est à vous de jouer".format(self.nom_joueur1))
						jouer = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
						jouer.joueCarte(terrain = terrain, carte_terrain = carte_terrain, atout = self.atout)
					else :
						print("{0}, c'est à vous de jouer".format(self.nom_joueur2))
						jouer = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
						jouer.joueCarte(terrain = terrain, carte_terrain = carte_terrain, atout = self.atout)

		#elif 0 < self.decount < 60 :
	def battle(self, carte_terrain, power_joueur1, power_joueur2, check) :
		if check == 0 :
			carte_joueur1 = ""
			carte_joueur2 = ""
			if self.kijou == 1 : #Si le dernier joueur à avoir joué est le joueur 1
				carte_joueur1 = carte_terrain[1]
				carte_joueur2 = carte_terrain[0]
			else : #Si le dernier joueur à avoir joué est le joueur 2
				carte_joueur1 = carte_terrain[0]
				carte_joueur2 = carte_terrain[1]
			valeur = Carte(atout = self.atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			valeur.powerOn(carte_joueur1 = carte_joueur1, carte_joueur2 = carte_joueur2)
		else :
			if power_joueur1 < power_joueur2 : 
				print("\n {0} remporte ce tour ! \n".format(self.nom_joueur2))
			elif power_joueur1 > power_joueur2 : 
				print("\n {0} remporte ce tour ! \n".format(self.nom_joueur1))
			else : 
				print("Egalité") #revoir les règles, je ne sais plus ce qu'il se passe quand il y a égalité
		terrain = 0
		carte_terrain = []
		debut_tour = Tour(kijou = self.kijou, atout = self.atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 2, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self. carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self. carte_hide_joueur2)
		debut_tour.joueCarte(terrain = terrain, carte_terrain = carte_terrain)







