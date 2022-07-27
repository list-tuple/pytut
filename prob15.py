def fun1():
  fh1 = open("alpha.txt","w")
  fh2 = open("numbers.txt","w")
  fh3 = open("alphanumbers.txt","w")
  # If the user enter data other than string then program crashed and errors will raise
  # to resolve this issues it's better to handle errors by using try
  for i in range(1,11,1):
      x = input("enter strings = ")
      if x.isdigit() == True:
          fh2.write(x)
      elif x.isalpha() == True:
          fh1.write(x)
      else:
          fh3.write(x)

  fh1.close()
  fh2.close()
  fh3.close()

try:

    fun1()
    
except Exception as error:
    print(error)
