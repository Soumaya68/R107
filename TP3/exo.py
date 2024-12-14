def calculer_tarif(debut, fin):
    """
    Fonction qui calcule le tarif de location d'un vélo en fonction des heures de début et de fin.
    Elle affiche également les durées correspondant à chaque tarif.
    """
    montant_total = 0
    heures_1euro = 0
    heures_2euro = 0

    # Vérification des conditions d'entrée
    if debut < 0 or debut > 24 or fin < 0 or fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !")
        return None
    if debut == fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.")
        return None
    if debut > fin:
        print("Attention ! le début de la location est après la fin ...")
        return None

    # Traitement des heures de location
    for h in range(debut, fin):
        if 0 <= h < 7 or 17 <= h < 24:
            montant_total += 1  # Tarif 1 euro par heure
            heures_1euro += 1
        else:
            montant_total += 2  # Tarif 2 euros par heure
            heures_2euro += 1

    # Affichage du détail des heures de location
    if heures_1euro > 0:
        print(f"{heures_1euro} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_2euro > 0:
        print(f"{heures_2euro} heure(s) au tarif horaire de 2.0 euro(s)")

    return montant_total


def main():
    # Affichage du message d'introduction
    print("IUT de Colmar Département RT – R107- TP3")
    print("Ismail Bennis 3 2023-2024")

    try:
        # Demander à l'utilisateur de saisir les heures de début et de fin
        debut = int(input("Donnez l’heure de début de la location (un entier) : "))
        fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
    except ValueError:
        print("Veuillez entrer des entiers valides.")
        return

    # Calcul du tarif total
    tarif_total = calculer_tarif(debut, fin)

    # Si les heures sont valides, afficher le montant total
    if tarif_total is not None:
        print(f"Le montant total à payer est de {tarif_total:.1f} euro(s).")


# Lancer le programme
if __name__ == "__main__":
    main()