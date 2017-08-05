# -*- coding: utf-8 -*-

#from gluon import *
from gluon import current
T = current.T
from validators import iban

#if not session.my_language:
#    pass
#else:
#    T.force(session.my_language)

# tip:
# tracebacks from errors in a validator are cryptic or not really findable. you can test a validator in
# the python shell:
# # python web2py.py -S Asylum -M
# >>> from customvalidators import IS_IBAN2_MSW

# this is only a test-validator for 'examples'
class IS_ISALPHA_MSW(object):
    def __init__(self, format='%s', error_message='must be alphastring (msw)!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        if value.isalnum():
            value = str(value)
            return (value, None)

        return (value, self.error_message)

    #def formatter(self, value):
    #    return value.str(str(self.format))


# this validator is used by the Asylum app
# for the time beeing, custom validators are flagged with '_CUSTOM',
# in order to not accidentally override a system validator (which may exist in the future)
class IS_IBAN_CUSTOM(object):
    def __init__(self, format='%s', error_message=\
        T('IBAN number not correct! use a number like DE29100500001061045672')):

        self.format = format
        self.error_message = error_message

    def __call__(self, value):

        if iban(value):
        #if 1==1:
            print '\t<I> IBAN is OK'
            return (value, None)

        print'\t <W> IBAN has errors'
        return (value, self.error_message)

    #def formatter(self, value):
    #    return value.str(str(self.format))
