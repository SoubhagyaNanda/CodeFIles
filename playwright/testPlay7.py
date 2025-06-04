import requests

# Get request
url='https://reqres.in/api/users?page=2'
response= requests.get(url)
# print(response.json())

# verification
'''if response.status_code==200:
    print(response.json())
else:
    print(f'Failed: {response.status_code}')'''


for i in range(1,11):
    params={'page':i}
    response= requests.get(url, params)
    print(f'pageNumber {i}', response.status_code)
# Params is a technical name where we used to get the data from server.


# Post method

# ++ If you want to create some data then it is called payload

payload = {
    "name": "morpheus",
    "job": "leader",
    "id": "549",
    "createdAt": "2025-06-03T02:13:23.890Z"
}

response = requests.post(url, json=payload)

# Verification
if response.status_code==201:
    print(response.json())
else:
    print(f'failed:', response.status_code)