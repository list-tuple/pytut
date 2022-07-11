"""
open a file in append mode take 10 inputs string from the cmd input
and write into the file


"""

fh3=open("python_learners_new.txt","a")
for i1 in range(0,10,1):
    var1 = input("enter the string :")
    #var1= "new contnent" + var1
    var1 = var1 +'\n'
    fh3.write(var1)
fh3.close()

"""
open two files alpha.txt , numbers.txt, alphanumber.txt in write mode
take 10 inputs strings from the cmd line in the for loop
check the inputstring is having only alphabets then write into alpha.txt
check the input string is having only numbers then write into numbers.txt
close both files
"""
fh1 = open("alpha.txt","w") 
fh2 = open("numbers.txt","w")
fh3 = open("alphanumbers.txt","w")
for i1 in range(0,10,1):
    str_1 = input("enter string: ")
    if str_1.isalpha() == True:
        fh1.write(str_1)
    elif str_1.isdigit() == True:
        fh2.write(str_1)
    else:
        fh3.write(str_1)
fh1.close()
fh2.close()
fh3.close()
