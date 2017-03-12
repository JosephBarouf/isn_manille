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
	def __init__(self, valeur, couleur, nom) :
		"""Initialisation de la classe carte"""
		self.nom = nom
		self.valeur = valeur
		self.couleur = couleur