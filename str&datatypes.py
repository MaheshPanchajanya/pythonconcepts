x = 5
""" bytearray and memory view"""

print(memoryview( bytearray(5)))

""" boolean """
x = True
print(x)

""" type casting """

a = int(1)
b = float(x)

print(a,b)

""" strings """
a = "hello, Mahesh"

b= a[:5]

print(b[::-1])

""" strip() """
m = "Ma h i"
print(m.strip())

""" string format """
x = 35
y = "my age is {}"
print(y.format(x))
