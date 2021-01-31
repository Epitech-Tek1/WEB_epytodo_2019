#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## models
##

from app import *
from flask import *
import hashlib
import time
from datetime import datetime

class user(object):
    def     __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.tb = "user"

    def     check_exist(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM %s WHERE username = '%s'" % (self.tb, username))
            exist = cursor.fetchone()[0]
            cursor.close()
            return (False, True)[exist]
        except (Exception) as e:
            print(e)
            return False
        return False

    def check_password(self, password, psswd):
        return (True, False)[password != psswd]

    def signup(self, username, email, password):
        salt = self.app.config['PASSWORD_SALT']
        try:
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            pass_crypt = hash.hexdigest()
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO %s (username, email, password) VALUES ('%s', '%s', '%s')" % (self.tb, username, email, pass_crypt))
            self.connection.commit()
            cursor.close()
        except (Exception) as e:
            print(e)

    def     get_user_id(self, username):
        try:
            curor = self.connection.cursor()
            curor.execute("SELECT user_id FROM %s WHERE username = '%s'" % (self.tb, username))
            user_id = curor.fetchone()[0]
            curor.close()
        except (Exception) as e:
            print(e)
        return user_id

    def     check_account(self, username, password):
        try:
            curor = self.connection.cursor()
            curor.execute("SELECT password FROM %s WHERE username = '%s'" % (self.tb, username))
            password = curor.fetchone()[0]
            curor.close()
            salt = self.app.config['PASSWORD_SALT']
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            digest = hash.hexdigest()
            return True if digest == password else False
        except (Exception) as e:
            print(e)

class task(object):
    def     __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.tb = "user_has_task"
        self.tb_task = "task"

    def     get_task(self, user_id):
        task = []
        try:
            curor = self.connection.cursor()
            curor.execute("SELECT fk_task_id FROM %s WHERE fk_user_id = '%d'" % (self.tb, user_id))
            ids = list(curor.fetchall())
            curor.close()
            for id in ids:
                curor = self.connection.cursor()
                curor.execute("SELECT * FROM %s WHERE task_id = '%d'" % (self.tb_task, id[0]))
                tasks = list(curor.fetchall()[0])
                task.append(tasks)
                curor.close()
            return task
        except (Exception) as e:
            print(e)
        return task

    def     delete_task(self, task_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM %s WHERE fk_task_id = %d AND fk_user_id = %d" % (self.tb, task_id, session['user_id']))
            self.connection.commit()
            cursor.close()
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM %s WHERE task_id = %d" % (self.tb_task, task_id))
            self.connection.commit()
            cursor.close()
        except (Exception) as e:
            print(e)
            return False
        return True

    def     add_task(self, title, begin, end, status):
        try:
            if not begin == 'None' and not begin == None and not end == 'None' and not end == None:
                cursor = self.connection.cursor()
                format = '%Y-%m-%d'
                new_format = '%Y-%m-%d'
                datetime.strptime(begin, format).strftime(new_format)
                datetime.strptime(end, format).strftime(new_format)
                cursor.execute("INSERT INTO %s (title, begin, end, status) VALUES ('%s', '%s', '%s', '%s')" % (self.tb_task, title, begin, end, status))
                self.connection.commit()
                id = cursor.lastrowid
                cursor.close()
                if not id: return False
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO %s (fk_user_id, fk_task_id) VALUES (%d, %d)" % (self.tb, session['user_id'], id))
                self.connection.commit()
                cursor.close()
        except (Exception) as e:
            print(e)
            return False
        return True

    def     set_task(self, task_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE %s SET status='%s' WHERE task_id=task_id" % (self.tb_task, "done"))
            self.connection.commit()
            cursor.close()
        except (Exception) as e:
            print(e)
            return False
        return True