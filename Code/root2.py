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
	
	def start(self) :
		"""Permet de débuter le jeu (à completer par l'enchainement d'une suite de classe)"""
		print("\nDébut du jeu\n")
