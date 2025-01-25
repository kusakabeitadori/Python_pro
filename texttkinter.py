"""
#print("hello")
la_variable = 45
print(la_variable) 

#ETUDE DES LISTES
plateforme = ["Facebook","Instram","Snapchat","Twitter","Whatsapp"]
print("avant le changement de la liste: {plateforme}")
#remplacement de twitter par youtube 
plateforme[3]="Youtube"
print(plateforme)
#ajout de norbert
plateforme.append("norbert")
print(plateforme)
#suppression de snapchat
plateforme.remove("Snapchat")
print(plateforme)
#pour afficher la longueur de ma liste

longueur=len(plateforme)
print(longueur)

s= plateforme.sort()
print(s)
"""
#Etudes des tuples
#caracteriser par les parentheses
#les tuples ne peuvent pas etre modifier
print("hello")

#la boucle for
race_de_chien = ["golden retriever","chihuahua","terrier","carlin"]
for chien in race_de_chien:
    print(chien)
