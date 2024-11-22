for i in range(3):
    n = int(input("Entrez un nombre entier: "))

    if n>0:
        s=("Le nombre est positif ")
    else:
        s=("Le nombre est négatif ")
    if n==0:
        s = ("Le nombre est zéro ")

    if n%2 == 0:
        pa=("et pair")
    else:
        pa=("et impair")

    print(s+pa)