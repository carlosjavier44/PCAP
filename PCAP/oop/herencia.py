class Book:
    def __init__(self, title, quantity,author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        
        self.__price=price
        self.__discount=None
        
    def set_discount(self,discount):
        self.__discount=discount
        
    def get_price(self):
        if self.__discount:
            return self.__price*(1-self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Titulo:\'{self.title}\',Cantidad: {self.quantity}, Autor: \'{self.author}\', Precio: {round(self.get_price(),3)}€"
        
class Novel(Book):
    def __init__(self, title, quantity, author, price,pages):
        super().__init__(title, quantity, author, price)
        self.pages=pages

class Academic(Book):
    def __init__(self, title, quantity, author, price,branch):
        super().__init__(title, quantity, author, price)
        self.branch=branch
    def __repr__(self):
        return f"Titulo:\'{self.title}\',Genero: \'{self.branch}\',Cantidad: {self.quantity}, Autor: \'{self.author}\', Precio: {round(self.get_price(),3)}€"

    
novela1=Novel('La comunidad del anillo',31,'JRR',31,560)    
novela1.set_discount(0.20)

ensayo1= Academic('Que si pereira',12,'ElXokas',18,'Sociologia')   

print(novela1)
print(ensayo1)

book1 = Book('El señor de los anillos 1',31,'JRR',21)
book2 = Book('El señor de los anillos 2',32,'JRR',22)
book3 = Book('El señor de los anillos 3',33,'JRR',23)

print(book1)
print(book2)
print(book3)