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

class Tour : 
	"""Classe organisant le déroulement d'un tour"""
	def __init__(self, kijou,first_joueur, decount) : 
		self.kijou = kijou
		self.first_joueur = first_joueur
		self.decount = decount

	def whoBegin(self) :
		if self.first_joueur == 1 :
			self.joueCarte(joueur = J1)
		else : 
			self.joueCarte(joueur = J2)
	def joueCarte(self, joueur) :
		if self.decount == 0 :
			joueur = Joueur() #on va chercher la main du joueur en question dans la classe joueur
			joueur.afficherCarteMainJoueur(joueur = joueur)
			joueur.afficherCarteShowJoueur(joueur = joueur)
		#elif 0 < self.decount < 60 :





