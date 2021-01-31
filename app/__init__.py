#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## __init__
##

import os
from app import *
from flask import Flask
from app.controller import *
from app.connection import *

# Config flask module
app = Flask(__name__)
app.config.from_object('config')

# Config db
connection = connection_manager(app)

def gconnection():
    return connection.gconnection()