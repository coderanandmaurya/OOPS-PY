class parent:
    
    def __init__(self,num):
        
        self.__num=num
        
    def get_num(self):
        return self.__num
    
class Child(parent):
    
    def show(self):
        print("This is child class")
        
son=Child(23)
print(son.get_num())
son.show()