from gluon import *
from gluon.tools import Auth, Crud, Service

#def as_first_func():
#    print "hallo welt"
#    return 0

#def foo_msw():
#    current.hallo = "hallo"
#    #return current.hallo
#    return current.request.client

# does not work????
def ip():
    return current.request.client
#    return "hallo"

#works????
#def ip2():
#    return current.request.client
#    #return "hallo"

def make_testform():
    print "hello world"
    form = FORM('Your name:', INPUT(_name='name'), INPUT(_type='submit'))
    #return current.request.client
    return form