"""
Exceptions => handling data related extreme scenarios programmatically

"""
"""
#scenario 1
try:
   n1 = int(input("enter number :"))
   n2= int(input("enter another number :"))
   
   result = float(n1)/float(n2)
   print(result)
except ZeroDivisionError as error:
    print("zero division error occured")

try:
   list_1=[]
   x2=int(input("number of strings:"))#x2 >100
   for i1 in range(x2):
       x1=input("enter string")
       list_1.append(x1)
 
   print(list_1)
   print(list_1[0])
   print(list_1[100])
except IndexError as error:
    print("Index error occured")

try:
   d1={}
   x2=int(input("number of strings:"))
   for i2 in range(x2):
       k1=int(input("enter key:"))
       v1=input("enter value:")
       d1[k1]=v1
   print(d1)
   print(d1[1])
   print(d1[100])
except KeyError as error:
   print("key error occured")
"""
try:
    s1={"hari","krishna"}
    s2={"ramu","giri"}
    s3=s1.union(s2)
    print(s1[0])
    d1={1:"one",2:"two",3:"three",4:"four"}#1
    print(d1[1])#2
    list_1 = [1,2,3,4,5,6]#3
    print(list_1[10])#4
    fh =open("qwerty_123.txt","r")#
    fh.close()
except TypeError as error:
    print("type error occured")
except KeyError as error:
    print(error)
except IndexError as error:#5
    print(error)
except FileNotFoundError as error:
    print("needed file is not found. Please check again")

"""
try:
    list_2=[10,20,30,40,50]
    print(list_2[100])
except Exception as error:
    print(error)

"""
