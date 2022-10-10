class parent:
    
    def __init__(self,num):
        
        self.__num=num
        
    def get_num(self):
        return self.__num
    
class Child(parent):
    
    def __init__(self,val, num):
        self.__val=val
        
    def get_val(self):
        return self.__val
        
son=Child(100,23)

# not invoked parent constructor 
print("Parent Num: ",son.get_num())
print("Child Val : ",son.get_val())
son.show()