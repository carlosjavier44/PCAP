import random
numAdivinar = random.randint(0, 100)
adivinado=False
print("Adivina el número entre 0 y 100")
while adivinado==False:
    num=int(input("Inserta un numero para intentarlo: "))
    if numAdivinar==num:
        print("Has ganado")
        adivinado=True
    elif numAdivinar>num:
        print(" ")
        print("El número es mayor, sigue intentandolo")
    else:
        print(" ")
        print("El número es menor, sigue intentandolo")
