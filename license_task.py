import datetime
from datetime import timedelta
import json
"""
License checking module
1. open a license_date.txt file
   a. if the file exists read the date string from the file
   b. else if the file doesnot exists open the file license_date.txt
      and write todays date

2.open a license_expiry_date.txt file
   a. if the file exists read the date string from the file
   b. else if the file doesnot exists open the file license_expiry_date.txt
      and write todays date + 90 days

3. check todays date string is equal to expiry date then print message
   license expired


"""

def write_read_license_date_file():
    try:
        fh1 = open("license_date1.txt",'r')
        #lines_txt = fh1.readlines()
        ret_d1 = json.load(fh1)
        fh1.close()
        return ret_d1["date"]   
    except FileNotFoundError as error:
        print("file not found")
        fh2 = open("license_date1.txt","w")
        d1 = datetime.datetime.now()
        d_str = d1.strftime("%Y-%m-%d")
        file_output_d1={"date":d_str}
        json.dump(file_output_d1,fh2)
        #fh2.write(d_str)
        fh2.close()
        return d_str
#loads,dumps  
def read_license_expiry_date_file():
    try:
        fe1 = open("license_expiry_date1.txt","r")
        lines_txt = fe1.readlines()
        line_d1 = json.loads(lines_txt[0])
        fe1.close()
        #return lines_txt[0]
        return line_d1['date']
    except FileNotFoundError as error1:
        d1 = datetime.datetime.now()
        td=timedelta(days=90)
        d2=d1+td
        d2_str=d2.strftime("%Y-%m-%d")
        fe2=open("license_expiry_date1.txt","w")
        #fe2.write(d2_str)
        d2={'date':d2_str}
        fe2.write(json.dumps(d2))
        fe2.close()
        return d2_str

license_taken_date = write_read_license_date_file()
print("License_taken_date : {} ".format(license_taken_date))
license_expiry_date = read_license_expiry_date_file()
todays_date = datetime.datetime.now()
todays_date_str = todays_date.strftime("%Y-%m-%d")
if todays_date_str == license_expiry_date:
    print("License expired, Please renew license")
else:
    print("License is valid")
