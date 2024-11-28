for i in range(10):
    while True:
        x = int(input("Donner un nombre entre 0 et 20 : "))
        if 0 <= x <= 20 :
            break
        print("Attention il faut que votre valeur soit comprise entre 0 et 20")
