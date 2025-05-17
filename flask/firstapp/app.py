from flask import Flask, request, session, render_template
app = Flask(__name__)
app.secret_key='SOME KEY'

@app.route('/')
def index1():
    return render_template('index1.html')

#we can give different names to a webpage
@app.route('/home')
def page():
    return 'This is home page', 200

#Dynamic webserver
@app.route('/greet/<nm>')
def dynamic(nm):
    return f'hello {nm}'

# Adding numbers in webserver
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f'{num1}+{num2} = {num1+num2}'

# url parameters
# http://127.0.0.1:5555/parameters?greetings=hello&name=mike (This is how you give url parameters)
@app.route('/parameters')
def params():
    if 'greetings' in request.args.keys() and 'name' in request.args.keys():
        greetings = request.args['greetings']
        name= request.args.get('name')

        return f'{greetings},{name}'
        # return request.args
    else:
        return 'Missing key value'

''' 
Note-----
GET - It is used to Show you webpages in the server.
POST - It is used to handel submited data from the webserver.
PUT- It is used to update any info from the webserver.
Delete- It is used to delete data.
'''


if __name__=='__main__':
    app.run(host='127.0.0.1', port =5555, debug=True)