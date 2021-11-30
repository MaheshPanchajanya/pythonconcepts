# object oriented concepts in python

# define a class 

class Computer: #class declaration

    def config(self):
        print("this i5 machine")


com1 = Computer()
print(com1.config()) #Acess with object
print(Computer().config()) #Acess without object

 # __init__ method 

class Laptop:
     
    graphics = "Galax1060ti" 
    
    def __init__(self,cpu,ram,price): # constructor 
        self.processor = cpu # instance variable
        self.ram = ram
        self.rate = price

   
    def config(self):
        print(self.processor,self.ram,self.rate,self.graphics)
    
    def compare(self,cmp):
        if self.rate > cmp.rate:
            return True
        else:
            return False      

    #@staticmethod
    @classmethod
    def speed(cls):

        cls.li = [1,3,4,5]

        cls.li.sort(reverse=True)
        print(cls.li)

l1 = Laptop("Amd","8gb",35000)
l2 = Laptop("intel","8gb",4000)


l1.config()
l2.config()
Laptop.speed()

if l1.compare(l2):
    print("amd is lesser")

