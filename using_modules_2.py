import datetime
from datetime import timedelta

d1=datetime.datetime.now()
str1=d1.strftime("%Y-%m-%d")
if str1 == '2022-07-19':
	print("link is valid")
else:
    print("link is not valid")

time_str =d1.strftime("%H-%M-%S")
print(time_str)

td=timedelta(days=50)

d2=d1+td

str2=d2.strftime("%Y-%m-%d")
print(str1)
print(str2)
	    
