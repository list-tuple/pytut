
list1=[1,2,3,5,-7,8,9,10,11,12,-13,20,22,23,24,-25,26,27,20,21,22,-4]
find out how many even numbers are there and
how many odd numbers are there and
how many positive numbers are there and
how many negative numbers are there



list1=[1,2,3,5,-7,8,9,10,11,12,-13,20,22,23,24,-25,26,27,20,21,22,-4]
Take a element from the user and find out how many times the  element occurred
in given list


even_count=0
odd_count=0
pos_count=0
neg_count=0

for i2 in list1:
    if i2>0:
        pos_count = pos_count+1
    else :
        neg_count = neg_count+1
    if i2%2 == 0:
        even_count = even_count +1
    else:
        odd_count = odd_count +1

print("even count ",even_count)
print("odd_count ",odd_count)
print("pos_count ",pos_count)
print("neg_count ",neg_count)
