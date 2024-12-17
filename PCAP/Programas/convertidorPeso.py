peso = float(input("Introduce tu peso: "))

unidad = input("¿Está el peso en (K)g o (L)bs? (Escribe K o L): ").strip().upper()

if unidad == "K":
    peso_en_libras = round(peso / 0.45, 2)
    print(f"Tu peso en libras es {peso_en_libras} lbs.")
elif unidad == "L":
    peso_en_kilos = round(peso * 0.45, 2)
    print(f"Tu peso en kilogramos es {peso_en_kilos} kg.")
else:
    print("Opción no válida. Por favor, escribe 'K' o 'L'.")
