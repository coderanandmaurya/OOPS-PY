class Atm:
    
    #static/class variable same for all obj
    __counter = 1
    
    def __init__(self):
        # instance variable is different for all obj

        self.pin=""
        self.__Name="muskee"
        self.balance=0
        self.sno=Atm.__counter
        Atm.__counter=Atm.__counter+1
        
        print(id(self))
        
        self.menu()
        
    # we dont need self because we dont use self here 
    # we need class variable
    # we call it static method because we dont need obj
    @staticmethod
    
    def get_counter():
        return Atm.__counter
    
    
    def set_counter(new1):
        if type(new1) == int():
            Atm.__counter=new1
        else:
            print("Not Allowd")
    
    def menu(self):
        
        user_input=input("""
                         Press 1 for SET Name
                         Press 2 for Set PIN
                         Press 3 for deposit Money
                         press 4 for Withdraw Money
                         press 5 for Check Balance
                         press Any Alphabet for exit
                         
                         Press: """)
        
        if user_input == "1":
            self.__Name=input("Enter Your name : ")
            print(self.__Name)
            self.menu()
        elif user_input == "2":
            self.pin =input("Enter New PIN : ")
            print(self.pin)
            self.menu()
        elif user_input== "3":
            self.valid_pin=input("Enter PIN : ")
            if self.valid_pin == self.pin:
                self.amount=int(input("enter Amount : "))
                self.balance=self.balance+self.amount
                print("sucessfully Deposit : ",self.amount,"Rs")
                print("Total Amout is : ",self.balance, "Rs")
                self.menu()
            else:
                print("wrong Pin")
                self.menu()
        else:
            print("thanku visit again")
                         
                         