import math

x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
except AssertionError:
    print("Que sipollo su colega")    
    exit(0)
    
x = math.sqrt(x)
    

print(x)
    