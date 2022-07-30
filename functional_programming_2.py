def fun_1(x1,x2):
    result =x1+x2
    return result


def fun_2(x3,x4):
    result1 = x3*x4
    return result1

def function_1(f1,f2):
    l1 = int(input("enter number :"))
    l2 = int(input("enter another number :"))
    res1 = f1(l1,l2)
    res2 = f2(l1,l2)
    print(res1)
    print(res2)

function_1(fun_1,fun_2)
