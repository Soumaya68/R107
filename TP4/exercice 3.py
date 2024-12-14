nMAx = 10

v1 = []
v2 = []

p = 0

while True:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
    if 1 <= n <= 10 :
        break
    print("Attention il faut que votre valeur soit à 1 ")

print("Saisie du premier vecteur :")
for i in range(n):
    a = int(input(f"v1[{i}] = "))
    v1.append(a)

print("\nSaisie du second vecteur :")
for i in range(n):
    b = int(input(f"v2[{i}] = "))
    v2.append(b)

for i in range(n):
    p+=v1[i]*v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {p}")


