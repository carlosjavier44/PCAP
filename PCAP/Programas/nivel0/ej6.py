num1 = input("Ingresa el primer numero: ")
num2 = input("Ingresa el segundo numero: ")

if num1>num2:
    print(f"El primer numero ({num1}) es mayor que el segundo numero ({num2})")
elif num1==num2:
    print(f"El primer numero ({num1}) es igual al segundo numero ({num2})")
else:
    print(f"El segundo numero ({num2}) es mayor que el primer numero ({num1})")