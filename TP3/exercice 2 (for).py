import time

x = int(input("Donner un nombre entier positif : "))

if x < 0:
    print("Attention il faut que votre valeur soit positive, recommencer")

else :
    for i in range(x, -1, -1):
        print(i)
        time.sleep(1)
