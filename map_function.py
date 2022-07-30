"""

map function => applying a particular function on all items of the list

"""

list_1=[22,44,66,77,88]

list_2 = [x*x for x in list_1]

def f1(x):
    return x*x

list_3_map = map(f1,list_1)

print(list_1)
print(list_2)
print(list_3_map)

for i1 in list_3_map:
    print(i1)
