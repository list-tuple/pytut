class firstclass():
    a1 = 20
    b1 = 5
    def __init__(self,l1,m1):
        self.c1=l1
        self.d1=m1
    def function_1(self):
        print("inside parent class function_1 function")
        result_1=self.a1+self.b1
        return result_1
    def function_2(self):
        result_2=self.a1-self.b1
        return result_2

    
class secondclass(firstclass):
    def __init__(self,str1,x1,y1):
        self.my_str = str1
        firstclass.__init__(self,x1,y1)# linking parent class constructor
        #with child class
    #"""
    def function_1(self):#overiding the parent class function function_1
        print("inside child class function_1 function")
        res = self.a1*self.b1+self.a1*self.a1
        return res
    #"""
    def function_5(self):#square function
        result_5=self.a1*self.a1
        result_51=self.b1*self.b1
        return result_5,result_51
    
    def function_6(self):#power function 10 power 6 = 1*10*10*10*10*10*10
        result_6 =1
        for i1 in range(self.b1):
            result_6=result_6*self.a1
        return result_6
    def function_7(self):
        result_7 = self.c1+self.d1
        print(result_7)
        return result_7


fc=firstclass(10,20)
result_1=fc.function_1()
print(result_1)
result_2=fc.function_2()
print(result_2)

sc=secondclass("hello python",11,22)
result_5,result_51=sc.function_5()
print(result_5,result_51)
result_6=sc.function_6()
print(result_6)
result_7 = sc.function_7()
print(result_7)

print("******************************")
rt1= sc.function_1()
print(rt1)
print("&&&&&&&&&&&&&&&&&&&&&&&&&")

