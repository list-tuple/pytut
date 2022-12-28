import re

string2=" Today is 4th december 2022, we are learning python, regular expression python module"
st1=re.search("python",string2)
print(st1)

st3=re.findall("python",string2)
#print(st3.group(0))
#print(st3.group(1))
print(st3)
if st3:
    print("python found")
else:
    print("python not found")
