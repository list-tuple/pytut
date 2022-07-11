"""
Read data strings from three files. ip1.txt,ip2.txt,ip3.txt
1.club all the strings and place it in one file "output_1.txt"
2.common strings across all the input files should be placed in output_2.txt

"""

ofh1=open("output_1.txt","w")
ofh2=open("output_2.txt","w")
ip1=open("ip1.txt","r")
ip2=open("ip2.txt","r")
ip3=open("ip3.txt","r")

ip1_content = ip1.readlines()
ip2_content = ip2.readlines()
ip3_content = ip3.readlines()

ip1_set = set(ip1_content)
ip2_set = set(ip2_content)
ip3_set = set(ip3_content)

union_result_set = ip1_set.union(ip2_set).union(ip3_set)

result_1_list = list(union_result_set)
for i1 in result_1_list:
    ofh1.write(i1)

        
union_result_set_1 = ip1_set.intersection(ip2_set).intersection(ip3_set)

result_2_list = list(union_result_set_1)
for i2 in result_2_list:
    ofh2.write(i2)
    
ip1.close()
ip2.close()
ip3.close()
ofh1.close()
ofh2.close()
