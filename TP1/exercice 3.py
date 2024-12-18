jour = int(input("Donner le jour du mois : "))

heure = int(input("Donner l'heure d'aujourd'hui : "))

minute = int(input("Donner le nombre de minutes dans cette heure : "))

x = (((jour-1) * 24)*60) + (heure*60) + minute

print (f"Le nombre de minutes écoulées depuis le début du mois est de : " , x)