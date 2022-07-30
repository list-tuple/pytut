"""
tuple comprehension always returns zero
generator is an object which generates items on demand

"""

list_1=[10,20,30,40,50]

list_2=[x1*x1 for x1 in list_1] #[100, 400, 900, 1600, 2500]
print(list_2)#5*4bytes = 20 bytes

tup_1 = (x1*x1 for x1 in list_1)
print(tup_1) #(100,400,900,1600,2500) 2bytes

for i1 in tup_1:
    print(i1) #20bytes
