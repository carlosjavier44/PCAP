# El Dígito de la Vida

"""
Se suman todos los dígitos de la fecha introducida.
Si el resultado contiene más de un dígito, se repite la suma hasta obtener un solo dígito.
Ejemplo: 1 Enero 2017 = 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12 -> 1 + 2 = 3
"""


while True:
    fecha = input("Introduce tu fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric() and len(fecha) == 8:
        break
    print("Debes introducir una fecha en formato AAAAMMDD.")

while len(fecha) > 1:
    suma = 0
    for digito in fecha:
        suma += int(digito) 
    fecha = str(suma)  

print(f"Tu Dígito de la Vida es: {fecha}")
