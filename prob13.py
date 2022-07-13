"""

Read data strings from three files. ip1.txt,ip2.txt,ip3.txt
1.club all the strings
numbers to numbers.txt
words to alpha.txt
others to alphanumbers.txt

"""
def main():
   #open all input files in read mode
   fh1=open("ip1.txt",'r')
   fh2=open("ip3.txt",'r')
   fh3=open("ip3.txt",'r')
   #open all output files in write mode
   fo1=open("alpha.txt",'w')
   fo2=open("numbers.txt",'w')
   fo3=open("alphanumbers.txt",'w')
   
   #read all input files data
   con1_list = fh1.readlines()
   con2_list = fh2.readlines()
   con3_list = fh3.readlines()
   #covert all input content lists into sets
   con1_set = set(con1_list)
   con2_set = set(con2_list)
   con3_set = set(con3_list)
   
   #club all input sets data using union
   out_var1 = con1_set.union(con2_set).union(con3_set)
   
   #convert the clubbed set into list so that we could visit each item
   out_list = list(out_var1)
   
   #iterate each item and check for alphabet or number
   print(out_list)
   for i2 in out_list:
      i1=i2.strip('\n')
      if i1.isdigit() == True:
           fo2.write(i1)
           fo2.write('\n')
      elif i1.isalpha() == True:
          fo1.write(i1)
          fo1.write('\n')
      else:
          fo3.write(i1)
          fo3.write('\n')
   
   #close output file handlers
   fo1.close()
   fo2.close()
   fo3.close()
   #close input file handlers
   fh1.close()
   fh2.close()
   fh3.close()

def function_1():
    print("hello")
def function_2():
    print("hello 1")
    
try:
   main_1()
   function_1()
   function_2()
except Exception as error:
    print(error)

"""
except IndexError as error:
    print(error)
except KeyError as error:
    print(error)
except FileNotFoundError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
"""
