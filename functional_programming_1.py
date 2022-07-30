"""

Python is an indented, object oriented, functional programming language

functional programming in python
we could send functions as arguments to other functions
we could return functions as return parameters from functions

1. list/tuple comprehension
2. lambda
3. generator,yield
4. map
5. reduce

"""

def function_1(x1,y1):
    result = x1+y1
    return result

def fun_2(x2,y2):
    res1= x2*y2+x2+100
    return res1

def fun_3(x3,y3):
    res2= x3+y3+999
    return res2

def function_2(f1,a1,b1):#f1 is a function
    result1 = f1(a1,b1)
    return result1

def function_3(): # returns fun_4 function
    def fun_4(a4,b4):
        res4 = a4+100+b4+100+a4+b4
        return res4
    def fun_5(a4,b4):
        res4 = a4+100+b4+100+a4+b4
        return res4
    return fun_4


re1 = function_2(function_1,10,20)
print(re1)

#re2 = function_2(45.23,10,20)
#print(re2)

re3= function_2(fun_2,100,200)
print(re3)

re4= function_2(fun_3,100,200)
print(re4)

f9 = function_3()
result_9 =f9(99,77)
print(result_9)

re5 = function_2(f9,22,44)
print(re5)
