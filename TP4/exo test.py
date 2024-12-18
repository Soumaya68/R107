def somme(a, b):
    print(a + b)

def division(a, b):
    print(round(a / b, 2))


a = int(input("Entrez un nombre : "))
somme(a, 3)

somme = 627

nbCent = 0
nbCinquante = 0
nbVingt = 0
nbDix = 0
nbDeux = 0
nbUn = 0

while somme >= 100:
    somme -= 100
    nbCent += 1
while somme >= 50:
    somme -= 50
    nbCinquante += 1
while somme >= 20:
    somme -= 20
    nbVingt += 1
while somme >= 10:
    somme -= 10
    nbDix += 1
while somme >= 2:
    somme -= 2
    nbDeux += 1
while somme >= 1:
    somme -= 1
    nbUn += 1

print(nbCent, nbCinquante, nbVingt, nbDix, nbDeux, nbUn)

test = []

for i in range(5):
    test.append("*")
    print(test)
print("\n")
for i in range(5):
    print(test)
    test.remove("*")

test1 = {"nom": "BELTRAN", "prenom": "Julien", "age": 25, "fonction": "Ingénieur"}
print(test1["nom"])


liste = [10,8,200,2,10000]

print(liste)
liste.sort()
print(liste)