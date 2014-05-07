import re

s = "1907,37,15,Petronille"
m = re.match ("19(\d\d),(.*?),(.*)", s)
a = m.group (0)
b = m.group (1)
c = m.group (2)
d = m.group (3)

print(a)
print(b)
print(c)
print(d)