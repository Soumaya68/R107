BASE = int(4)
fromage = float(800.0)
eau = float(2.0)
ail = float(2.0)
pain = float(400.0)

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

nouvelleQuantitéfromage = fromage * nbConvives / BASE
nouvelleQuantitéeau = eau * nbConvives / BASE
nouvelleQuantitéail = ail * nbConvives / BASE
nouvelleQuantitépain = pain * nbConvives / BASE


print("Pour faire une fondue fribourgeoise pour" , nbConvives , "personnes, il vous faut : ")
print(nouvelleQuantitéfromage ,"gr de fromage")
print(nouvelleQuantitéeau ,"dl d'eau")
print(nouvelleQuantitéail ,"gousse(s) d'ail")
print(nouvelleQuantitépain ,"gr de pain")


