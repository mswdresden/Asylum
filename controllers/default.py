# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

if not session.my_language:
    pass
else:
    T.force(session.my_language)

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(message=T('Welcome to the Afropa Databases!'))

# -----------------------------
def wiki():
    return auth.wiki()

# -----------------------------
def my_language():
    langs = T.get_possible_languages()
    for lang in langs:
        print "language:", lang

    # convert langs to a dict
    langdict = {k: v for k, v in enumerate(langs)}
    print langdict

    # works, but dictform below doesn't like numbers as keys in SQLFORMS ...
    # ... so now a simple test
    langs = dict(en='en', de='de', it='it')

    # use a radio button
    form = SQLFORM.factory(
        Field('language', requires = IS_IN_SET(['en','de','it','es', 'ar']),
              widget = lambda field,value: SQLFORM.widgets.radio.widget(field,value, style='table'))
    )

    if form.process().accepted:

        lang = form.vars.language
        T.force(lang)
        response.flash = T('Welcome to %s' % lang)
        # store result in session
        session.my_language = lang

    elif form.errors: response.flash = 'form has errors'
    else: response.flash = 'Choose a language'


    teststring = T("Hello World")

    return locals()




# -----------------------------
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
