
class myClassJuly22():
    list_1=[10,20,30,40,50]
    dic_1 = {1:100,2:200,3:300,4:400}
    def function_1(self):
        sum1=0
        for i1 in self.list_1:
            sum1= sum1+i1

        return sum1


class myClassJan23(myClassJuly22):
    def function_2(self):
        c1=0
        sum1=0
        for i1 in self.list_1:
            sum1 = sum1+i1
            c1=c1+1
        ave = sum1/c1
        sum_2 = self.function_1()
        print(self.dic_1)
        return ave


mj22=myClassJuly22()
result1=mj22.function_1()
print(result1)

mj23 = myClassJan23()
result2 = mj23.function_2()
print(result2)


"""
class1 with two parameters a1,b1
four functions add,diff,multi,div
class2 inherited from class1
two functions square,power
"""


