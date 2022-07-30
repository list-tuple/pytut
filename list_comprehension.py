"""
list comprehension => to make another list based on existing list


"""

list_1 =[1,2,3,4,5]
#list_2=[1,4,9,16,25]

list_2= [ i1*i1 for i1 in list_1]

print(list_1)
print(list_2)

list_3 = [2*i1+3*i1*i1+999 for i1 in list_1]

print(list_3)

li_3 = []
for i2 in list_1:
    x1=2*i2+3*i2*i2+999
    li_3.append(x1)
print(li_3)


"""
1.
list_t = [22,55,34,23,67,89,12,45]
1. x1*x1+99
2. x1*x1*x1+x1*x1+789+x1
3. x1*99+x1*(99+x1*78)
make another list using list comprehension
2.
write a function which returns 4 functions fun_1,fun_2,fun_3,fun_4

fun_1 => +
fun_2 => *
fun_3 =>sqrt
fun_4 => pow


"""
