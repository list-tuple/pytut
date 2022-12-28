"""
search
findall
match
sub

"""

import re

string1 = "Today is sunday"

result1=re.search("sun",string1)
if result1:
    print(" sun is found in string {}",string1)
else:
    print(" sun is not found in string {}",string1)

string2=" Today is 4th december 2022, we are learning python, regular expression module"

pattern="python"

result2 =re.search(pattern,string2)
if result2:
    print("{} found in {}".format(pattern, string2))
else:
    print("pattern is not found")


while True:
    st1 = input("enter str :")
    res = re.search(st1,string2)
    if res:
        print("{} found in {}".format(st1, string2))
    else:
        print(" not found")
        
