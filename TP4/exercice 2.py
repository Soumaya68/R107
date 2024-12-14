# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range (nombreEtudiants):
    x = float(input(f"Note etudiant {i} : "))
    notes.append(x)
    moyenne += x

moyenne = moyenne / nombreEtudiants
print(f"\nMoyenne de classe : {moyenne}\n")

for i in range (nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i] - moyenne}")



