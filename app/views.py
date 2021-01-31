#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## views
##

from app import *

@app.route('/', methods=['GET'])
def     route_index():
    controller = controller_root(app)
    return controller.render_index()

@app.route('/user/profil.html', methods=['GET'])
def     route_profil():
    controller = controller_profil(app)
    return controller.render_profil()

@app.route('/logs/signin', methods=['GET'])
def     route_signin_render():
    controller = controller_signin(app, gconnection())
    return controller.render_signin()

@app.route('/logs/signup', methods=['GET'])
def     route_signup_render():
    controller = controller_signup(app, gconnection())
    return controller.render_signup()

@app.route('/logs/signin', methods=['POST'])
def     route_signin():
    controller = controller_signin(app, gconnection())
    return controller.signin(request)

@app.route('/logs/signup', methods=['POST'])
def     route_signup():
    controller = controller_signup(app, gconnection())
    return controller.signup(request)

@app.route('/logs/signout', methods=['GET'])
def     route_signout():
    controller = controller_signout(app, gconnection())
    return controller.signout(request)

@app.route('/todolist/todolist', methods=['GET'])
def     route_all_task():
    controller = controller_task(app, gconnection())
    return controller.all_task()

@app.route('/todolist/todolist/del/<int:task_id>', methods=['POST'])
def     route_delete_task(task_id):
    controller = controller_task(app, gconnection())
    return controller.delete_task(task_id)

@app.route('/todolist/todolist/add/', methods=['POST'])
def     route_add_task():
    controller = controller_task(app, gconnection())
    return controller.add_task(request)

@app.route('/todolist/todolist/set/<int:task_id>', methods=['POST'])
def     route_set_complet(task_id):
    controller = controller_task(app, gconnection())
    return controller.set_task(task_id)