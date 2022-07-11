"""

List and its operations

List is collection of items any type, any repetations, any number, and also it is alterable

1. append => adds a new item at the end of the list
2. count => counts the number of times a particular item is repeated
3. index => return the index or position -1 of a particular item
4. extend => extend the current list with the new list
5. insert => inserts an item at a position we specify
6. pop => it removes the last items and returns
7. sort => sorts the items in a list
8. remove => removes a particular item

"""
list2 =['h','o',25,3.53,0.33,3.53,"dee",'o',25,("kn","lo","iu",58,7735.2)]

#1. append => adds a new item at the end of the list
# append a item 888.9 to the list list2
print(list2)
list2.append(888.9)
print(list2)
list2.append("qwerty")
list2.append('a')
print(list2)
"""
Result:
['h', 'o', 25, 3.53, 0.33, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2)]
['h', 'o', 25, 3.53, 0.33, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9]
['h', 'o', 25, 3.53, 0.33, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a']
"""
#re1=list_5.count('a')
#2. count => counts the number of times a particular item is repeated
result = list2.count(25)
print(result)
result1=list2.count(0.33)
print(result1)
result2=list2.count('z')
print(result2)
"""
Result:
2
1
0
"""
#3. index => return the index or position -1 of a particular item
result3 = list2.index('dee')
print(result3)
result4 = list2.index(3.53) # returns the first occurance
print(result4)
#result5 = list2.index(999)# throws value error
#print(result5)
"""
Result:
6
3
Traceback (most recent call last):
  File "C:/Users/Lalith Eswar/Documents/desktop/20june22/list_operations.py", line 51, in <module>
    result5 = list2.index(999)
ValueError: 999 is not in list
"""
#4. extend => extend the current list with the new list
li_1=[1,2,3,4]
li_3=[1,2,3,4]
li_2 =['a','b','c']
li_1.extend(li_2)
print(li_1)
li_3.append(li_2)
print(li_3)
# append adds a complete list as a single item where as extend adds each item of the second
# list to first list as individial items
list2.extend(li_1)
print(list2)
"""
Result:
[1, 2, 3, 4, 'a', 'b', 'c']
[1, 2, 3, 4, ['a', 'b', 'c']]
['h', 'o', 25, 3.53, 0.33, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c']

"""
#5. insert => inserts an item at a position we specify
x=123.56
print(list2)
list2.insert(5,x)
print(list2)
res1 = len(list2)
print(res1)
y='Apple'
list2.insert(25,y)
print(list2)
print(len(list2))
# if the index is greater than the length of the list, the item is inserted at the end
"""
Result:
['h', 'o', 25, 3.53, 0.33, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c']
['h', 'o', 25, 3.53, 0.33, 123.56, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c']
21
['h', 'o', 25, 3.53, 0.33, 123.56, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c', 'Apple']
22
"""
#6. pop => it removes the last items and returns
print(list2)
res3 = list2.pop()
print(res3)
print(list2)
res4=list2.pop()
print(res4)
print(list2)
"""
Result:
['h', 'o', 25, 3.53, 0.33, 123.56, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c', 'Apple']
Apple
['h', 'o', 25, 3.53, 0.33, 123.56, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b', 'c']
c
['h', 'o', 25, 3.53, 0.33, 123.56, 3.53, 'dee', 'o', 25, ('kn', 'lo', 'iu', 58, 7735.2), 888.9, 'qwerty', 'a', 1, 2, 3, 4, 'a', 'b']

"""
#7. sort => sorts the items in a list in an assending order
list_4=[98,43,12,67,-98,-34,23,-67,9]
print(list_4)
list_4.sort()
print(list_4)
#list2.sort()#TypeError: 
#print(list2) 
"""
[98, 43, 12, 67, -98, -34, 23, -67, 9]
[-98, -67, -34, 9, 12, 23, 43, 67, 98]
Traceback (most recent call last):
  File "C:/Users/Lalith Eswar/Documents/desktop/20june22/list_operations.py", line 123, in <module>
    list2.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
"""

#8. remove => removes an item from a list
print(list_4)
list_4.remove(-98)
print(list_4)
#list_4.remove("abc")#ValueError
#print(list_4)
"""
Result:
[-98, -67, -34, 9, 12, 23, 43, 67, 98]
[-67, -34, 9, 12, 23, 43, 67, 98]
Traceback (most recent call last):
  File "C:/Users/Lalith Eswar/Documents/desktop/20june22/list_operations.py", line 138, in <module>
    list_4.remove("abc")
ValueError: list.remove(x): x not in list

"""
