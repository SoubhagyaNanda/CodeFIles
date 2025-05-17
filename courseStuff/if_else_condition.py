

di = {"page": 2, "per_page": 6, "total": 12, "total_pages": 2, "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}

# Fetch the first name and last name of the user with the email id tobias.funke@reqres.in.
'''
for key, value in di.items():
    if key == 'data':
        for user in value:
            if user['email'] == 'tobias.funke@reqres.in':
                print(user['first_name'],user['last_name'])
'''

# Count the total number of users with avatar URLs containing the substring faces.

# Retrieve all user ids whose first name starts with the letter M.
'''
for key, value in di.items():
    if key == 'data':
        for user in value:
            if user['first_name'][0] == 'M':
                print(user['id'])
'''

# List all the full names (first and last names combined) of users.
'''lik= []
for user in di['data']:
    kit = user['first_name']+" "+user['last_name']
    lik.append(kit)
print(lik)'''

'''import practice
armstrong()'''
