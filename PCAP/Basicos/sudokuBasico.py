tablero = []
sudoku_ok = True  # Suponemos que es válido hasta que se demuestre lo contrario

# Ingresar las 9 filas del Sudoku
for i in range(9):
    fila = input(f"Introduce fila #{i}: ")
    if not fila.isnumeric() or len(fila) != 9:  # Verifica si es numérica y tiene 9 dígitos
        print("La fila contiene caracteres no numéricos o no tiene exactamente 9 números.")
        sudoku_ok = False
        break
    elif sorted(fila) != list("123456789"):  # Verifica que contenga exactamente los números del 1 al 9
        print("La fila debe contener todos los dígitos del intervalo [1-9].")
        sudoku_ok = False
        break
    else:
        tablero.append(fila)

if sudoku_ok:
    print("El Sudoku SÍ es válido")
else:
    print("El Sudoku NO es válido")
