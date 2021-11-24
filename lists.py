#### python list concepts ###

li = [1,2,3,4,5]
cat = len(li)
myli = [li[x] * x for x in range(cat)]
print(myli)


""""sorting list"""

myli.sort(reverse=True)
print(myli)

""" Tuples   """

tm = (20,21,23,24)

d = list(tm)
d.append(26)

print(d)

car = {"brand","model","year"}
data = ["ford","mustang",1964]

cnvrtcar = list(car)
cnvrtcar.sort(reverse=False)
size = len(cnvrtcar)


newdict = {cnvrtcar[x]:data[x] for x in range(size)}
print(newdict)