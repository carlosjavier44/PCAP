divisa=input("Introduce que divisa usas: ").lower().capitalize()
divisas={'Euros':'€','Dolar':'$','Yen':'¥'}
if divisa in divisas:
    print(f"El simbolo de {divisa} es {divisas[divisa]}")
else:
    print("No encontre esa divisa")