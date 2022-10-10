# pass by reference
#create class name custmer
class Customer:
    
    
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print(self.name)
        print(self.gender)

def greet(customer):
    if customer.gender == "male":
        print("Mr",customer.name)
    elif customer.gender == "female":
        print("Ms",customer.name)
    else:
        print("hello",customer.name)
        
    cust2 = Customer("Anand","male")
    
    return cust2

# creating obj name Anand        
cust=Customer("bandi","female")
print(cust.name)

# passing object to method
greet(cust)

new_cust=greet(cust)
print(new_cust.name)
        