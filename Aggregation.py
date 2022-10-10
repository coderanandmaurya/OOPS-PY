# relationship b/w classes 3 type 2 major: Aggregation and Inheritance
# Aggregation : Has - A relationship
# inheritance : Is - A relationship

# smartphone class
# product class
# what relationship in this
# Inheritance: smartphone -> is a -> product diagram: - [smartphone] ---------<>[product]
# Aggregation: Customer -> has a ->Address  diagram: - [cust] <>---------[add]

class Customer:
    
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city, new_pin, new_state)
        
class Address:
    
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
        
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state
        
add=Address("LDH", 141013,"WB")
cust= Customer("anand","male",add)

cust.edit_profile("musk","PB",12,"Ind")

print(cust.address)
print(cust.address.pincode)