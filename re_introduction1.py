
import re

string2=" Today is 4th december 2022, we are learning python, regular expression python module"
st1=re.sub("python","java",string2)
print(st1)

st2=re.sub("december","november",string2)
print(st2)

st3=re.sub("2022","2021",string2)
print(st3)
