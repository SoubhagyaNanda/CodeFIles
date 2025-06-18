import requests

BASE_URL= "http://127.0.0.1:5000"

LOGIN_DATA = {
    "username": "abc@gmail.com",
    "password": "abc@123"
}


def get_jwt():
    response= requests.post(f'{BASE_URL}/login', data=LOGIN_DATA, allow_redirects=False)
    if response.status_code==302 and 'token=' in response.headers.get('Location', ''):
        token= response.headers['Location'].split('token=')[1]
        print('jwt token', token)
        return token
    else:
        print('login failed', response.status_code)
        return None

token= get_jwt()

# def get_all_user(token):
#     headers= {'Authorization': f'Bearer {token}'}
#     response= requests.get(f'{BASE_URL}/api/user', headers=headers)
#     print(response.status_code)
#     print(response.json())
#
# get_all_user(token)

def post_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "firstname":"ram krishna",
        "lastname":"padhi",
        "email":"ram@gmail.com",
        "phone":"ram@123",
        "password":"ram@123"
    }

    response= requests.post(f'{BASE_URL}/api/user', json=data, headers=headers)
    print(response.status_code)
    print(response.json())

post_user(token)