import re

string1="today is sunday 2022 december month"
s1=re.match("(\w+) (\w+) (\w+) (\d+) (\w+) (\w+)",string1)
print(s1)
print(s1.group(0))
print(s1.group(1))
print(s1.group(2))
print(s1.group(3))
print(s1.group(4))#number
print(s1.group(5))
print(s1.group(6))
#* none or more
#+ one or more
