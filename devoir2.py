#coding: utf-8

import csv

fichier = "grants.csv"

f1 =open(fichier,encoding = "utf-8")

lignes = csv.reader(f1)

next(lignes)

liste = []


for subvention in lignes:

	for element in subvention:
		word = element.split()	

		#liste de plusieurs mots 
		for words in word:
			if words.lower() == "périodiques":
				date = subvention[13].split("-")
				result =(str(date[0])+": " + str(subvention))
				liste.append(result)
				
final = list(set(liste))


for x in final:
	print(x)
	print("")
	print("-"*100)
