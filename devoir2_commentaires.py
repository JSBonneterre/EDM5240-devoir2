### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8
import csv

### Pour commencer, ici, je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier = '../grants.csv'
f1 = open(fichier, encoding = "utf-8")
#j'avais des charmap error alors j'ai demandé au fichier d'encode en utf-8
document = csv.reader(f1)

#on créé nos variables en fonction des 3 programmes du Fonds

editeurs = "Aide aux éditeurs"
innovation = "Innovation commerciale"
initiative = "Initiatives collectives"
n=0

for subvention in document:

#si le programme apparait dans les éléments des listes des subventions, on veut la date et la ligne (subvention)
#j'affiche aussi le programme à part, pour pouvoir ajouter une autre colonne dans le nouveau fichier et les trier selon le programme
		
#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
	if any(editeurs in element for element in subvention):
		
		date = subvention[13]

### Ingénieux d'utiliser «.split()» pour isoler la date!
### Une autre méthode: «annee = annee[:4]»

		annee = date.split("-")

### Bravo d'avoir pensé mettre le compteur à l'intérieur des conditions pour ne compter que les subventions que tu cherches

		n+=1

### Jolies décorations de ton «output» :)

		print("-" * 100)
		print(n,annee[0], subvention)
		print(editeurs)
	

	if any(innovation in element for element in subvention):

		date = subvention[13]
		annee = date.split("-")
		n+=1
		
		print("-" * 100)
		print(n,annee[0], subvention)
		print(innovation)


	if any(initiative in element for element in subvention):
		date = subvention[13]
		annee = date.split("-")
		n+=1
			
		print("-" * 100)
		print(n,annee[0], subvention)
		print(initiative)

### Cet enchaînement de conditions faisait en sorte que tu n'obtenais pas tout à fait les bonnes subventions
### Certaines «Initiatives collectives» ne concernent pas le Fonds du Canada pour les périodiques et touchent plutôt le monde du livre
### Résultat, tu obtiens 4844 subventions.
### La solution, un seul «if», mais avec un «or»:
### «if "Fonds du Canada pour les périodiques" in subvention[17] or "FCP -" in subvention[17]:»
### t'en donne 4608.