"""
1. General data types

Integer, Float, Character, String
Integer => 100,200,-12 (rounded values no decimal digits)
Float => 11.23, -456.67,0.009,-0.234
Character => 'a','1','*','#','0' any single item with single quotes
String => "qwerty","apple","asdf","qwert@123","one#456" it is a group of characters
'qwerty' => this is not a good practice, it works in some places, but doesnot
work in cases like json string we will face issues.

2. Python Data types
List, Tuple, Dictionary, Set

List => collection of items of any type of any repeatations enclosed by [],a any alterations are possible
[10,34,67,12.346,'c','g',10,"apple",-10,-34.67,"ball",'c',34,-10]
Tuple => it is a special case of list which is immutable means we cannot change/alter any item
         enclosed by ()
(13,56.78,13,'4','c','v',"cycle","dog","screen","keyboard",'h',10,45,67.89,4)
Set => Set is also special case of list enclosed {} and no repeatations or duplicates
{12,45,67.89,'c','e','y',"laptop","computer","wednesday","june"}
Dictionary=> It is a collection of key value pairs enclosed {}, keys are always unique
keys are not not repeatable,values could be repeatable
{"apple":"it is a fruit","ball":"it is a toy",100:"one hundred",35.4:"hyderabad temperature",'c':100
24.6:"hyderbad temperature"}


list_1=[10,56,[56.6,89,'c'],{12,'c'},{1:'c',5:'i'},(1,2,34)]
diction_1={'a':[34,67,'c',89.76],100:{"qwerty","asdf","zxcv"},45.67:(2,3,4,5)}

list_2=[999,333,12.34,{"qwert":{'a':"qw",'b':"as"}}]
diction_2={'a':"today is wednesday",'v':('q','a'),111:{100:123,200:567},'f':[1089.56,67.78]}

list is any types, any repeatations, alterable
set     any types, no repeatations,  alterable
tuples  any types, any repatations,  immutable(no change)






"""

list_1=[23,56,34,23.67,98] # 5 items,length of the list is 5
#       0  1   2  3    4   # number for each item
# index starts with 0 ends with n-1 where n is length of the list
# using index we could access items in the list
print(list_1[0])#23
print(list_1[3])#23.67
print(list_1[4])#98
#print(list_1[6])# index error
print(list_1)
list_1[2]=999
print(list_1)
#altering the items is possible in list by assignment operator

tuple_1=(12,67,45,34)
print(tuple_1[2])
#tuple_1[2]=1234

set_1={10,20,40,56,10,20,45,12}
print(set_1)


