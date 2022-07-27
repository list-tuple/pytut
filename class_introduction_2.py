"""
Class is a template of an object
object is with parameters and functions
constructor is a function which will be called while object is created
no destructor in python
self parameter binds parameters and functions
"""

class myClass():
    i1=111 #public
    j1=222 #public
    __x=444 #private
    __y=555 #private
    def __init__(self,a,b): #constructor
        self.m1=a
        self.n1=b

    def function_1(self):
        result = self.n1*self.i1 + self.m1*self.j1
        return result

    def function_2(self,c,d):
        result = self.n1 *c + self.m1*d
        r1= self.__function_3()
        p1= self.__function_4(c,d)
        result = result +r1+p1
        return result

    def __function_3(self): # private
        result = self.i1+self.j1+self.__x+self.__y
        return result

    def __function_4(self,q1,w1):#private
        result = self.__x+self.__y+q1+w1
        return result
    


mc = myClass(100,200)
res1= mc.function_1()
res2=mc.function_2(20,30)
print(res1)
print(res2)
#res3= mc.__function_3()
    
