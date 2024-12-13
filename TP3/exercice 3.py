from random import *
x = randint(0,100)
compteur = 0

while True :
    n = int(input("Devinez la valeur aléatoire de 0 à 100 que le programme a tiré : "))

    compteur += 1

    if n > x :
        print("Votre valeur est supérieur à celle qu'il faut devinez")
    elif n < x:
        print("Votre valeur est inférieur à celle qu'il faut devinez)")
    else :
        print(f"Bravo, vous avez réussie à deviner le nombre {x} !")
        print(f"Vous avez trouvé le nombre en {compteur} tentatives")


