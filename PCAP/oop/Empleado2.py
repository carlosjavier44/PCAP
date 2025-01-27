class Empleado:

    plantilla = []  
    num_empleados = 0  

    def __init__(self, nombre: str, cargo: str, salario: float = 25000.50):
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")

        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario 

        Empleado.plantilla.append(self)

        Empleado.num_empleados += 1

    def get_salario(self):
        return self.__salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Cargo: {self.cargo}, Salario: {self.__salario}"

try:
    empleado1 = Empleado("Carlos Pérez", "Ingeniero", 30000)
    empleado2 = Empleado("Ana López", "Diseñadora")
    empleado3 = Empleado("Luis García", "Analista", -15000)
except ValueError as e:
    print(e)

print(f"Número total de empleados: {Empleado.num_empleados}")
print("Plantilla de empleados:")
for empleado in Empleado.plantilla:
    print(empleado)
