#-------------------------------------------------------------------------------
# Name:        Classe_Carte.py
# Purpose:
#
# Author:		Joseph Petit
#
# Created:     12/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------


class Carte :
	"""Definition de la classe Carte"""
	def __init__(self, nom_joueur1, nom_joueur2, atout, decount, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) :
		"""Initialisation de la classe carte"""
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.atout = atout
		self.decount = decount
		self.carte_main_joueur1 = carte_main_joueur1
		self.carte_main_joueur2 = carte_main_joueur2
		self.carte_show_joueur1 = carte_show_joueur1
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1
		self.carte_hide_joueur2 = carte_hide_joueur2
	def powerOn(self, carte_joueur1, carte_joueur2) :
		from Classe_Tour import Tour
		power_joueur1 = 0
		power_joueur2 = 0
		if self.atout == 1 : #Si l'atout est coeur
			if carte_joueur1 == "sept_coeur" : 
				power_joueur1 = 9
			elif carte_joueur2 == "sept_coeur" : 
				power_joueur2 = 9
			elif carte_joueur1 == "huit_coeur" :
				power_joueur1 = 10
			elif carte_joueur2 == "huit_coeur" :
				power_joueur2 = 10
			elif carte_joueur1 == "neuf_coeur" :
				power_joueur1 = 11
			elif carte_joueur2 == "neuf_coeur" : 
				power_joueur2 = 11
			elif carte_joueur1 == "valet_coeur" : 
				power_joueur1 = 12
			elif carte_joueur2 == "valet_coeur" :
				power_joueur2 = 12
			elif carte_joueur1 == "dame_coeur" : 
				power_joueur1 = 13
			elif carte_joueur2 == "dame_coeur" :
				power_joueur2 = 13
			elif carte_joueur1 == "roi_coeur" :
				power_joueur1 = 14
			elif carte_joueur2 == "roi_coeur" : 
				power_joueur2 = 14
			elif carte_joueur1 == "as_coeur" : 
				power_joueur1 = 15
			elif carte_joueur2 == "as_coeur" :
				power_joueur2 = 15
			elif carte_joueur1 == "dix_coeur" :
				power_joueur1 = 16
			elif carte_joueur2 == "dix_coeur" :
				power_joueur2 = 16
			elif carte_joueur1 == "sept_carreau" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_carreau" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_carreau" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_carreau" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_carreau" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_carreau" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_carreau" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_carreau" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_carreau" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_carreau" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_carreau" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_carreau" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_carreau" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_carreau" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_carreau" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_carreau" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_trefle" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_trefle" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_trefle" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_trefle" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_trefle" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_trefle" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_trefle" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_trefle" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_trefle" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_trefle" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_trefle" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_trefle" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_trefle" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_trefle" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_trefle" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_trefle" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_pique" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_pique" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_pique" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_pique" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_pique" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_pique" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_pique" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_pique" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_pique" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_pique" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_pique" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_pique" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_pique" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_pique" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_pique" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_pique" :
				power_joueur2 = 8
		elif self.atout == 2 : #Si l'atout est carreau
			if power_joueur1 == "sept_coeur" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_coeur" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_coeur" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_coeur" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_coeur" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_coeur" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_coeur" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_coeur" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_coeur" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_coeur" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_coeur" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_coeur" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_coeur" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_coeur" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_coeur" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_coeur" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_carreau" : 
				power_joueur1 = 9
			elif carte_joueur2 == "sept_carreau" : 
				power_joueur2 = 9
			elif carte_joueur1 == "huit_carreau" :
				power_joueur1 = 10
			elif carte_joueur2 == "huit_carreau" :
				power_joueur2 = 10
			elif carte_joueur1 == "neuf_carreau" :
				power_joueur1 = 11
			elif carte_joueur2 == "neuf_carreau" : 
				power_joueur2 = 11
			elif carte_joueur1 == "valet_carreau" : 
				power_joueur1 = 12
			elif carte_joueur2 == "valet_carreau" :
				power_joueur2 = 12
			elif carte_joueur1 == "dame_carreau" : 
				power_joueur1 = 13
			elif carte_joueur2 == "dame_carreau" :
				power_joueur2 = 13
			elif carte_joueur1 == "roi_carreau" :
				power_joueur1 = 14
			elif carte_joueur2 == "roi_carreau" : 
				power_joueur2 = 14
			elif carte_joueur1 == "as_carreau" : 
				power_joueur1 = 15
			elif carte_joueur2 == "as_carreau" :
				power_joueur2 = 15
			elif carte_joueur1 == "dix_carreau" :
				power_joueur1 = 16
			elif carte_joueur2 == "dix_carreau" :
				power_joueur2 = 16
			elif carte_joueur1 == "sept_trefle" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_trefle" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_trefle" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_trefle" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_trefle" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_trefle" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_trefle" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_trefle" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_trefle" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_trefle" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_trefle" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_trefle" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_trefle" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_trefle" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_trefle" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_trefle" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_pique" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_pique" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_pique" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_pique" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_pique" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_pique" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_pique" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_pique" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_pique" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_pique" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_pique" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_pique" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_pique" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_pique" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_pique" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_pique" :
				power_joueur2 = 8

		elif self.atout == 3 : #Si l'atout est trèfle
			if power_joueur1 == "sept_coeur" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_coeur" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_coeur" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_coeur" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_coeur" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_coeur" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_coeur" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_coeur" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_coeur" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_coeur" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_coeur" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_coeur" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_coeur" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_coeur" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_coeur" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_coeur" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_carreau" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_carreau" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_carreau" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_carreau" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_carreau" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_carreau" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_carreau" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_carreau" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_carreau" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_carreau" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_carreau" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_carreau" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_carreau" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_carreau" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_carreau" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_carreau" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_trefle" : 
				power_joueur1 = 9
			elif carte_joueur2 == "sept_trefle" : 
				power_joueur2 = 9
			elif carte_joueur1 == "huit_trefle" :
				power_joueur1 = 10
			elif carte_joueur2 == "huit_trefle" :
				power_joueur2 = 10
			elif carte_joueur1 == "neuf_trefle" :
				power_joueur1 = 11
			elif carte_joueur2 == "neuf_trefle" : 
				power_joueur2 = 11
			elif carte_joueur1 == "valet_trefle" : 
				power_joueur1 = 12
			elif carte_joueur2 == "valet_trefle" :
				power_joueur2 = 12
			elif carte_joueur1 == "dame_trefle" : 
				power_joueur1 = 13
			elif carte_joueur2 == "dame_trefle" :
				power_joueur2 = 13
			elif carte_joueur1 == "roi_trefle" :
				power_joueur1 = 14
			elif carte_joueur2 == "roi_trefle" : 
				power_joueur2 = 14
			elif carte_joueur1 == "as_trefle" : 
				power_joueur1 = 15
			elif carte_joueur2 == "as_trefle" :
				power_joueur2 = 15
			elif carte_joueur1 == "dix_trefle" :
				power_joueur1 = 16
			elif carte_joueur2 == "dix_trefle" :
				power_joueur2 = 16
			elif carte_joueur1 == "sept_pique" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_pique" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_pique" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_pique" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_pique" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_pique" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_pique" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_pique" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_pique" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_pique" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_pique" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_pique" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_pique" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_pique" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_pique" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_pique" :
				power_joueur2 = 8

		elif self.atout == 4 : #Si l'atout est pique
			if power_joueur1 == "sept_coeur" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_coeur" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_coeur" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_coeur" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_coeur" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_coeur" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_coeur" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_coeur" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_coeur" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_coeur" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_coeur" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_coeur" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_coeur" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_coeur" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_coeur" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_coeur" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_carreau" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_carreau" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_carreau" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_carreau" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_carreau" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_carreau" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_carreau" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_carreau" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_carreau" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_carreau" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_carreau" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_carreau" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_carreau" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_carreau" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_carreau" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_carreau" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_trefle" : 
				power_joueur1 = 1
			elif carte_joueur2 == "sept_trefle" : 
				power_joueur2 = 1
			elif carte_joueur1 == "huit_trefle" :
				power_joueur1 = 2
			elif carte_joueur2 == "huit_trefle" :
				power_joueur2 = 2
			elif carte_joueur1 == "neuf_trefle" :
				power_joueur1 = 3
			elif carte_joueur2 == "neuf_trefle" : 
				power_joueur2 = 3
			elif carte_joueur1 == "valet_trefle" : 
				power_joueur1 = 4
			elif carte_joueur2 == "valet_trefle" :
				power_joueur2 = 4
			elif carte_joueur1 == "dame_trefle" : 
				power_joueur1 = 5
			elif carte_joueur2 == "dame_trefle" :
				power_joueur2 = 5
			elif carte_joueur1 == "roi_trefle" :
				power_joueur1 = 6
			elif carte_joueur2 == "roi_trefle" : 
				power_joueur2 = 6
			elif carte_joueur1 == "as_trefle" : 
				power_joueur1 = 7
			elif carte_joueur2 == "as_trefle" :
				power_joueur2 = 7
			elif carte_joueur1 == "dix_trefle" :
				power_joueur1 = 8
			elif carte_joueur2 == "dix_trefle" :
				power_joueur2 = 8
			elif carte_joueur1 == "sept_pique" : 
				power_joueur1 = 9
			elif carte_joueur2 == "sept_pique" : 
				power_joueur2 = 9
			elif carte_joueur1 == "huit_pique" :
				power_joueur1 = 10
			elif carte_joueur2 == "huit_pique" :
				power_joueur2 = 10
			elif carte_joueur1 == "neuf_pique" :
				power_joueur1 = 11
			elif carte_joueur2 == "neuf_pique" : 
				power_joueur2 = 11
			elif carte_joueur1 == "valet_pique" : 
				power_joueur1 = 12
			elif carte_joueur2 == "valet_pique" :
				power_joueur2 = 12
			elif carte_joueur1 == "dame_pique" : 
				power_joueur1 = 13
			elif carte_joueur2 == "dame_pique" :
				power_joueur2 = 13
			elif carte_joueur1 == "roi_pique" :
				power_joueur1 = 14
			elif carte_joueur2 == "roi_pique" : 
				power_joueur2 = 14
			elif carte_joueur1 == "as_pique" : 
				power_joueur1 = 15
			elif carte_joueur2 == "as_pique" :
				power_joueur2 = 15
			elif carte_joueur1 == "dix_pique" :
				power_joueur1 = 16
			elif carte_joueur2 == "dix_pique" :
				power_joueur2 = 16
		verification = Tour(kijou = 0, atout = self.atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 2, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
		verification.battle(carte_terrain = 0, power_joueur1 = power_joueur1, power_joueur2 = power_joueur2, check = 1)




