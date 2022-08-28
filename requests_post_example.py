import requests
import json


headers={"Authorization": "Bearer 50a9401d9598c69e94e906188f497fcadd1feab941fba66ca38926fd91ff8d03"}
url="https://gorest.co.in/public/v2/users"
data={"name":"raghuram Ramakrishna", "gender":"male",\
      "email":"raghuram.ramakrishna@15ce.com", "status":"active"}

response = requests.post(url=url,headers=headers,data=data)

print(response.status_code)
response_text = response.text
d1=json.loads(response_text)
print(d1)
