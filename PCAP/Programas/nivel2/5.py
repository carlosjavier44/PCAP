asignaturas={'Matemáticas': 6, 'Física': 4, 
'Química': 5}
total_creditos=0
for asignatura , creditos in asignaturas.items():
    print(f'La asignatura {asignatura} tiene {creditos} créditos')
    total_creditos += creditos
    
print("Un total de",total_creditos,"créditos")