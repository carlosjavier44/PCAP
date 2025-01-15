import sys
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)
    
    def pop(self):
        val=self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def mostrar_pila(self):
        elementos = ""
        for val in self.__stack_list:
            elementos += f"{val}, "
        elementos = elementos[:-2] if elementos else ""
        return f"pila={{{elementos}}}"

stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.mostrar_pila())

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
try:
    print(len(stack_object.__stack_list))
except AttributeError:
    print(f"Error de atributo, es privado")
    sys.exit(1)