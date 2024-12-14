# Demander à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier n pour calculer sa factorielle : "))

# Demander à l'utilisateur de choisir le type de boucle
choix_boucle = input("Choisissez le type de boucle ('for' ou 'while') : ").strip().lower()

# Initialisation de la variable de la factorielle
fact = 1

if choix_boucle == 'for':
    # Boucle 'for' pour calculer la factorielle
    for i in range(1, n + 1):
        fact *= i
        print(f"Après {i} itération(s), la factorielle est : {fact}")

elif choix_boucle == 'while':
    # Boucle 'while' pour calculer la factorielle
    i = 1
    while i <= n:
        fact *= i
        print(f"Après {i} itération(s), la factorielle est : {fact}")
        i += 1

else:
    print("Choix invalide, veuillez choisir 'for' ou 'while'.")

# Affichage du résultat final
print(f"La factorielle de {n} est : {fact}")