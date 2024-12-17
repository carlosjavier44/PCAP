ganadores=[]
for i in range(0,5):
    num=input("Intoduce un numero ganador de la loteria:")
    ganadores.append(int(num))
    
ganadores.sort()
    
print("Numeros ganadores: "+str(ganadores))