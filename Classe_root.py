#-------------------------------------------------------------------------------
# Name:        Classe_root.py
# Purpose:
#
# Author:		JosephVPetit
#
# Created:     15/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------
from Classe_Joueur import Joueur
from Classe_Manche import Manche
from random import randint

class root :
	"""docstring for root"""
	def __init__(self) :
		"""Initialisation de la classe root"""
		self.compte = []

	def listerCompte(self) :
		"""Permet d'afficher tout les comptes actuels"""
		if self.compte:
			print("\nVoici le nom des comptes crée(s):\n") #Tip reseau : Les conditions qui suivent sur une autre page.
			for compte in self.compte:
				print("- " + compte)
			print("\n\n")
		else:
			print("\nAucun compte n'existe\n")
	
	def creerCompte(self) :
		"""Permet de crer un compte"""
		name = input("\n\
Quel est le nom du joueur ?\n")		#Tip reseau : Peut etre même page que lister compte
		self.compte.append(name)
		self.listerCompte()
	
	def startGame(self) :
		"""Permet de débuter le jeu (à completer par l'enchainement d'une suite de classe)"""
		print("\nDébut du jeu\n") #Tip reseau et affichage : Petite animation sur la page de jeu avec debut du jeu qui s'annonce. Genre street fighter
		nom_joueur1 = str(input("\nLe joueur 1 entre son pseudo pour cette partie\n"))
		nom_joueur2 = str(input("\nLe joueur 2 entre son pseudo pour cette partie\n"))
		dealer = randint(1,2)
		decount = 0
		cartes = 0
		carte_main_joueur1 = 0 
		carte_main_joueur2 = 0 
		carte_show_joueur1 = 0 
		carte_show_joueur1 = 0
		carte_show_joueur2 = 0
		carte_hide_joueur1 = 0
		carte_hide_joueur2 = 0
		if dealer == 1 :
			dealer = Manche(bouton_press = str(input("{0}, vous êtes dealer.\n S'il vous plait, press enter".format(nom_joueur1))), kijou = 1, nom_joueur1 = nom_joueur1, nom_joueur2 = nom_joueur2, decount = decount, carte_main_joueur1 = carte_main_joueur1, carte_main_joueur2 = carte_main_joueur2, carte_show_joueur1 = carte_show_joueur1, carte_show_joueur2 = carte_show_joueur2, carte_hide_joueur1 = carte_hide_joueur1, carte_hide_joueur2 = carte_hide_joueur2)
			dealer.prepareManche()
		else :
			dealer = Manche(bouton_press = str(input("{0}, vous êtes dealer.\n S'il vous plait, press enter".format(nom_joueur2))), kijou = 2, nom_joueur1 = nom_joueur1, nom_joueur2 = nom_joueur2, decount = decount, carte_main_joueur1 = carte_main_joueur1, carte_main_joueur2 = carte_main_joueur2, carte_show_joueur1 = carte_show_joueur1, carte_show_joueur2 = carte_show_joueur2, carte_hide_joueur1 = carte_hide_joueur1, carte_hide_joueur2 = carte_hide_joueur2)
			dealer.prepareManche()



