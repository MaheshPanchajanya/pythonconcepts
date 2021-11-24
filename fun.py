### functions and lambda ####

def  simple(x):

    return lambda a : a*x

tit = simple(6)

print(tit(10))