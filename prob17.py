"""
class1 with two parameters a1,b1
four functions add,diff,multi,div
class2 inherited from class1
two functions square,power
"""

class firstclass():
    a1 = 20
    b1 = 5    
    def function_1(self):
        result_1=self.a1+self.b1
        return result_1
    def function_2(self):
        result_2=self.a1-self.b1
        return result_2
    def function_3(self):
        result_3=self.a1*self.b1
        return result_3
    def function_4(self):
        result_4=self.a1/self.b1
        return result_4
    def function_a(self):
        res_a=10*10
        return res_a
    
class secondclass(firstclass):
    def function_5(self):#square function
        result_5=self.a1*self.a1
        result_51=self.b1*self.b1
        return result_5,result_51
    
    def function_6(self):#power function 10 power 6 = 1*10*10*10*10*10*10
        result_6 =1
        for i1 in range(self.b1):
            result_6=result_6*self.a1
        return result_6


fc=firstclass()
result_1=fc.function_1()
print(result_1)
result_2=fc.function_2()
print(result_2)
result_3=fc.function_3()
print(result_3)
result_4=fc.function_4()
print(result_4)
sc=secondclass()
result_5,result_51=sc.function_5()
print(result_5,result_51)
result_6=sc.function_6()
print(result_6)
rea=fc.function_a()
print(rea)
