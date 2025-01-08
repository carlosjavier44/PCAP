nombre=input("Introduce tu nombre: ")
edad=int(input("Introduce tu edad: "))
direccion=input("Introduce tu direccion: ")
telefono=int(input("Introduce tu telefono: "))

info={'nombre':nombre,'edad':edad,'direccion':direccion,'telefono':telefono}

print(f"{info['nombre']} tiene {info['edad']} años, vive en {info['direccion']} y su número de teléfono es {info['telefono']}")