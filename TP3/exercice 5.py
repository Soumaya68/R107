def calculer_tarif(debut, fin):
    tarif_total = 0
    for h in range(debut, fin):
        if 0 <= h < 7 or 17 <= h < 24:
            tarif_total += 1
        elif 7 <= h < 17:
            tarif_total += 2
    print("Vous avez loué votre vélo pendant")

    return tarif_total


def main():
    while True:
        try:
            debut = int(input("Donnez l’heure de début de la location (un entier) : "))
            fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

            if not (0 <= debut <= 24 and 0 <= fin <= 24):
                print("Les heures doivent être comprises entre 0 et 24 !")
                continue
            if debut == fin:
                print("Attention ! l’heure de fin est identique à l’heure de début.")
                continue
            if debut > fin:
                print("Attention ! le début de la location est après la fin. ")
                continue

            tarif = calculer_tarif(debut, fin)
            print(f"Le montant total à payer est de {tarif} euro(s)")
            break

        except ValueError:
            print("Veuillez entrer des valeurs valides.")
            continue

if __name__ == "__main__":
    main()
