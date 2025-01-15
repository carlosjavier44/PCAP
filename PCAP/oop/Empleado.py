class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario
    

    def getSalario(self):
        return self.__salario

    def __str__(self):
        return f"Empleado(nombre={self.nombre}, edad={self.edad})"

empleado = Empleado("Juan", 30, 50000)

print(empleado)

