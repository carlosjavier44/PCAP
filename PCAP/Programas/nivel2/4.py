meses = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}

fecha = input("Introduce una fecha en formato dd/mm/yyyy: ")

dia, mes, año = fecha.split('/')

mes_nombre = meses[int(mes)]

print(f"{dia} de {mes_nombre} de {año}")
