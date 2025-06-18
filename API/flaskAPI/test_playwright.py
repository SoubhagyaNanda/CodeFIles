from playwright.sync_api import sync_playwright
BASE_URL= "http://127.0.0.1:5000"

LOGIN_DATA = {
    "username": "abc@gmail.com",
    "password": "abc@123"
}

def run(playwright):
    request_context = playwright.request.new_context()

    # Login Token
    login_response = request_context.post(f"{BASE_URL}/login", data=LOGIN_DATA)
    assert login_response==302, 'Login Failed'

    redirect_url= login_response.headers.get("LOCATION", "")
    token= redirect_url.split("token=")[1] if "token=" in redirect_url else None
    assert token, 'Token Not Found'

    headers= {
        "Authorizations": f"Bearer {token}"
    }

    #Get Request
    # get_res= request_context.get(f"{BASE_URL}/api/user", headers=headers)
    # print("Get Response", get_res.status, get_res.json())

    #Post Request
    post_data = {
        "firstname": "Soubhagya",
        "lastname": "Nanda",
        "email": "abcd@gmail.com",
        "phone": "7750819477",
        "password": "abcd@123",
    }
    post_res= request_context.post(f"{BASE_URL}/api/user", headers=headers, data=post_data)
    print('POST Response', post_res.status, post_res.json())



with sync_playwright() as playwright:
    run(playwright)