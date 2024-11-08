# Sumador de Números

from imprime_pares import imprime_pares as impp

'''
Este programa toma una serie de números como entrada, y devuelve la suma total.
Si encuentra caracteres no numéricos, lanza una excepción.
'''

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print("Error: '" + substr + "' no es un numero.")

impp(strings)
