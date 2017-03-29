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

class root :
	"""docstring for root"""
	def __init__(self) :
		"""Initialisation de la classe root"""
		self.compte = []

	def listerCompte(self) :
		"""Permet d'afficher tout les comptes actuels"""
		if self.compte:
			print("\nVoici le nom des comptes crée(s):\n")
			for compte in self.compte:
				print("- " + compte)
			print("\n\n")
		else:
			print("\nAucun compte n'existe\n")
	
	def creerCompte(self) :
		"""Permet de crer un compte"""
		name = input("\n\
Quel est le nom du joueur ?\n")
		self.compte.append(name)
		self.listerCompte()
	
	def startGame(self) :
		"""Permet de débuter le jeu (à completer par l'enchainement d'une suite de classe)"""
		print("\nDébut du jeu\n")
		J1 = Joueur(str(input("\nLe joueur 1 entre son pseudo pour cette partie\n")))
		J2 = Joueur(str(input("\nLe joueur 2 entre son pseudo pour cette partie\n")))
		dealer = randint(1,2)
		decount = 0
		if dealer == 1 :
			dealer = Manche()
			dealer.startManche(bouton_press = str(input("Joueur 1, vous êtes dealer.\n S'il vous plait, appuyez sur entrer")), first_joueur = J1, decount = decount)
		else :
			dealer = Manche()
			dealer.startManche(bouton_press = str(input("Joueur 2, vous êtes dealer.\n S'il vous plait, appuyez sur entrer")), nfirst_joueur = J2, decount = decount)



