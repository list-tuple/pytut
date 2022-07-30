"""
reduce => it is an aggregation function returns single value

"""

from functools import reduce

list_1=[10,20,30,40,50,60,70,80,90,100]


def f1(a,b):
    return a+b

def f2(a,b):
    if a>b:
        return a
    else:
        return b

def f3(a,b):
    if a<b:
        return a
    else:
        return b
#sum   
result = reduce(f1,list_1)
print(result)

#maximum
result1 = reduce(f2,list_1)
print(result1)

#minimum
result2 = reduce(f3,list_1)
print(result2)
