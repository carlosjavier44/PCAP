asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
pendientes = []

for asignatura in asignaturas:
    nota = int(input("Introduce tu nota de " + asignatura + ": "))
    if nota < 5:
        pendientes.append(asignatura) 

print("Asignaturas pendientes: " + ", ".join(pendientes))
