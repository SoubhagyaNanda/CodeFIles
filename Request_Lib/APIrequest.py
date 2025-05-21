from http.client import responses

import requests

# response= requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# print(response.json())

# Filtering Data
'''params = {'userId': 2}
response= requests.get("https://jsonplaceholder.typicode.com/posts", params)
print(response.status_code)
print(response.json())'''

# Post request
'''data = {'title': 'Hello', 'body': 'World', 'userId':101}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)
print(response.json())'''

# Error handling
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response)
except requests.exceptions.RequestException as e:
    print("Errror: ", e)