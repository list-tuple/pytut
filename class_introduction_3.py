class uClass():
    list_1 = [10,20,30,40,50]
    d_2={4:100,5:200,6:300}
    def __init__(self,d1):
        self.dic1 = d1

    def fun_1(self):
        sum1=0
        for i1 in self.list_1:
            sum1 = sum1+i1
        return sum1

    def fun_2(self):
        re1= self.dic1.keys()
        re2 = self.dic1.values()
        return re1,re2

d_1={1:100,2:200,3:300}
uc=uClass(d_1)
result1 = uc.fun_1()
result2,result3 = uc.fun_2()
print(result1)
print(result2)
