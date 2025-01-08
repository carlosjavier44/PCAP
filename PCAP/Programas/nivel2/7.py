# Solicitar al usuario que introduzca las palabras y sus traducciones
entrada = input("Introduce las palabras y sus traducciones (formato: palabra:traducción, palabra:traducción): ")

# Crear el diccionario a partir de la entrada del usuario
traducciones = {}
pares = entrada.split(",")  # Separar los pares por comas
for par in pares:
    palabra, traduccion = par.split(":")  # Separar palabra y traducción por dos puntos
    traducciones[palabra.strip()] = traduccion.strip()  # Guardar en el diccionario quitando espacios

# Mostrar el diccionario creado
print("\nDiccionario de traducciones:", traducciones)

# Pedir una frase en español al usuario
frase = input("\nIntroduce una frase en español: ")
palabras = frase.split()  # Separar la frase en palabras

# Traducir la frase palabra por palabra
frase_traducida = []
for palabra in palabras:
    if palabra in traducciones:
        frase_traducida.append(traducciones[palabra])  # Traducir si está en el diccionario
    else:
        frase_traducida.append(palabra)  # Dejar sin traducir si no está

# Mostrar la frase traducida
print("\nFrase traducida:", " ".join(frase_traducida))
