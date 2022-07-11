"""
Dictionaries in Python is a collection of key value pairs,enclosed in {},keys are unique(keys
will not be repeated
d1={1:100,2:200,3:300,4:400,5:500,'c':345,45.67:"qwerty",'a':12.56}
1,2,3,4,5,'c',45.67,'a' => keys
100,200,300,400,500,345,"qwerty",12.56 => values

1. keys => returns the keys of a dictionary
2. values => returns the values of the dictionary
3. items => returns key,value tuples of the dictionary
4. update => we can use update function to add or update any value of the dictionary
5. copy => copies the dictionary
6. pop => we could remove one key:value pair from the dictionary
"""

d1={1:100,2:200,3:300,4:400,5:500,'c':345,45.67:"qwerty",'a':12.56}
#read operations of the dictionary
print(d1['c']) #345
print(d1[5])#500
print(d1['a'])#12.56
#write/update operation of the dictionary
#using a key and with assignment operator we could update the particular value of a dictionary
d1[2]=999
#d1={1:100,2:999,3:300,4:400,5:500,'c':345,45.67:"qwerty",'a':12.56}
d1[111]="aaa"
#d1={1:100,2:999,3:300,4:400,5:500,'c':345,45.67:"qwerty",'a':12.56,111:'aaa'}

#1. keys => returns the keys of a dictionary
k_123_list = d1.keys()
print(k_123_list)
"""
Result:
dict_keys([1, 2, 3, 4, 5, 'c', 45.67, 'a', 111])

"""
#2 values
v_123_list = d1.values()
print(v_123_list)
"""
Result:
dict_values([100, 999, 300, 400, 500, 345, 'qwerty', 12.56, 'aaa'])
"""
#3 items
i_12_tuples = d1.items()
print(i_12_tuples)
"""
Result:
dict_items([(1, 100), (2, 999), (3, 300), (4, 400), (5, 500), ('c', 345), (45.67, 'qwerty'), ('a', 12.56), (111, 'aaa')])

"""
#4 update
#d1={1:100,2:999,3:300,4:400,5:500,'c':345,45.67:"qwerty",'a':12.56,111:'aaa'}
d1.update({111:'bbb'})
print(d1)

d1.update({1111:"qqqq",2222:"ssss"})
print(d1)
"""
Result:
{1: 100, 2: 999, 3: 300, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb'}
{1: 100, 2: 999, 3: 300, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}

"""
#5 copy function is to take backup or one copy of the dictionary data
d_1=d1
print(d1)
print(d_1)
d1[3]=333
print(d1)
print(d_1)
"""
{1: 100, 2: 999, 3: 300, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 300, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
"""
d_2=d1.copy()
print(d1)
print(d_2)
d1['c']="apple"
print(d1)
print(d_2)
"""
Result:
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 'apple', 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 345, 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}

"""
#6 pop
print(d1)
E1=d1.pop(1)
print(d1)
print(E1)
"""
Result:
{1: 100, 2: 999, 3: 333, 4: 400, 5: 500, 'c': 'apple', 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
{2: 999, 3: 333, 4: 400, 5: 500, 'c': 'apple', 45.67: 'qwerty', 'a': 12.56, 111: 'bbb', 1111: 'qqqq', 2222: 'ssss'}
100
"""

"""

1.Below dictionary is a for alphabet and related word keys. Please fix the keys and values properly
alpabet_items ={'a':'apple','b':'cat','c':'dog','d':'ball'}

2.Below number:word dictionaries are not in  proper order correct it
number_words ={100:"one hundred",200:"three hundred",300:"two hundred",400:"five hundred"}

"""


