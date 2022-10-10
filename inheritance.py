# inheritance : legally : your father property your property
# Biological level : same face

# udemy: users: std, instructor
#class std: login reg, enroll,renew
# class instructute: login, reg, create course, Answer

# login and reg both have same same code writing code F
# DRY Dont repeat yourself
# make a new class user-login,reg-<std-enroll,rev>,<Instructor,createcourse,Answer>

# Inheritance always on up side your dad money is your bbut not your money is belong to dad

#P -->C data_member(variable),member fun(method),Constructor
# private member are not inherited

class User:
    
    def login(self):
        print("Login")
        
    def register(self):
        print("Register")
        
class Student(User):
    
    def enroll(self):
        print("enroll")
        
    def review(self):
        print("Review")
        
stu1=Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()

# reverse inheritance is not allowed
#U=User()
#U.enroll()
