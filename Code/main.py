from root2 import root 

jeu = root()
print("=================PyManille=================\n")

while True:
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
		jeu.start()