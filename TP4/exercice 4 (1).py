L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""

maxOccurence = 0
maxIndice = 0


x = len(L1)


for i in range(x):
    occurence = 0

for j in range(i, x):
    if L1[i] == L1[j]:
        occurence += 1

if occurence > maxOccurence:
    maxOccurence == occurence
    maxIndice = L1[i]


print(f"Le nombre le plus frequent dans la liste est le : {maxIndice} ({maxOccurence}x)")







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
