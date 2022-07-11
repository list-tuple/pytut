"""

Range function

"""


list_1 = [0,1,2,3,4]
list_2 = range(0,5,1) #initial_value,final_value+1,increment
list_3 = range(0,5)#incremental is by default 1
list_4 = range(5)#incremtnal is by default 1, initial_value is 0

range(0,100,10)#=>[0,10,20,30...90]
range(0,25,5)#=>[0,5,10,15,20]
range(0,1000,100)#=>[0,100,200,900]
range(25)#[0,1,2,3,..24]
range(100,0,-10)#[100,90,80,70,60..10]
#range is only for integers

#calculate sum of numbers starting 0 till 100 with an increment of 10

sum1=0
for a1 in range(0,110,10):
    sum1=sum1+a1
print(sum1)#0,10,20,30..100

#print numbers between 0to100 which are multiples of 5
#print sum of even numbers between 0to500
#print average of numbers which are multiples of 3 between 0 and 50
