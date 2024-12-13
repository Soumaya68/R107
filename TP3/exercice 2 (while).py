import time

x = int(input("Donner un nombre entier positif : "))

if x < 0:
    print("Attention il faut que votre valeur soit positive, recommencer")

else:
    while x > 0 :
        x-=1
        print(x)
        time.sleep(1)
