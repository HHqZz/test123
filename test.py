import pygame

##### VARIABLES #######
#integer => entier
alizee = 5.5
lunette = 3
total = alizee + lunette
print(total)

# String = chaine de caractere
prenom = "Constantin"
nom = "Bouis"
#prenom = "dgfgdsgjknlodf"

nomComplet = prenom + " " + nom
print(nomComplet)

## list double(gros entier) float (nombre a virgule) 

# bool => true or false
isBroken = True

#Condition
# Si prenom c'est Constantin, alors affiche 7
#  Sinon affiche 0
if prenom == "Constantin" :
    print(7)
else :
    print(0)

print("programme termine")

maListe = []
maListe.append(1)
maListe.append(45)
maListe.append("coucou")
maListe.append(prenom)

isConstantinInList = False
# Verifier si Constantin est bien present dans la liste
for item in maListe:
    if item == "Constantin":
        isConstantinInList = True

if isConstantinInList:
    print("Constantin est dans liste")
else:
    print("Constantin pas dans liste")


#Fonction

#while


