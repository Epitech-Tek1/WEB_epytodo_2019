#!/usr/bin/env python3
#coding:utf-8
##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019 [WSL: Debian]
## File description:
## run
##

import os
from app import views
from app import app

if __name__ == "__main__":
    os.urandom(24)
    app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    app.run()