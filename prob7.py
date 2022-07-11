"""
Take a two numbers from the user and do below menu driven operations
1. addition
2. multiples
3.division
4.sqrt
5. pow    a**b
6.subtraction
After selection do the corresponding operation.
"""
a=int(input("enter var 1"))
b=int(input("enter var 2"))
print("1. addition")
print("2. multiples")
print("3.division")
print("4.subtraction")
operation = input("enter operation :")

if operation == '1':
    result = a+b
elif operation == '2':
    result = a*b
elif operation == '3':
    result = a/b
elif operation == '4':
    result = a-b
else:
    result="invalid operation"
print(result)
    
