def read_int(prompt, min, max):

    try:
        value = int(input(prompt))
        if value < min or value > max:
            print("Ingresa un numero entre {} y {}".format(min, max))
            raise ValueError
        return value
    except ValueError:
        print("Valor no valido")
        return read_int(prompt, min, max)
    

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
    