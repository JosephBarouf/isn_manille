class root(object):
	"""docstring for root"""
	def __init__(self):
		self.compte = []

	def listerCompte(self):
		if self.compte:
			print("\nVoici le nom des comptes crée(s):\n")
			for compte in self.compte:
				print("- " + compte)
			print("\n\n")
		else:
			print("\nAucun compte n'existe\n")
		

	def creerCompte(self):
		name = input("\n\
Quel est le nom du joueur ?\n")
		self.compte.append(name)
		self.listerCompte()
