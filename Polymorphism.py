# Polymorphism: - method overloading, method overriding,operator overloading

# method overriding : dil ki baat suno
# parent buisness  ---> i love coding so i go for coding i have opton for usiness but i love coding

class Phone:
    
    def __init__(self,Price,brand,camera):
        print("Inside phone constructor")
        self.Price=Price
        self.__brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying a Phone")
        
class Smartphone(Phone):
    
    def buy(self):
        print("buying a smartphone")

# class b ka contructor bnaoge to class a call ho jayga
S=Smartphone(200, "mi", "13MP")

S.buy()