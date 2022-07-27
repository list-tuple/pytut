"""
di1 ={1:"one",2:"two",3:"three"}
write a class with constructor
2 functions
1. count number of key,value pairs means number of keys(private)
2. return the concat string of all values the dintionary(private)
3. return the concat string and count number(public)
"""
class A():
    def __init__(self,di2):
        self.x1 = di2
        
   
    
    def __fun1(self):
        x2 = len(self.x1 )
        #print(x2)
        return x2
   
    
    def __fun2(self):
        x3 = self.x1.values()
        
        x4 =''.join(x3)


        #print(x4)
        return x4
      
    
    def fun3(self):
        x5=self.__fun1()
        x6=self.__fun2()
        return x5,x6
          

di1 ={1:"one",2:"two",3:"three"}
obj = A(di1)
res1,res2=obj.fun3()
print(res1)
print(res2)
