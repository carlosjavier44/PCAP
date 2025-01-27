class reptil:
    def __init__(self,nombre):
        self.nombre=nombre
    
class serpiente(reptil):
    def __init_subclass__(cls):
        return super().__init_subclass__()
    
class culebra(serpiente):
    def __init_subclass__(cls):
        return super().__init_subclass__()

rep=reptil("lagarto")
serp=serpiente("mamba nigga")
cul=culebra("culebra")

print(f"{reptil.__name__}\t{serpiente.__name__}\t{culebra.__name__}")
for cls1 in [reptil,serpiente,culebra]:
    for cls2 in [reptil,serpiente,culebra]:
        print(issubclass(cls1,cls2), end="\t")
    print()
    
print(f"\t\t{type(rep).__name__}\t{type(serp).__name__}\t{type(cul).__name__}")
for obj in [rep,serp,cul]:
    print(obj.nombre, end=" \t")
    for clase in [reptil,serpiente,culebra]:
        print(isinstance(obj,clase), end="\t")
    print()

print(reptil.__name__)
print(type(rep))
print(type(serp))
print(type(cul))

reptil1=reptil("lagartija")
reptil2=reptil("lagarto")
reptil3=reptil("cocodrilo")

reptil1=reptil2
reptil2=reptil3

print(reptil1==reptil2,reptil1 is reptil2)

reptil1==reptil3
print(reptil2==reptil3,reptil1 is reptil3)