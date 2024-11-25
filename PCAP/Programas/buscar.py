grupo = input("Introduce palabra a buscar: ").upper()
palabra = input("Introduce grupo de caracteres: ").upper()

contiene = False
posicion = -1

for i in range(len(palabra) - len(grupo) + 1):
    if palabra[i:i + len(grupo)] == grupo:
        contiene = True
        posicion = i
        break

if contiene:
    print(f"El grupo '{grupo}' se encuentra en la posición {posicion} de la palabra '{palabra}'.")
else:
    print(f"El grupo '{grupo}' no se encuentra en la palabra '{palabra}'.")
