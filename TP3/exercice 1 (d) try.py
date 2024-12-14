x = 0
somme = 0
i = 0

while x <= 1:
    print("Veuillez saisir une valeur de x supérieure à 1 : ")
    x = input()
    try:
        x = int(x)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

while somme + i <= x:
    somme += i
    i += 1

print(f"Le plus grand nombre N est {i - 1}")
