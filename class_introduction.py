"""
object
  ==> some parameters
  ==> will perform some actions

car
  ==> parameters
      4 wheels
      4 windows
      4 doors
      color
      shape
  ==> functionalities
      Drive/travel
      Air condition
      
object that binds parameters with functionalities/functions
class is a template of an object

pulsar class, TS07QW1234, TS12ER1235,...
swift class, AP123er1234, AP34QW1234..

in python there are only constructors but no destructors, reason memory
release will happen automatically
constructor constructs/initializes the object
There will be only one constructor in python class and its name is __init__
the first argument/parameter to the functions in class is always is self
constructor is a special case of function
"""

class first_class_123():
    def __init__(self,a1,b1,c1): #constructor
        self.m1=a1
        self.n1=b1
        self.k1=100
        self.j1=c1

    def function_1(self):
        result_1 = self.m1 + self.n1
        return result_1

    def function_2(self,x1,x2):
        result_2 = self.m1+self.n1 + x1*x2
        return result_2

fc1 = first_class_123(100,200,300) #creating an object fc1 for the class first_class_123

res1 =fc1.function_1()
print(res1)
print(fc1.function_1())
res2=fc1.function_2(11,22)
print(res2)
"""
write a class,constructor takes two numbers
it has 4 functions +,-,*,/
"""
"""
write a class,constructor takes one list
it has two functions
1. gets the length of the list
2. gives the count of even numbers
3. sum of all the numbers in list
4. average of all numbers in the list
list_1=[12,67,34,89,34,56]
"""
class sec_class():
    def __init__(self,list1): #constructor
        self.m_list_1 = list1

    def list_count(self):
        return len(self.m_list_1)

    def co_even(self):
        co =0
        for i1 in self.m_list_1:
            if i1%2 == 0:
                co = co+1
        return co

    def sum_list(self):
        sum1=0
        for i1 in self.m_list_1:
            sum1 = sum1+i1
        return sum1

    def ave_list(self):
        sum1=0
        co=0
        for i1 in self.m_list_1:
            co=co+1
            sum1 = sum1+i1
        ave = sum1/co
        return ave

list_1=[12,67,34,89,34,56]
sc = sec_class(list_1)
re1= sc.list_count()
re2= sc.co_even()
re3= sc.sum_list()
re4=sc.ave_list()
print(re1)
print(re2)
print(re3)
print(re4)











