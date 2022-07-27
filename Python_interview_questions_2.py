i = int(input("enter number : "))

if i < 10:
    pass# pass statement is a dummy statement to maintain the index level
else:
    print(i)

#exceptions, file operations, functions

# what is an exception?

# l1 = [10,20,30,40,50]
# what happens print(l1[5])?

# what is the output of print(l1[-6])?

# how to write custom exception? => extending exception class

class new_exception(Exception):
    def __init__(self,message):
        
# which part of the code is covered to catch exceptions?

# what is raise statement will do?

# how to handle dividedby zero scenario?

i=10
print(ii)
#what happens above?

#how to handle generic exceptions?
try:
    print(i)
except Exception as e:
    print(e)
#what is try, except block?

#can we handle multiple exceptions in a single try except block?
try:
    print(i)
except NameError as e:
    print(e)
except Exception as e1:
    print(e1)
# how do we send data to functions? => by sending through argument

def function1(a,b):
    c = a+b
    return c

# how do we return values from functions? => by return statement

# how many values we could return from any function? => 1

# how to pass multiple values from function? => prepare a list of multiple values and return list

# what is a default argument?
def function1(a,b=100):
    c = a+b
    return c
# can we write functions in a seperate file? yes

# how do we use functions from a module? by importing

# what is open function will do? return file description to do read and write operations

# what is the argument to be used to open a file in append mode? #'a'

# what is the argumnet to be used to open file in write mode? # 'w'

# what is the difference between write mode and append mode?

#what is fclose function will do? closes file

#lambda, list comprehension, yield, generators, map, reduce, filter => wednesday

#modules(existing, writing new modules),classes => monday
