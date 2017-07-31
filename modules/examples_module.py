# -*- coding: utf-8 -*-

from gluon import *

def func_in_module():
     return current.request.client

# write functions
def foo(): return 'hello world'
def more_complex():
    form = FORM('Your name:', INPUT(_name='name'), INPUT(_type='submit'))
    return form

# ... now go to your controller and use the functionality
# example:
#do_not_uncomment# import examples_module           # (write this code in your controller-file)
#do_not_uncomment# def callfoo(): return foo()  # (write this code in your controller-file)
