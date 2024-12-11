inf = 0
sup = 0
entre = 0


>>>>>>> 1d15952 (maj)
for i in range(10):
    while True:
        x = int(input("Donner un nombre entre 0 et 20 : "))
        if 0 <= x <= 20 :
            break
        print("Attention il faut que votre valeur soit comprise entre 0 et 20")

    if x < 10 :
        inf = inf +1
        #inf +=1

    elif 10 <= x < 15 :
        entre += 1

    else :
        sup += 1


print("Le nombre de valeurs inférieur strictement à 10 est", inf)
print(f"Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est {sup}")
print("Le nombre de valeurs supérieur ou égale à 15 est", entre)






while True:
    x = int(input("Donner un nombre entier supérieur à 1 : "))
    if x > 1 :
        break
    print("Attention il faut que votre valeur soit supérieur à 1 ")

