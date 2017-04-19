 #-------------------------------------------------------------------------------
# Name:        Classe_main.py
# Purpose:
#
# Author:		JosephVPetit
#
# Created:     15/03/2017
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

from random import *

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
class Tour : 
	"""Classe organisant le déroulement d'un tour"""
	def __init__(self, kijou, atout, nom_joueur1, nom_joueur2, decount, tour, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) : 
		self.kijou = kijou
		self.atout = atout
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.decount = decount
		self.tour = tour
		self.carte_main_joueur1 = carte_main_joueur1
		self.carte_main_joueur2 = carte_main_joueur2
		self.carte_show_joueur1 = carte_show_joueur1
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1
		self.carte_hide_joueur2 = carte_hide_joueur2

	def joueCarte(self, terrain, carte_terrain) :
		from Classe_Joueur import Joueur
		while self.decount < 60 :
			if self.tour == 1 :
				#Cette condition est peut etre à mettre dans un autre méthode correspondant à choisir l'atout. 
				if self.kijou == 1 :
					voir = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2) #on va chercher la main du joueur en question dans la classe joueur
					voir.afficherCarteMainJoueur()
					voir.afficherCarteShowJoueur()
					choose_atout = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					choose_atout.atout(choix_atout = int(input("{0}, choisissez l'atout : \n 1 --> coeur \n 2 --> carreau \n 3 --> trèfle \n 4 --> pique\n".format(self.nom_joueur1))), carte_terrain = carte_terrain)
				else :
					voir = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2) #on va chercher la main du joueur en question dans la classe joueur
					voir.afficherCarteMainJoueur()
					voir.afficherCarteShowJoueur()
					choose_atout = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					choose_atout.atout(choix_atout = int(input("{0}, choisissez l'atout : \n 1 --> coeur \n 2 --> carreau \n 3 --> trèfle \n 4 --> pique\n".format(self.nom_joueur2))), carte_terrain = carte_terrain) #Choix de l'atout par le dealer qui mène à une initialisation de la puissance de chaque cartes
			else :
				if terrain == 2 : #Vérifie si les deux joueurs ont joué ou non
					print("\n Les deux joueurs ont sélectionné leurs cartes ! \n")
					afficher_terrain = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
					afficher_terrain.afficherCarteTerrain(carte_terrain = carte_terrain)
					battle = self.battle(carte_terrain = carte_terrain, power_joueur1 = 0, power_joueur2 = 0, check = 0)
				else : #Lorsque tout les joueurs n'ont pas selectionné leur carte
					if self.kijou == 1 :
						print("{0}, c'est à vous de jouer".format(self.nom_joueur1))
						jouer = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
						jouer.joueCarte(terrain = terrain, carte_terrain = carte_terrain, atout = self.atout)
					else :
						print("{0}, c'est à vous de jouer".format(self.nom_joueur2))
						jouer = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self. nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
						jouer.joueCarte(terrain = terrain, carte_terrain = carte_terrain, atout = self.atout)

		#elif 0 < self.decount < 60 :
	def battle(self, carte_terrain, power_joueur1, power_joueur2, check) :
		if check == 0 :
			carte_joueur1 = ""
			carte_joueur2 = ""
			if self.kijou == 1 : #Si le dernier joueur à avoir joué est le joueur 1
				carte_joueur1 = carte_terrain[1]
				carte_joueur2 = carte_terrain[0]
			else : #Si le dernier joueur à avoir joué est le joueur 2
				carte_joueur1 = carte_terrain[0]
				carte_joueur2 = carte_terrain[1]
			valeur = Carte(atout = self.atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			valeur.powerOn(carte_joueur1 = carte_joueur1, carte_joueur2 = carte_joueur2)
		else :
			if power_joueur1 < power_joueur2 : 
				print("\n {0} remporte ce tour ! \n".format(self.nom_joueur2))
			elif power_joueur1 > power_joueur2 : 
				print("\n {0} remporte ce tour ! \n".format(self.nom_joueur1))
			else : 
				print("Egalité") #revoir les règles, je ne sais plus ce qu'il se passe quand il y a égalité
		terrain = 0
		carte_terrain = []
		debut_tour = Tour(kijou = self.kijou, atout = self.atout, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 2, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self. carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self. carte_hide_joueur2)
		debut_tour.joueCarte(terrain = terrain, carte_terrain = carte_terrain)

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

class Manche : 
	def __init__ (self, bouton_press, kijou, nom_joueur1, nom_joueur2, decount, carte_main_joueur1, carte_main_joueur2, carte_show_joueur1, carte_show_joueur2, carte_hide_joueur1, carte_hide_joueur2) :
		self.bouton_press = bouton_press
		self.kijou = kijou
		self.nom_joueur1 = nom_joueur1
		self.nom_joueur2 = nom_joueur2
		self.decount = decount
		self.carte_main_joueur1 = carte_main_joueur1
		self.carte_main_joueur2 = carte_main_joueur2
		self.carte_show_joueur1 = carte_show_joueur1
		self.carte_show_joueur2 = carte_show_joueur2
		self.carte_hide_joueur1 = carte_hide_joueur1
		self.carte_hide_joueur2 = carte_hide_joueur2

	def prepareManche(self) : 
		from Classe_root import root
		if self.bouton_press == "" :
			distribuer_carte = Joueur(kijou = self.kijou, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, score = 0, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self.carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self.carte_hide_joueur2)
			distribuer_carte.distribuer()
		else : 
			"""problème, ne revient pas dans root.../:"""
			jeu = root()
			print("=================PyManille=================\n")
			while True :
				r = 0
				while(r!=1 and r!=2 and r!=3) :
					r = int(input("\
1: Créer un compte\n\
2: Lister les comptes\n\
3: Start\n"))

				if(r == 1) :
					jeu.creerCompte()
				elif(r == 2) :
					jeu.listerCompte()
				elif (r == 3) :
					jeu.startGame()

	def startManche(self) :
		terrain = 0
		carte_terrain = []
		debut_tour = Tour(kijou = self.kijou, atout = 0, nom_joueur1 = self.nom_joueur1, nom_joueur2 = self.nom_joueur2, decount = self.decount, tour = 1, carte_main_joueur1 = self.carte_main_joueur1, carte_main_joueur2 = self.carte_main_joueur2, carte_show_joueur1 = self.carte_show_joueur1, carte_show_joueur2 = self. carte_show_joueur2, carte_hide_joueur1 = self.carte_hide_joueur1, carte_hide_joueur2 = self. carte_hide_joueur2)
		debut_tour.joueCarte(terrain = terrain, carte_terrain = carte_terrain)

jeu = root()
print("=================PyManille=================\n")

while True :
	r = 0
	while(r!=1 and r!=2 and r!=3) :
			r = int(input("\
1: Créer un compte\n\
2: Lister les comptes\n\
3: Start\n"))

	if(r == 1) :
		jeu.creerCompte()	#Tip reseau : Pour les 3 condition qui suivent faire un genre de menus. Première page d'accueil
	elif(r == 2) :
		jeu.listerCompte()
	elif (r == 3) :
		jeu.startGame()




