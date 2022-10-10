class Customer:
    
    def __init__(self,name):
        self.name=name
        
def greet(customer):
    # customer pointing at name
    print(customer.name,"id is : ", id(customer))
    
    # lets change the customer name 
    customer.name="mango"
    print("customer name is : ",customer.name)
    print(customer.name,"id is : ", id(customer))
    
cust=Customer("Anand")
print(cust.name,"id is : ", id(cust))


greet(cust)
print("cust name is : ",cust.name)
print(cust.name,"id is : ", id(cust))

#class object is always mutable see id
# change will occur at all place because of mutability