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

class Joueur : 
	"""Classe permettant de créer les joueurs de la partie"""

	def __init__(self, nom_joueur) :
		score = 0
		self.nom_joueur = nom_joueur
		self.score = score