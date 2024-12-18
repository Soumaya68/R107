L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

maxOccurence = 0
maxIndice = 0

x = len(L1)


for i in range(x):
    occurence = 0
    L1.count(L1[i])
if occurence > maxOccurence:
    maxOccurence == occurence
    maxIndice = L1[i]


print(f"Le nombre le plus frequent dans la liste est le : {maxIndice} ({maxOccurence}x)")
