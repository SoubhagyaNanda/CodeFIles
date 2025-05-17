from base64 import decode
import pandas as pd
from flask import Flask, render_template, request, session
from pyexpat.errors import messages

new1 = Flask( __name__ , template_folder='templates', static_folder='static', static_url_path='/')
new1.secret_key= 'SOME KEY'

@new1.route('/')
def index():
    mylist = [10,30,50]
    return render_template('index.html',mylist=mylist)

@new1.route('/other')
def other():
    mytext = 'Hello world'
    return render_template('other.html', context=mytext)

@new1.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@new1.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username== 'Soubhagya' and password== '123':
            return 'success'
        return 'failure'


@new1.route('/files', methods=['POST','GET'])
def file_upload():
    file = request.files['file']
    if file.content_type=='text/plain':
        return file.read().decode()
    elif file.content_type== "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type== "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()


@new1.route('/files_setting')
def post():
    return render_template('files_settings.html')


if __name__=='__main__':
    new1.run(host='0.0.0.0', debug=True)