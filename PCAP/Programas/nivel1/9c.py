palabra = input("Introduce una palabra: ").lower()

vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    contador = palabra.count(vocal)
    print(f"{vocal}: {contador}")
