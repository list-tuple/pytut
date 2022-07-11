"""
Tuple is a special case of list, in which items are not changable/alterable
any type of data types any number of repeatations, enclosed by ()

1. index => return the index of a particular item in list
2. count => returns the number of times a particular item is repeated in the tuple
"""
a_123 = (12,45,'c','a',"qwerty","asdf",34.67,45.78,'c',12,"asdf")
#        0  1   2   3     4       5     6

#1 index
print(a_123.index("qwerty"))

r1=a_123.index(34.67)
print(r1)

#r2 = a_123.index(999)
#print(r2)

"""
Result:
4
6
Traceback (most recent call last):
  File "C:/Users/Lalith Eswar/Documents/desktop/20june22/tuple_functions.py", line 15, in <module>
    r2 = a_123.index(999)
ValueError: tuple.index(x): x not in tuple

"""
a_123 = (12,45,'c','a',"qwerty","asdf",34.67,45.78,'c',12,"asdf")
#2 count

r3=a_123.count(12)
print(r3)

r4 = a_123.count('a')
print(r4)

r5 = a_123.count(888)
print(r5)

"""
Result:
2
1
0
"""
