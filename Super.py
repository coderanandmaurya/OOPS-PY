# super : parent method and constructor not attribute

class Phone:
    
    def __init__(self,price,brand,camera):
        print("indside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("buying a phone")
        
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone ")
        super().buy()
        
        
s=SmartPhone(2000, "mi", "13MP")
  
s.buy()      

#nOt working s.super().buy()