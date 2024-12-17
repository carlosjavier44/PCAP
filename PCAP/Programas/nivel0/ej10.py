import random

consola = ["piedra","papel","tijera"]
jugar=True

while jugar==True:
    usuario = input("Que quieres usar?? (piedra papel tijera) ")
    bot = random.choice(consola)
    print("El bot usara:",bot)," y tu has usado",usuario
    if usuario == bot:
        print("Empate")
    elif usuario == "piedra":
        if bot == "tijera":
            print("Ganaste")
        else:
            print("Perdiste")
    elif usuario == "papel":
        if bot == "piedra":
            print("Ganaste")
        else:
            print("Perdiste")
    elif usuario == "tijera":
        if bot == "papel":
            print("Ganaste")
        else:
            print("Perdiste")
    
    jugar = input("Quieres jugar de nuevo? (si/no)")
    if jugar == "no":
        jugar = False
        print("Hasta luego")
    else:
        jugar = True
        print("Jugaremos de nuevo")
    