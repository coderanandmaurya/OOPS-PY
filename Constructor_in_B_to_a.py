# Use parent constructor

class Phone:
    
    def __init__(self,Price,brand,camera):
        print("Inside phone constructor")
        self.Price=Price
        self.brand=brand
        self.camera=camera
        
class Smartphone(Phone):
    pass

# class b ka contructor bnaoge to class a call ho jayga
S=Smartphone(200, "mi", "13MP")

print(S.Price)