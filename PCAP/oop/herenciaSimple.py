class Saiyan:
    origen="saldana"
    def __init__(self, nombre):
        self.nombre = nombre
        
class Humano:
    origen = "Tierra"
    def __init__(self, nombre):
        self.nombre = nombre

class Goku(Saiyan):
    pass


class Vegeta(Saiyan):
    pass    

class Trunks(Saiyan,Humano):
    def __init__(self,padre,madre):
        self.padre=padre
        self.madre=madre

    def verAncestros(self):
        for x in Trunks.__bases__:
            print(x.__name__, end=' ')
        print()

goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegetta777")
bulma = Humano("Bulma")
trunks = Trunks(vegeta,bulma)

print(type(trunks).__name__)

print(trunks.__dict__)

print(f"El padre de {trunks.nombre} es {trunks.__dict__['padre']}")
print(f"El madre de {trunks.nombre} es {trunks.__dict__['madre']}")

if type(trunks).__name__=="Mestizo":
    if issubclass(Trunks,Saiyan):print(f"{trunks.nombre} puede convertirse en supersaiyan")
    if issubclass(Trunks,Humano):
        print(f"{trunks.nombre} tiene madre humana")
else:
    print(f"{trunks.nombre} NO puede convertirse en supersaiyan")