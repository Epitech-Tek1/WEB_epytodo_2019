#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## api
##

from app import *
from app.models import *
from flask import *

class api(object):
    def     __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.user = user(app, connection)
        self.task = task(app, connection)
    def     create_user(self, username, email, password, psswd):
        ret = {}
        if not username and not email and not password:
            ret['error'] = "Veillez remplir tous les champs !"
        else:
            if not username.isalnum():
                ret['error'] = "Votre username doit contenir que des lettres !"
            else:
                if self.user.check_exist(username):
                    ret['error'] = "Cet username est déjà utilisé !"
                else:
                    if not self.user.check_password(password, psswd):
                        ret['error'] = "Vos mots de passes ne correspondent pas !"
                    else:
                        self.user.signup(username, email, password)
                        ret['result'] = "Bienvenue sur Epytodo %s !" % (username)
        return json.dumps(ret)

    def     login_user(self, username, password):
        ret = {}
        if not username and not password:
            ret['error'] = "Veillez remplir tous les champs !"
        else:
            if not self.user.check_exist(username):
                ret['error'] = "Ce compte n'exist pas !"
            else:
                if self.user.check_account(username, password):
                    ret['error'] = "Ce mot de passe ne correspond pas au compte !"
                else:
                    session['username'] = username
                    session['user_id'] = self.user.get_user_id(username)
                    ret['result'] = "Welcome Back %s !" % (username)
        return json.dumps(ret)

    def     signout_user(self, username):
        ret = {}
        ret['result'] = "Good bye %s, See you later !" % (username)
        session.pop('username', None)
        session.pop('user_id', None)
        return json.dumps(ret)

    def     get_all_task(self, user_id):
        ret = {}
        result = self.task.get_task(user_id)
        ret['result'] = result
        return json.dumps(ret)

    def     delete_task(self, task_id):
        ret = {}
        if self.task.delete_task(task_id):
            ret['result'] = "Your task has been correctly deleted !"
        else:
            ret['error'] = "An error occured. Please try again !"
        return json.dumps(ret)

    def     add_task(self, title, begin, end, status):
        ret = {}
        if not title == None:
            if self.task.add_task(title, begin, end, status):
                ret['result'] = "Your task has been added !"
            else:
                ret['error'] = "Failed to add. Please try again !"
        return json.dumps(ret)

    def     set_task(self, task_id):
        ret = {}
        if self.task.set_task(task_id):
            ret['result'] = "Your task has been done !"
        else:
            ret['error'] = "Failed to edit. Please try again !"
        return json.dumps(ret)