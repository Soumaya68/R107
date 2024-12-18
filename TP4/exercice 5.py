date = input("Donnez moi une date (jjmmaaaa) : ")
jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])
print(f"{jour}/{mois}/{annee}")

while 0 > annee or annee > 9999 or 0 > mois or mois>12 or jour < 1 or jour > 31 :
    print("Date incorrecte ! ")
    date = input("Entrez une nouvelle date (jjmmaaaa) : ")
    jour = int(date[0]) * 10 + int(date[1])
    mois = int(date[2]) * 10 + int(date[3])
    annee = int(date[4]) * 1000 + int(date[5]) * 100 + int(date[6]) * 10 + int(date[7])