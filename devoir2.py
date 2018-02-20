#coding: utf-8
import csv
fichier = 'grants.csv'
f1 = open(fichier, encoding = "utf-8")
#j'avais des charmap error alors j'ai demandé au fichier d'encode en utf-8
document = csv.reader(f1)

#on créé nos variables en fonction des 3 programmes du Fonds

editeurs = "Aide aux éditeurs"
innovation = "Innovation commerciale"
initiative = "Initiatives collectives"
n=0



for ligne in document:

#si le programme apparait dans les éléments des listes des subventions, on veut la date et la ligne (subvention)
#j'affiche aussi le programme à part, pour pouvoir ajouter une autre colonne dans le nouveau fichier et les trier selon le programme
		

	if any(editeurs in element for subvention in ligne):
		
		date = ligne[13]
		annee = date.split("-")
		n+=1
		print("-" * 100)
		print(n,annee[0], ligne)
		print(editeurs)
	

	if any(innovation in element for subvention in ligne):

		date = ligne[13]
		annee = date.split("-")
		n+=1
		
		print("-" * 100)
		print(n,annee[0], ligne)
		print(innovation)


	if any(initiative in element for subvention in ligne):
		date = ligne[13]
		annee = date.split("-")
		n+=1
			
		print("-" * 100)
		print(n,annee[0], ligne)
		print(initiative)
