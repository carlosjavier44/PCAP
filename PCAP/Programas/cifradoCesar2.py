# Cifrado César 2.
mensaje = input("Ingresa tu mensaje: ")
cipher = ''
num=0

while True:
    num = input("Ingresa el desplazamiento: ")
    if num not in range(1,26):
        break

for char in mensaje:
    if not char.isalpha(): #Si no es cifra, pasa
        continue
    char = char.upper()     #m -->
    code = ord(char) + int(num)    #punto de codigo siguiente
    if code > ord('Z'):     #si rebasa el alfabeto...
        code = ord('A')     #... empieza otra vez
    cipher += chr(code)

print(cipher)