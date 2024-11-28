x = float(input("Entrez un nombre décimal : "))

I = (x >= 2  and x < 3) or (0 < x and x <= 1) or (-10 <= x and x < -2)

if I :
    print("x appartient à I")
else:
    print("x n'appartient pas à I")