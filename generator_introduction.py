"""
generator is implemented using yield key word
next function is used to retrieve data from the generator
we will call next till we get StopIteration
"""

def f1(list_1):
    for i1 in list_1:
        return i1

def f2(list_1):
    for i1 in list_1:
        yield i1
        
list_1=[25,35,12,34,23]

"""
res1=f1(list_1)
print(res1)
"""
g1=f2(list_1) #generator

r1=next(g1)
print(r1)
r2=next(g1)
print(r2)
r3=next(g1)
print(r3)
r4=next(g1)
print(r4)
r5=next(g1)
print(r5)
r6=next(g1)#StopIteration
print(r6)
