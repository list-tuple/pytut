import json
import requests
response = requests.get("https://gorest.co.in/public/v2/users")
print(response.status_code)

reponse_body=response.text
response_obj=json.loads(reponse_body)
print(type(response_obj))

for i1 in response_obj:
    print(i1["name"])
for i1 in response_obj:
    print(i1["email"])
