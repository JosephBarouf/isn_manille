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
from random import random

class Joueur : 
	"""Classe permettant de créer les joueurs de la partie"""

	def __init__(self, nom_joueur, carte_show_joueur, carte_hide_joueur) :
		score = 0
		self.nom_joueur = nom_joueur
		self.score = score

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
		self.afficherCarteMainJoueur(carte_main_joueur1, carte_main_joueur2) #Envoie les carte contenue dans la main de chaque joueur à afficherCarteMainJoueur


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
		self.afficherCarteShowJoueur(carte_show_joueur1, carte_show_joueur2) #Envoie les cartes show de chaque joueur à la classe afficher cartes show

	def afficherCarteMainJoueur(self, carte_main_joueur1, carte_main_joueur2, joueur) :
		if joueur == J1 : #Vérifie qui est le joueur qui va voir ses carte en mains
			print("Cartes de votre main : {0}".format(carte_main_joueur1))
		else : 
			print("Cartes de votre main : {0}".format(carte_main_joueur2))



	def afficherCarteShowJoueur(self, joueur) :
		if joueur == J1 :  #Vérifie qui est le joueur qui va voir ses cartes show
			print("Vos cartes show : {0}".format(carte_show_joueur1))
		else : 
			print("Vos cartes show : {0}".format(carte_show_joueur2))


	"""def dealer(self) :
		x = 0 #x est la variable permettant de choisir un premier dealer aléatoirement
		x = randint(1,2)
		if x == 1 : """

