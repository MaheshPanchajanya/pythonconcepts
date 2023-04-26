from fileinput import FileInput
import os
import re
import pymysql





x = open("dml","r")
temp  = ""
li = []
for f in x:
	li.append(f)
print(li)

for i in li:
	s = i.strip()
	if re.findall(';$',s):
		
		if temp == "":
			print(s)

		else:
			if not re.findall(';$',temp):
				print(temp+" "+s)
	else:
		if not re.findall(';$',s):
			temp = s
		
