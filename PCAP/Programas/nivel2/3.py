precios = {
    'Manzana': 3.5,
    'Plátano': 2.0,
    'Naranja': 1.8,
    'Pera': 2.5
}

fruta = input("Introduce el nombre de la fruta: ").title() 
kilos = float(input("Introduce el número de kilos: "))

if fruta in precios:
    precio_total = precios[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {precio_total:.2f}€")
else:
    print("La fruta no está en el diccionario.")
