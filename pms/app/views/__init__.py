from flask import session, render_template, request, redirect

from app import create_app
from app.models import UserModel

app = create_app()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = UserModel.login(request.form)
    session['user'] = user
    return redirect('/')


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return '<p>logout success.</p> return to <a href="/">index</a>.'


@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        menu = UserModel.get_menu(session['user']['id'], 4)
    else:
        menu = []
    return render_template('index.html', menu=menu)

# TODO 权限
