#gorest token 50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03

import requests

headers={"Authorization":"Bearer 50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03"}
data={"name":"Tenali Ramakrishna2", "gender":"male", \
      "email":"tenali1.ramakrishna@15ce.com", "status":"active"}
url= "https://gorest.co.in/public/v2/users"
response = requests.post(url=url,headers=headers,data=data)
print(response)
print(response.text)
"""
-d
'{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
"""
