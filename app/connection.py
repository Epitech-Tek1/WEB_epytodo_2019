#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## connection
##

import pymysql as mysql

class connection_manager(object):
    def     __init__(self, app):
        self.app = app
        self.connection = None
        self.connect(app.config)

    def     connect(self, config):
        try:
            self.connection = mysql.connect(host=config[('DATABASE_SOCK', 'DATABASE_HOST')[config['DATABASE_SOCK'] == None]],
            user=config['DATABASE_USER'], password=config['DATABASE_PASS'], database=config['DATABASE_NAME'])
            if (self.connection): print("You're connected to MySQL")
            else: raise Exception
        except (Exception) as e:
            print("Error while connecting to MySQL", e)
            exit (84)
    def     gconnection(self):
        return self.connection