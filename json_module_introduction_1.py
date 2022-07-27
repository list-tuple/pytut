import json

f2=open("json_output.txt",'r')
js_str = f2.readlines()
f2.close()
print("^^^^^^^^^^^^^^^^^^^^")
print(js_str[0])
print(type(js_str[0]))
print("%%%%%%%%%%%%%%%%%%%")
d1= json.loads(js_str[0])
print(d1)
print(type(d1))
print("################")
