#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## controller
##

from app import *
from app.models import *
from app.api import *
from flask import *

class controller_root(object):
    def __init__(self, app):
        self.app = app
    def render_index(self):
        return render_template('index.html')

class controller_profil(object):
    def __init__(self, app):
        self.app = app
    def render_profil(self):
        return render_template('user/profil.html')

class controller_todolist(object):
    def __init__(self, app):
        self.app = app
    def render_todolist(self):
        return render_template('todolist/todolist.html')

class controller_signin(object):
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api = api(app, connection)
    def render_signin(self):
        return render_template('logs/signin.html')
    def signin(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.login_user(username, password)
        flash(json.loads(result))
        return redirect(url_for('route_index'))

class controller_signup(object):
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api = api(app, connection)
    def render_signup(self):
        return render_template('logs/signup.html')
    def signup(self, request):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        psswd = request.form['psswd']
        result = self.api.create_user(username, email, password, psswd)
        flash(json.loads(result))
        return redirect(url_for('route_index'))

class controller_signout(object):
    def     __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api = api(app, connection)
    def signout(self, request):
        username = session['username']
        user_id = session['user_id']
        result = self.api.signout_user(username)
        flash(json.loads(result))
        return redirect(url_for('route_index'))

class controller_task(object):
    def     __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.api = api(app, connection)
    def     all_task(self):
        task = self.api.get_all_task(session['user_id'])
        task = json.loads(task)
        return render_template("/todolist/todolist.html", task=task['result'])
    def     delete_task(self, task_id):
        result = self.api.delete_task(task_id)
        flash(json.loads(result))
        return redirect(url_for('route_all_task'))
    def     add_task(self, request):
        title = request.form['title']
        begin = request.form['begin']
        end = request.form['end']
        status = request.form['status']
        result = self.api.add_task(title, begin, end, status)
        flash(json.loads(result))
        return redirect(url_for('route_all_task'))
    def     set_task(self, task_id):
        result = self.api.set_task(task_id)
        flash(json.loads(result))
        return redirect(url_for('route_all_task'))