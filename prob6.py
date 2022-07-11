"""
Problem:
operating systems:
	1.windows
	2.android
	3.mac
Enter an option:

If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
If the user enters 2 then show "Goto second floor and buy adroid mobiles"
If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"

we need to use dictionaries and if else conditions
"""

#approach 1
d1={'1':"Goto first floor and buy windows laptop or mobile",\
    '2':"Goto second floor and buy adroid mobiles",\
    '3':"Goto third floor and buy mac laptop or iphones"}
print("
other_msg="There is only three floors, please select 1 or 2 or 3"

print("1.windows")
print("2.android")
print("3.mac")

number = input("Enter an option: ")
#i_number = int(number)
if number in d1.keys():
    print(d1[number])
else:
    print(other_msg)

#approach 2
print("1.windows")
print("2.android")
print("3.mac")

number = input("Enter an option: ")
if number =='1':
    print("Goto first floor and buy windows laptop or mobile")
elif number =='2':
    print("Goto second floor and buy adroid mobiles")
elif number =='3':
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")




    
