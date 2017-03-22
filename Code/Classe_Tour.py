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
	"""Classe organisans le déroulement d'un tour"""
	def __init__(self, dealer) : 
		self.dealer = dealer

	def whoBegin(self) :
		if self.dealer == 1 : 
			J1.joueCarte()
		else : 
			J2.joueCarte()
	def joueCarte(self) : 
		

