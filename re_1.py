import re
# searching pattern with digits one or more

string1="this is year is 2022"
pat1 = "\d+"

result1 = re.search(pat1,string1)
if result1:
    print("pattern found")
else:
    print("pattern not found")

#searching a pattern with 4 digits
pat2="\d{4}"
result2 = re.search(pat2,string1)
if result2:
    print("pattern found")
else:
    print("pattern not found")

#searching a patten with 4 digits at the end of the string
pat3="\d{4}$"
result3 = re.search(pat3,string1)
if result2:
    print("pattern found")
else:
    print("pattern not found")
#searching a patten with 4 digits at the begining of the string
string2="5,December 2022 is todays date"
pat4="^\d"
result4 = re.search(pat4,string2)
if result2:
    print("pattern found")
else:
    print("pattern not found")
#one or more words in any place of the string
pat5="\w+"
string2="5,December 2022 is todays date"

result5 = re.search(pat5,string2)
if result2:
    print("pattern found")
else:
    print("pattern not found")

#one or more words at the end of the string
pat6="\w+$"
string2="5,December 2022 is todays date"

result5 = re.search(pat6,string2)
if result5:
    print("pattern found")
else:
    print("pattern not found")
#one or more words at the start of the string
pat7="^\w+"
string1="this is year is 2022"

result5 = re.search(pat7,string1)
if result5:
    print("pattern found")
else:
    print("pattern not found")

#search for a word with 4 letters at the starting 
pat8="^\w{4}"
string1="this is year is 2022"
string2="5,December 2022 is todays date"
result5 = re.search(pat8,string1)
if result5:
    print("pattern found")
else:
    print("pattern not found")

#search for a word with 4 letters at any place with space before and after
pat9="\s\w{4}\s"
string1="this is year is 2022"
string2="5,December 2022 is todays date"
result6 = re.search(pat9,string1)
if result6:
    print("pattern found")
else:
    print("pattern not found")

#replace 4 digit word with 2021
string3 = re.sub("\d{4}","2021",string1)
print(string3)

#replace first four letter word with 2022
string4 = re.sub("^\w{4}","2022",string1)
print(string4)

#replace year(word starting with y) with YEAR
string5 = re.sub("y\w+","YEAR",string1)
print(string5)

#replace December with November
string6 = re.sub("D\w+","November",string2)
print(string6)

#findall words starting with D
list1=re.findall("D\w+",string2)
print(list1)

#findall words starting with 2
list2=re.findall("2\d+",string2)
print(list2)

#search of word starting with 2 and at the position at the end of the string
list3=re.findall("2\d+$",string1)
print(list3)

#findall a digit at the begining of the string
list4=re.findall("^\d+",string2)
print(list4)
