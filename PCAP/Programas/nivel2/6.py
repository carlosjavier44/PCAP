informacion_persona = {}

while True:
    clave = input("¿Qué información quieres añadir (por ejemplo, nombre, edad, sexo, etc.)?: ")
    valor = input(f"Introduce el valor para {clave}: ")
    
    informacion_persona[clave] = valor
    
    print("\nContenido actual del diccionario:")
    for clave, valor in informacion_persona.items():
        print(f"{clave}: {valor}")

    continuar = input("\n¿Quieres añadir más información (Si/No)?: ").strip().lower()
    if continuar != "si":
        print("\nPrograma finalizado.")
        break
