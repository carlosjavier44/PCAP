import csv

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

    # Método estático para verificar si un número es entero
    @staticmethod
    def is_integer(num):
        # Cuenta el nº de elementos que tienen punto cero (.0)
        # Ej. 2.0, 10.0, 100.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Método de clase para instanciar empleados desde un diccionario
    @classmethod
    def instanciar_desde_diccionario(cls, emp):
        return cls(
            nombre=emp.get('nombre'),
            cargo=emp.get('cargo'),
            salario=float(emp.get('salario', 25000.50))  # Valor por defecto si no hay salario
        )

    # Método para imprimir el objeto Empleado
    def __repr__(self):
        return f"Empleado('{self.nombre}', '{self.cargo}', {self.__salario})"

# Manejo de excepciones al crear empleados
try:
    empleado1 = Empleado("Carlos Pérez", "Ingeniero", 30000)
    empleado2 = Empleado("Ana López", "Diseñadora")
    empleado3 = Empleado("Luis García", "Analista", -15000)
except ValueError as e:
    print(e)

# Mostrar el número total de empleados y la plantilla
print(f"Número total de empleados: {Empleado.num_empleados}")
print("Plantilla de empleados:")
for empleado in Empleado.plantilla:
    print(empleado)

# Crear un empleado desde un diccionario de ejemplo
empleado_dict = {'nombre': 'Pedro Martínez', 'cargo': 'Gerente', 'salario': '40000'}
nuevo_empleado = Empleado.instanciar_desde_diccionario(empleado_dict)
print(nuevo_empleado)
