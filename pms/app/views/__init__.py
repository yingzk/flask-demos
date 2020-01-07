from flask import session, render_template, request, redirect

from app import create_app
from app.models import UserModel, RoleModel

app = create_app()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = UserModel.login(request.form)
    session['user'] = user
    # 默认选择第一个角色登录
    session['current_role'] = user['roles'][0]['id']
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return '<p>logout success.</p> return to <a href="/">index</a> or <a href="/login">login</a>.'


@app.route('/change_role', methods=['POST'])
def change_role():
    form = request.form
    session['current_role'] = int(form['role'])
    return redirect('/')


@app.route('/')
@app.route('/index')
def index():
    page_data = {}
    if 'current_role' in session:
        page_data['menu'] = RoleModel.get_menu(session['current_role'])
    return render_template('index.html', **page_data)
