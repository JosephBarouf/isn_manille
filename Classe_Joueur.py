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
from random import *
from Classe_JeuDeCarte import JeuDeCarte
from Classe_Carte import Carte
from Classe_Tour import Tour

class Joueur : 
	"""Classe permettant de créer les joueurs de la partie"""

	def __init__(self, kijou, nom_joueur1, nom_joueur2, decount, score, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) :
		score = 0
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.kijou = kijou
		self.decount = decount
		self.score = score
		self.carte_main_joueur1 = carte_main_joueur1 
		self.carte_main_joueur2 = carte_main_joueur2 
		self.carte_show_joueur1 = carte_show_joueur1 
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1 
		self.carte_hide_joueur2 = carte_hide_joueur2

	def cartes(self) : 
		"""Je crois que je ne m'en sert plus finalement"""
		"""Répertorie toute les cartes du jeu et les stockent dans une liste"""
		As_coeur = Carte(couleur = 1, nom = "As_coeur") 			#couleur : 1 pour coeur 2 pour carreau 3 pour trèfle, 4 pour pique
		Roi_coeur = Carte(couleur = 1, nom = "Roi_coeur")
		Dame_coeur = Carte(couleur = 1, nom = "Dame_coeur")
		Valet_coeur = Carte(couleur = 1, nom = "Valet_coeur")
		dix_coeur = Carte(couleur = 1, nom = "Dix_coeur")
		neuf_coeur = Carte(couleur = 1, nom = "Neuf_coeur")
		huit_coeur = Carte(couleur = 1, nom = "Huit_coeur")
		sept_coeur = Carte(couleur = 1, nom = "Sept_coeur")
		As_carreau = Carte(couleur = 2, nom = "As_carreau")
		Roi_carreau = Carte(couleur = 2, nom = "Roi_carreau")
		Dame_carreau = Carte(couleur = 2, nom = "Dame_carreau")
		Valet_carreau = Carte(couleur = 2, nom = "Valet_carreau")
		dix_carreau = Carte(couleur = 2, nom = "Dix_carreau")
		neuf_carreau = Carte(couleur = 2, nom = "Neuf_carreau")
		huit_carreau = Carte(couleur = 2, nom = "Huit_carreau")
		sept_carreau = Carte(couleur = 2, nom = "Sept_carreau")
		As_trefle = Carte(couleur = 3, nom = "As_trefle")
		Roi_trefle = Carte(couleur = 3, nom = "Roi_trefle")
		Dame_trefle = Carte(couleur = 3, nom = "Dame_trefle")
		Valet_trefle = Carte(couleur = 3, nom = "Valet_trefle")
		dix_trefle = Carte(couleur = 3, nom = "Dix_trefle")
		neuf_trefle = Carte(couleur = 3, nom = "Neuf_trefle")
		huit_trefle = Carte(couleur = 3, nom = "Huit_trefle")
		sept_trefle = Carte(couleur = 3, nom = "Sept_trefle")
		As_pique = Carte(couleur = 4, nom = "As_pique")
		Roi_pique = Carte(couleur = 4, nom = "Roi_pique")
		Dame_pique = Carte(couleur = 4, nom = "Dame_pique")
		Valet_pique = Carte(couleur = 4, nom = "Valet_pique")
		dix_pique = Carte(couleur = 4, nom = "Dix_pique")
		neuf_pique = Carte(couleur = 4, nom = "Neuf_pique")
		huit_pique = Carte(couleur = 4, nom = "Huit_pique")
		sept_pique = Carte(couleur = 4, nom = "Sept_pique")
		cartes = [As_coeur, Roi_coeur, Dame_coeur, Valet_coeur, dix_coeur, neuf_coeur, huit_coeur, sept_coeur,As_carreau, Roi_carreau, Dame_carreau, Valet_carreau, dix_carreau, neuf_carreau, huit_carreau,sept_carreau,As_trefle, Roi_trefle, Dame_trefle, Valet_trefle, dix_trefle, neuf_trefle, huit_trefle,sept_trefle,As_pique, Roi_pique, Dame_pique, Valet_pique, dix_pique, neuf_pique, huit_pique, sept_pique]
		return cartes

	def distribuer(self) : 
		"""Distibue équitablement les cartes entre chaque joueur"""
		from Classe_Manche import Manche
		l_cartes = ["as_coeur", "roi_coeur", "dame_coeur", "valet_coeur", "dix_coeur", "neuf_coeur", "huit_coeur", "sept_coeur", "as_carreau", "roi_carreau", "dame_carreau", "valet_carreau", "dix_carreau", "neuf_carreau", "huit_carreau", "sept_carreau", "as_trefle", "roi_trefle", "dame_trefle", "valet_trefle", "dix_trefle", "neuf_trefle", "huit_trefle", "sept_trefle", "as_pique", "roi_pique", "dame_pique", "valet_pique", "dix_pique", "neuf_pique", "huit_pique", "sept_pique"]
		carte_main_joueur1 = []
		carte_main_joueur2 = []
		carte_show_joueur1 = []
		carte_show_joueur2 = []
		carte_hide_joueur1 = []
		carte_hide_joueur2 = []
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
		game_ready = Manche(bouton_press = 0, kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, carte_show_joueur1 = carte_show_joueur1, carte_show_joueur2 = carte_show_joueur2, carte_main_joueur1 = carte_main_joueur1, carte_main_joueur2 = carte_main_joueur2, carte_hide_joueur1 = carte_hide_joueur1, carte_hide_joueur2 = carte_hide_joueur2) #Envoie les cartes show de chaque joueur à la classe afficher cartes show
		game_ready.startManche()

	def afficherCarteMainJoueur(self) :
		if self.kijou == 1 : #Vérifie qui est le joueur qui va voir ses carte en mains
			print("Carte main de {0} : ".format(self.nom_joueur1))
			for k in self.carte_main_joueur1 :
				print(k)
		else :
			print("Carte main de {0} : ".format(self.nom_joueur2))
			for k in self.carte_main_joueur2 :
				print(k)

	def afficherCarteShowJoueur(self) :
		if self.kijou == 1 :  #Vérifie qui est le joueur qui va voir ses cartes show
			print("Carte show de {0} : ".format(self.nom_joueur1))
			for k in self.carte_show_joueur1 :
				print(k)
		else : 
			print("Carte show de {0} : ".format(self.nom_joueur2))
			for k in self.carte_show_joueur2 :
				print(k)
	def afficherCarteTerrain(self, carte_terrain) :
		for i in carte_terrain : #Pour l'instant ca suffit, il faudra voir pour qu'à chaque fin de tour les cartes sur le terrain disparaissent
			print(i)

	def atout(self, choix_atout, carte_terrain) :
		if choix_atout == 1 : #Le dealer a choisi coeur
			print("L'atout pour cette manche : Coeur \n")
			atout_ok = Tour(kijou = self.kijou, atout = 1, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			atout_ok.joueCarte(terrain = 0, carte_terrain = carte_terrain)
		elif choix_atout == 2 : #Le dealer a choisi carreau
			print("L'atout pour cette manche : Carreau \n")
			atout_ok = Tour(kijou = self.kijou, atout = 2, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			atout_ok.joueCarte(terrain = 0, carte_terrain = carte_terrain)
		elif choix_atout == 3 : #Le dealer a choisi trèfle
			print("L'atout pour cette manche : Trèfle \n")
			atout_ok = Tour(kijou = self.kijou, atout = 3, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			atout_ok.joueCarte(terrain = 0, carte_terrain = carte_terrain)
		elif choix_atout == 4 : #Le dealer a choisi pique
			print("L'atout pour cette manche : Pique \n")
			atout_ok = Tour(kijou = self.kijou, atout = 4, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			atout_ok.joueCarte(terrain = 0, carte_terrain = carte_terrain)

	def joueCarte(self, terrain, carte_terrain, atout) :
		which_type = 0
		choix_carte = 0
		k = 0
		j = 0
		if self.kijou == 1 :
			print("Cartes mains {0} : \n".format(self.nom_joueur1))
			for i in enumerate(self.carte_main_joueur1) : #Astuce réseau : A afficher sur écran joueur 1
				print(i)
			print("\nCartes show {0} : \n".format(self.nom_joueur1))
			for i in enumerate(self.carte_show_joueur1) : #Astuce réseau : A afficher sur l'écran des 2 joueurs
					print(i)
			which_type = (int(input("\n{0} quel type de carte souhaitez vous utiliser ? \n Press 0 ---> Play carte main \n Press 1 ---> Play carte show \n Press 2 ---> Play carte hide \n ".format(self.nom_joueur1))))
			if which_type == 0 : #Lorsque le joueur veux jouer une carte de sa main
				print("Choisissez messire {0}".format(self.nom_joueur1))
				for i in enumerate(self.carte_main_joueur1) :
					print(i)
				choix_carte = int(input("{0}, quelle carte voulez vous jouer ?".format(self.nom_joueur1))) #Faudra revoir pour que ca redemande lorsque le chiffre n'est pas bon ou qu'on inscrit une chaine de caractère...ect
				print("Vous avez choisi {0} \n".format(self.carte_main_joueur1[choix_carte]))
				carte_terrain.append(self.carte_main_joueur1[choix_carte])
				del self.carte_main_joueur1[choix_carte]
				terrain = terrain + 1
			elif which_type == 1 : #Lorsque le joueur veut jouer une carte show
				print("Choisissez messire {0}".format(self.nom_joueur1))
				for i in enumerate(self.carte_show_joueur1) :
					print(i)
				choix_carte = int(input("{0}, quelle carte voulez vous jouer ?".format(self.nom_joueur1)))
				print("Vous avez choisi {0} \n".format(self.carte_show_joueur1[choix_carte]))
				carte_terrain.append(self.carte_show_joueur1[choix_carte])
				del self.carte_show_joueur1[choix_carte]
				terrain = terrain + 1
			elif which_type == 2 : 
				print("On verra plus tard bonhome stress pas ;)")
			finish = (str(input("\n {0} Appuyez sur entrer pour finir votre tour".format(self.nom_joueur1))))
			while j == 0 :
				if finish == "" :
					j = 1
					after = Tour(kijou = 2, atout = atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 2, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					after.joueCarte(terrain = terrain, carte_terrain = carte_terrain)
				else :
					finish = (str(input("\n {0} S'il vous plait, appuyez sur entrer pour finir votre tour".format(self.nom_joueur1))))
		else :
			print("Cartes mains {0} : \n".format(self.nom_joueur2))
			for i in enumerate(self.carte_main_joueur2) : #Astuce réseau : A afficher sur écran joueur 2
				print(i)
			print("\nCartes show {0} : \n".format(self.nom_joueur2))
			for i in enumerate(self.carte_show_joueur2) : #Astuce réseau : A afficher sur l'écran des 2 joueurs
				print(i)
			which_type = (int(input("\n{0} quel type de carte souhaitez vous utiliser ? \n Press 0 ---> Play carte main \n Press 1 ---> Play carte show \n Press 2 ---> Play carte hide \n ".format(self.nom_joueur2))))
			if which_type == 0 : #Lorsque le joueur veux jouer une carte de sa main
				print("Choisissez messire {0} ".format(self.nom_joueur2))
				for i in enumerate(self.carte_main_joueur2) :
					print(i)
				choix_carte = int(input("{0}, quelle carte voulez vous jouer ?".format(self.nom_joueur2))) #Faudra revoir pour que ca redemande lorsque le chiffre n'est pas bon ou qu'on inscrit une chaine de caractère...ect
				print("Vous avez choisi {0}".format(self.carte_main_joueur2[choix_carte]))
				carte_terrain.append(self.carte_main_joueur2[choix_carte])
				del self.carte_main_joueur2[choix_carte]
				terrain = terrain + 1
			elif which_type == 1 : #Lorsque le joueur veut jouer une carte show
				print("Choisissez messire {0}".format(self.nom_joueur2))
				for i in enumerate(self.carte_show_joueur2) :
					print(i)
				choix_carte = int(input("{0}, quelle carte voulez vous jouer ?".format(self.nom_joueur2)))
				print("Vous avez choisi {0} \n".format(self.carte_show_joueur2[choix_carte]))
				carte_terrain.append(self.carte_show_joueur2[choix_carte])
				del self.carte_show_joueur2[choix_carte]
				terrain = terrain + 1
			elif which_type == 2 : 
				print("On verra plus tard bonhome stress pas ;)")
			finish = (str(input("\n {0} Appuyez sur entrer pour finir votre tour".format(self.nom_joueur2))))
			while j == 0 :
				if finish == "" :
					j = 1
					after = Tour(kijou = 1, atout = atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 2, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					after.joueCarte(terrain = terrain, carte_terrain = carte_terrain)
				else :
					finish = (str(input("\n {0} S'il vous plait, appuyez sur entrer pour finir votre tour".format(self.nom_joueur2))))







