# imprime_pares.py

def imprime_pares(lista):
    '''
    Toma como argumento una lista de números e imprime solamente los pares.
    '''
    for num in lista:
        if int(num) % 2 == 0:
            print(num)
        else:
            continue
