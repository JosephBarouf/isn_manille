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

from random import choice
from Classe_Carte import Carte
carte_main_joueur1 = []
carte_hide_joueur1 = []
carte_show_joueur1 = []
carte_main_joueur2 =[]
carte_hide_joueur2 =[]
carte_show_joueur2 =[]


class JeuDeCarte : 
	"""Definition de la classe JeuDeCarte"""
	def __init__(self, nbr_cartes = 32, atout = "coeur") :
		"""Initialisation de la classe JeuDeCarte"""
		self.nbr_cartes = nbr_cartes
		self.atout = atout

	def cartes(self) : 
		"""Répertorie toute les cartes du jeu et les stocke dnas une liste"""
		As_coeur = Carte(valeur = 1, couleur = "coeur", nom = "As_coeur")
		Roi_coeur = Carte(valeur = 13, couleur = "coeur", nom = "Roi_coeur")
		Dame_coeur = Carte(valeur = 12, couleur = "coeur", nom = "Dame_coeur")
		Valet_coeur = Carte(valeur = 11, couleur = "coeur", nom = "Valet_coeur")
		dix_coeur = Carte(valeur = 10, couleur = "coeur", nom = "Dix_coeur")
		neuf_coeur = Carte(valeur = 9, couleur = "coeur", nom = "Neuf_coeur")
		huit_coeur = Carte(valeur = 8, couleur = "coeur", nom = "Huit_coeur")
		sept_coeur = Carte(valeur = 7, couleur = "coeur", nom = "Sept_coeur")
		As_carreau = Carte(valeur = 1, couleur = "carreau", nom = "As_carreau")
		Roi_carreau = Carte(valeur = 13, couleur = "carreau", nom = "Roi_carreau")
		Dame_carreau = Carte(valeur = 12, couleur = "carreau", nom = "Dame_carreau")
		Valet_carreau = Carte(valeur = 11, couleur = "carreau", nom = "Valet_carreau")
		dix_carreau = Carte(valeur = 10, couleur = "carreau", nom = "Dix_carreau")
		neuf_carreau = Carte(valeur = 9, couleur = "carreau", nom = "Neuf_carreau")
		huit_carreau = Carte(valeur = 8, couleur = "carreau", nom = "Huit_carreau")
		sept_carreau = Carte(valeur = 7, couleur = "carreau", nom = "Sept_carreau")
		As_trefle = Carte(valeur = 1, couleur = "trefle", nom = "As_trefle")
		Roi_trefle = Carte(valeur = 13, couleur = "trefle", nom = "Roi_trefle")
		Dame_trefle = Carte(valeur = 12, couleur = "trefle", nom = "Dame_trefle")
		Valet_trefle = Carte(valeur = 11, couleur = "trefle", nom = "Valet_trefle")
		dix_trefle = Carte(valeur = 10, couleur = "trefle", nom = "Dix_trefle")
		neuf_trefle = Carte(valeur = 9, couleur = "trefle", nom = "Neuf_trefle")
		huit_trefle = Carte(valeur = 8, couleur = "trefle", nom = "Huit_trefle")
		sept_trefle = Carte(valeur = 7, couleur = "trefle", nom = "Sept_trefle")
		As_pique = Carte(valeur = 1, couleur = "pique", nom = "As_pique")
		Roi_pique = Carte(valeur = 13, couleur = "pique", nom = "Roi_pique")
		Dame_pique = Carte(valeur = 12, couleur = "pique", nom = "Dame_pique")
		Valet_pique = Carte(valeur = 11, couleur = "pique", nom = "Valet_pique")
		dix_pique = Carte(valeur = 10, couleur = "pique", nom = "Dix_pique")
		neuf_pique = Carte(valeur = 9, couleur = "pique", nom = "Neuf_pique")
		huit_pique = Carte(valeur = 8, couleur = "pique", nom = "Huit_pique")
		sept_pique = Carte(valeur = 7, couleur = "pique", nom = "Sept_pique")
		cartes = [As_coeur, Roi_coeur, Dame_coeur, Valet_coeur, dix_coeur, neuf_coeur, huit_coeur, sept_coeur,As_carreau, Roi_carreau, Dame_carreau, Valet_carreau, dix_carreau, neuf_carreau, huit_carreau,sept_carreau,As_trefle, Roi_trefle, Dame_trefle, Valet_trefle, dix_trefle, neuf_trefle, huit_trefle,sept_trefle,As_pique, Roi_pique, Dame_pique, Valet_pique, dix_pique, neuf_pique, huit_pique, sept_pique]
		return cartes
	def distribuer(self) : 
		"""Distibue équitablement les cartes entre chaque joueur"""
		l_cartes = self.cartes()
		x = 0 #variable permettant de choisir une carte aléatoirement dans l_cartes
		i = 0 #Compte le nombre de cartes distribuées dans la main de chaque joueur
		j = 0 #Compte le nombre de carte hide distribuée
		k = 0 #Compte le nombre de carte shox distribuée
		z = 0 #Variable comptant le nombre de joueur servi
		while i < 16 : #Boucle jusqu'à ce que chaque joueur ai 8 cartes dans sa main
			x = l_cartes.index(choice(l_cartes))
			carte_main_joueur1.append(l_cartes[x])
			i = i + 1
			del l_cartes[x]
			x = l_cartes.index(choice(l_cartes))
			carte_main_joueur2.append(l_cartes[x])
			i = i + 1
			del l_cartes[x]
		while j < 8 :  #Boucle jusqu'à ce que chaque joueur est 4 cartes caché face à lui
			x = l_cartes.index(choice(l_cartes))
			carte_hide_joueur1.append(l_cartes[x])
			j = j + 1
			del l_cartes[x]
			x = l_cartes.index(choice(l_cartes))
			carte_hide_joueur2.append(l_cartes[x])
			j = j + 1
			del l_cartes[x]
		while k < 8 :  #Boucle jusqu'à ce que chaque joueur est 4 cartes caché face à lui
			x = l_cartes.index(choice(l_cartes))
			carte_show_joueur1.append(l_cartes[x])
			k = k + 1
			del l_cartes[x]
			x = l_cartes.index(choice(l_cartes))
			carte_show_joueur2.append(l_cartes[x])
			k = k + 1
			del l_cartes[x]
		"""while z < 2 : #Boucle jusqu'à ce que tout les joueurs puissent voir leur main
			print("Carte main joueur 1 : ")
			for l in carte_main_joueur1 :
				print(l.nom)
			z = z + 1
			print("Carte show joueur 1 : ")
			for l in carte_show_joueur1 :
				print(l.nom)
			z = z + 1
			print("Carte hide joueur 1 : ")
			for l in carte_hide_joueur1 :
				print(l.nom)
			z = z + 1
			print("Carte main joueur 2 : ")
			for l in carte_main_joueur2 :
				print(l.nom)
			z = z + 1
			print("Carte show joueur 2 : ")
			for l in carte_show_joueur2 :
				print(l.nom)
			z = z + 1
			print("Carte hide joueur 2 : ")
			for l in carte_hide_joueur2 :
				print(l.nom)
			z = z + 1"""
	def atout (self) : 
		"""Permet d'attribuer les caractéristiques des cartes de la couleur de l'atout"""


tour1 = JeuDeCarte()
tour1.distribuer()






"""l_cartes = self.cartes()
		x = 0
		if (self.nbr_joueur) == 4 :
			while  len(carte_joueur1) - 1 < (len(l_cartes))/(4) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur1.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 1 : ")
			for i in carte_joueur1 :
				print(i.nom)

			while len(carte_joueur2) < (len(l_cartes))/(4) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur2.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 2 : ")
			for i in carte_joueur2 :
					print(i.nom)
			while  len(carte_joueur3) < (len(l_cartes))/(4) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur3.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 3 : ")
			for i in carte_joueur3 :
					print(i.nom)
			while len(carte_joueur4) < (len(l_cartes))/(4) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur4.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 4 : ")
			for i in carte_joueur4 :
					print(i.nom)
		else : 
			while  len(carte_joueur1) - 1 < (len(l_cartes))/(2) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur1.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 1")
			for i in carte_joueur1 :
					print(i.nom)
			while len(carte_joueur2) - 1 < (len(l_cartes))/(2) :
				x = l_cartes.index(choice(l_cartes))
				carte_joueur2.append(l_cartes[x])
				del l_cartes[x]
			print("Main Joueur 2")
			for i in carte_joueur2 :
					print(i.nom)"""





