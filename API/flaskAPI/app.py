from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
from datetime import timedelta
import uuid
# from django.http import HttpResponse

database=[]


app= Flask(__name__)
app.secret_key= 'heybuddy'
app.config['JWT_SECRET_KEY']= 'jwtsecretkey'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
jwt= JWTManager(app)


# Homepage
@app.route('/')
def index():
    return redirect(url_for('signup'))

#Signup page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        data= request.form
        user= {
            'id':str(uuid.uuid4()),
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'email': data['email'],
            'phone':data['phone'],
            "password": data['password'],
        }
        database.append(user)
        return redirect(url_for('login'))
    return render_template('signup.html')

#Login Page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        username= request.form['username']
        password= request.form['password']

        for user in database:
            if user['email']==username and user['password']==password:
                access_Token = create_access_token(identity= username)
                return redirect(url_for('dashboard', token=access_Token))
        return 'Invalid User'
    return render_template('login.html')

#Dashboard
@app.route('/dashboard')
@jwt_required()
def dashboard():
    return render_template('dashboard.html')

#Get User Data
@app.route('/api/user', methods=["GET"])
@jwt_required()
def get_user():
    return jsonify(database), 200


#Create User
@app.route('/api/user', methods=["POST"])
@jwt_required()
def createUser():
    data= request.get_json()
    data['id']= str(uuid.uuid4())
    database.append(data)
    return jsonify({
        'message': 'User Added Successfully',
        'Data': data
    }), 201

#Update User
@app.route('/api/user/<email>', methods=["PUT"])
def updateUser(email):
    data= request.get_json()
    for user in database:
        if user['email'] == email:
            user.update(data)
            return jsonify({'message': 'User Update', 'data': user}), 200
    return jsonify({'Message': 'User Not Found'}), 404


#Patch user
@app.route('/api/user/<email>', methods=["PATCH"])
@jwt_required()
def patchUser(email):
    data = request.get_json()
    for user in database:
        if user['email']==email:
            user.update(data)
            return jsonify({'message':'User patched', 'data': user}), 200
    return jsonify({'message': 'User not Found'}), 404

#Delete user
@app.route('/api/user/<user_id>', methods=["DELETE"])
@jwt_required()
def delete(user_id):
    global database
    database= [user for user in database if user['id']!=user_id]
    return jsonify({'Message': 'User Deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)