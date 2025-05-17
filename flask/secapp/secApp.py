from flask import Flask, render_template, session, make_response, request

secApp= Flask(__name__)
secApp.secret_key='SOME KEY'


@secApp.route('/')
def index():
    return render_template('index.html', message='Index')


@secApp.route('/set_data')
def set_data():
    session['name']= 'RaviGupta'
    session['passion']='Youtuber'
    return render_template('index.html', message='Session Data.')

@secApp.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'passion' in session.keys():
        name= session['name']
        passion= session['passion']
        return render_template('index.html', message=f'name:{name},passion:{passion}')
    else:
        return render_template('index.html', message='No session found')

@secApp.route('/clear')
def clear():
    session.clear()
    return render_template('index.html', message='Session cleared.')

@secApp.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set.'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@secApp.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'cookie value:{cookie_value}')

@secApp.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Remove cookie.'))
    response.set_cookie('cookie_name', expires=0)
    return response

@secApp.route('/')
def sql_data():
    pass

if __name__ == '__main__':
    secApp.run(host='0.0.0.0', debug=True)