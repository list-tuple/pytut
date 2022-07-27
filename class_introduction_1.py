"""
1. private members(parameter or function) will start with __
2. private memmbers are accessible from other functions of the same class
3. from public function we could access private functions
"""

class first_class_123():
    __k1 = 100 #private member
    __l1 = 200 #private member

    e1=400
    f1=500
    def __init__(self,a1,b1): #constructor
        self.m1=a1
        self.n1=b1

    def function_1(self):
        result_1 = self.m1 + self.n1 + self.__k1
        return result_1

    def function_2(self,x1,x2):#public function
        result_2 = self.m1+self.n1 + x1*x2 + self.__k1 + self.__l1
        re2= self.__function_3()#calling private function from public function
        result = result_2+re2
        return result

    def __function_3(self): # private function
        result_3 = self.m1 * self.n1 + self.__k1 + self.__l1
        return result_3

    def __function_4(self):
        result_4 = self.m1*self.n1+self.__k1
        return result_4

def fun1():
   fc=first_class_123(10,20)
   re1=fc.function_1()
   print(re1)
   re2=fc.function_2(20,30)
   print(re2)
   #res3= re1.__function_3()#throws error
   #print(re3)
   #print(re1.__k1) #throws error

fun1()

di1 ={1:"one",2:"two",3:"three"} #onetwothree
write a class with constructor and 2 functions
1. count number of key,value pairs means number of keys(private)
2. return the concat string of all values the dintionary(private)
3. return the concat string and count number(public)


