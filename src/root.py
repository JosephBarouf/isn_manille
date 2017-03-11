class root(object):
	"""docstring for root"""
	def __init__(self):
		self.joueurs = []
		r = 0
		while(r!=1 and r!=2):
			r = int(input("\
=====================PyManille==========\n\
1: Inscrire un joueur\n\
2: Lister les joueurs\n"))
		if(r == 1):
			creerJoueur()
		elif(r == 2):
			self.listerJoueurs(self.joueurs)

	def listerJoueurs(self, joueurs):
		if joueurs:
			for joueur in joueurs:
				print(joueur)
