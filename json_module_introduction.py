"""
json => java script object notation
json module is to convert python lists,dictionaries to strings and vice versa

loads takes string as input and converts to dictionary or list
load takes files handler as input and converts to dictionary or list

dumps takes dictionary and converts to the json str
dump takes dictionary & file handler and writes json str into the file
"""
import json

d1={1:100,2:200,3:333.12,4:444.34,'a':"apple",'b':"bat"}

d1_str = json.dumps(d1)

print("**************************")
print(d1)
print(type(d1))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(d1_str)
print(type(d1_str))
print("#########################")

f1=open("json_output.txt",'w')
f1.write(d1_str)
f1.close()
