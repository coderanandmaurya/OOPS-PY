class Customer:
    def __init__(self,name):
        self.name=name
        
    def intro(self):
        print("I am ",self.name)
        
c1=Customer("A")
c2=Customer("B")
c3=Customer("C")

L=[c1,c2,c3]

for i in L:
    print(i.name)
    i.intro()
