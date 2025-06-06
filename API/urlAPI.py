from flask import request
import requests

url= 'http://127.0.0.1:5000/posts'

payload= {
    'title': 'ABC',
    'body' : 'XYZ'
}
response= requests.post(url, json=payload)

print(response.status_code)
print(response)

response1= requests.get(url)
print(response1.status_code)
print(response1.json())