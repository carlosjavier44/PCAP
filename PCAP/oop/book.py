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
        
book1 = Book('El señor de los anillos 1',31,'JRR',21)
book2 = Book('El señor de los anillos 2',32,'JRR',22)
book3 = Book('El señor de los anillos 3',33,'JRR',23)

print(book1)
print(book2)
print(book3)