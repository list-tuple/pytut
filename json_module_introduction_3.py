import json

d1={1:100,2:200,3:333.12,4:444.34,'a':"apple",'b':"bat"}

f4=open("load_json_1.txt",'w')
json.dump(d1,f4)
f4.close()
