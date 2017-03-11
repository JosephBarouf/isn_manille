from root import root

jeu = root()
print("=================PyManille=================\n")

print(type(jeu))
while True:
	r = 0
	while(r!=1 and r!=2):
			r = int(input("\
1: Créer un compte\n\
2: Lister les compte\n"))

	if(r == 1):
		jeu.creerCompte()
	elif(r == 2):
		jeu.listerCompte()
	elif (r == 3):
		print ("Lancement du jeu")