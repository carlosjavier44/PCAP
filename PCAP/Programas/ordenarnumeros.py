def ordena_positivos(lista):
    if not lista:
        return []

    positivos_ordenados = sorted([num for num in lista if num > 0])

    resultado = []
    indice_positivos = 0
    for num in lista:
        if num > 0: 
            resultado.append(positivos_ordenados[indice_positivos])
            indice_positivos += 1
        else: 
            resultado.append(num)

    return resultado

lista = [3, -1, 4, 1, -5, 0, -2]
print(ordena_positivos(lista)) 