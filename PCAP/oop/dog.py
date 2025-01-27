class dog:
    kennel = 0 
    def __init__(self,raza):
        self.raza=raza
        dog.kennel+=1
    def __str__(self):
        return self.raza + " dice: ¡Guau!"

class sheepdog(dog):
    def __init__(self):
        return super().__str__() + " ¡No huyas corderito!"

class guarddog(sheepdog):
    def __str__(self):
         return super().__str__() + " ¡Hola buenas soy un guardian!"
  
class lowlanddog(sheepdog):
    def __str__(self):
             return super().__str__(self) + " ¡No me gustan las montañas"
         

        