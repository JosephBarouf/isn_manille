from random import choice
from ClasseCarte import Carte
carte_joueur1 = []
carte_joueur2 =[]
carte_joueur3 = []
carte_joueur4 =[]

class JeuDeCarte : 
	def __init__(self, nbr_joueur) :
		self.nbr_joueur = nbr_joueur

	def cartes(self) : 
		As_coeur = Carte(valeur = 1, couleur = "coeur")
		Roi_coeur = Carte(valeur = 13, couleur = "coeur")
		Dame_coeur = Carte(valeur = 12, couleur = "coeur")
		Valet_coeur = Carte(valeur = 11, couleur = "coeur")
		dix_coeur = Carte(valeur = 10, couleur = "coeur")
		neuf_coeur = Carte(valeur = 9, couleur = "coeur")
		huit_coeur = Carte(valeur = 8, couleur = "coeur")
		sept_coeur = Carte(valeur = 7, couleur = "coeur")
		As_carreau = Carte(valeur = 1, couleur = "carreau")
		Roi_carreau = Carte(valeur = 13, couleur = "carreau")
		Dame_carreau = Carte(valeur = 12, couleur = "carreau")
		Valet_carreau = Carte(valeur = 11, couleur = "carreau")
		dix_carreau = Carte(valeur = 10, couleur = "carreau")
		neuf_carreau = Carte(valeur = 9, couleur = "carreau")
		huit_carreau = Carte(valeur = 8, couleur = "carreau")
		sept_carreau = Carte(valeur = 7, couleur = "carreau")
		As_trefle = Carte(valeur = 1, couleur = "trefle")
		Roi_trefle = Carte(valeur = 13, couleur = "trefle")
		Dame_trefle = Carte(valeur = 12, couleur = "trefle")
		Valet_trefle = Carte(valeur = 11, couleur = "trefle")
		dix_trefle = Carte(valeur = 10, couleur = "trefle")
		neuf_trefle = Carte(valeur = 9, couleur = "trefle")
		huit_trefle = Carte(valeur = 8, couleur = "trefle")
		sept_trefle = Carte(valeur = 7, couleur = "trefle")
		As_pique = Carte(valeur = 1, couleur = "pique")
		Roi_pique = Carte(valeur = 13, couleur = "pique")
		Dame_pique = Carte(valeur = 12, couleur = "pique")
		Valet_pique = Carte(valeur = 11, couleur = "pique")
		dix_pique = Carte(valeur = 10, couleur = "pique")
		neuf_pique = Carte(valeur = 9, couleur = "pique")
		huit_pique = Carte(valeur = 8, couleur = "pique")
		sept_pique = Carte(valeur = 7, couleur = "pique")
		cartes = [As_coeur, Roi_coeur, Dame_coeur, Valet_coeur, dix_coeur, neuf_coeur, huit_coeur, sept_coeur,As_carreau, Roi_carreau, Dame_carreau, Valet_carreau, dix_carreau, neuf_carreau, huit_carreau,sept_carreau,As_trefle, Roi_trefle, Dame_trefle, Valet_trefle, dix_trefle, neuf_trefle, huit_trefle,sept_trefle,As_pique, Roi_pique, Dame_pique, Valet_pique, dix_pique, neuf_pique, huit_pique, sept_pique]
		return cartes
	def distribuer(self) :
		l_cartes = self.cartes()
		x = 0
		while  len(carte_joueur1) - 1 < (len(l_cartes))/(self.nbr_joueur) :
			x = l_cartes.index(choice(l_cartes))
			carte_joueur1.append(l_cartes[x])
			del l_cartes[x]
		print(carte_joueur1)

		while len(carte_joueur2) - 1 < (len(l_cartes))/(self.nbr_joueur) :
			x = l_cartes.index(choice(l_cartes))
			carte_joueur2.append(l_cartes[x])
			del l_cartes[x]
		print(carte_joueur2)
		while  len(carte_joueur3) - 1 < (len(l_cartes))/(self.nbr_joueur) :
			x = l_cartes.index(choice(l_cartes))
			carte_joueur3.append(l_cartes[x])
			del l_cartes[x]
		print(carte_joueur3)
		while len(carte_joueur4) - 1 < (len(l_cartes))/(self.nbr_joueur) :
			x = l_cartes.index(choice(l_cartes))
			carte_joueur4.append(l_cartes[x])
			del l_cartes[x]
		print(carte_joueur4)
manche1 = JeuDeCarte(nbr_joueur = 4)
manche1.distribuer()
			





