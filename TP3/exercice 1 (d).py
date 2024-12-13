x = 0
somme = 0
i = 0

while True:
    x = int(input("Donner un nombre entier supérieur à 1 : "))
    if x > 1 :
        break
    print("Attention il faut que votre valeur soit supérieur à 1 ")


while somme + i <= x:
    somme += i
    i += 1

print(f"Le plus grand nombre N est {i - 1}")
