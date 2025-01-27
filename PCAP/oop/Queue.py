class Queue:
    
    def __init__(self):
        self.queue=[1,2,3]
        return
    
    def enqueue(self,valor):
        if self.queue:
            self.queue.append(valor)
            return
        
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return None
    
pila =  Queue()
 
pila.enqueue(1)
pila.enqueue(2)
pila.enqueue(3)
 
dequeue = pila.dequeue()
print(dequeue)
