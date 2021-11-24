"""
python variables concepts

global,local variable  

multiline 

"""


x = 10 #globalvariaable
#y = 5
def myfun():
    global y
    y = 5
    print(x,y)

myfun() 

print(y)

a,b,c = [10,20,30]

print(a)
print(b)
print(c)
