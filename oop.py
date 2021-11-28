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
    def __init__(self,cpu,ram):
        self.processor = cpu
        self.ram = ram

    def config(self):
        print(self.processor,self.ram)

l1 = Laptop("Amd","8gb")
l1.config()
