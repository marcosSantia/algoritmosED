class Queue:
    
    def __init__(self):
        self.elements = []
        
    def arrive(self,element):
        self.elements.append(element)
    
    def atention(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.elements)
    
    def on_front(self):
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            return None
        
    def move_to_end(self):
        element = self.atention()
        if element != None:
            self.arrive(element)
            
            
cola_1 = Queue()

cola_1.arrive(1)
cola_1.arrive(2)
cola_1.arrive(3)
cola_1.arrive(4)
cola_1.arrive(5)
print(cola_1.elements)
print(cola_1.atention())
print(cola_1.on_front())    
cola_1.move_to_end()
print(cola_1.elements)
print(cola_1.atention())
print(cola_1.on_front())
for i in range(cola_1.size()):
    print(cola_1.atention())
    cola_1.move_to_end()
print(cola_1.elements)

    
    