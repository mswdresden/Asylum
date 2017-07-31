#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon import *
from gluon import current
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM
from gluon.validators import IS_NOT_EMPTY, IS_EMAIL, IS_LENGTH

def ip(): return current.request.client

def ip2():
    print "hello world"
    form = FORM('Your name:', INPUT(_name='name'), INPUT(_type='submit'))
    #return current.request.client
    return form

def huhu():
    return "hello world"
