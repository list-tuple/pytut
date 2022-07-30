"""
lambda is to write anonymous functions
lambda is used basically for small single line functions
functions written using lambda gives performance inmprovements

"""

def fun1(x):
    result = x*x+200*x+900
    return result

def fun2(x,y):
    result1 = x*x*2001+x*299+x*y+y*y
    return result1

fun_1 = lambda x:x*x+200*x+900
fun_2 = lambda x,y:x*x*2001+x*299+x*y+y*y

x=200

res1=fun_1(x)
res2=fun1(x)

print(res1)
print(res2)

x1=11
x2=22
res3=fun2(x1,x2)
res4=fun_2(x1,x2)
print(res3)
print(res4)
