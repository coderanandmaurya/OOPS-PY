# super : parent method and constructor not attribute

class Phone:
    
    def __init__(self,price,brand,camera):
        print("indside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
        
class SmartPhone(Phone):
    
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        print("indside phone constructor")
        self.os=os
        self.ram=ram
        print("Inside Smartphone constructor")
        
        
s=SmartPhone(2000, "mi", "13MP","win",4)
  

print(s.os)
print(s.brand)
#nOt working s.super().buy()