####################
# examples: by msw #
####################


#  import things if you need them
from gluon import * # is this really needed, as we import also in the model, hmmm?


##########################################
# 'Global' settings in a controller file #
##########################################

# ??? what is the convention (they are seen for this model/controller??)

#  speciality of asylum app. the current language of the user is stored in the 'session' object
if not session.my_language:
    pass
else:
    T.force(session.my_language)

###############
# First steps #
###############

# you should always have a 'index' controller (the default, if no fuction is given in the url)
def index():
    # returning a dict(...) means that web2py will look for a
    # corresponding ../views/<controller>/<function>.html file and call/evaluate/render it

    linklist = UL(

        LI(A('', 'my_first_controller', _href=URL('my_first_controller')), _class='test', _id=0),
        LI(A('', 'callhelpers', _href=URL('callhelpers')), _class='test', _id=0),
        LI(A('', 'test_view', _href=URL('test_view')), _class='test', _id=0),
        LI(A('', 'pythonexamples', _href=URL('pythonexamples')), _class='test', _id=0),
        LI('Forms:'),
        LI(A('', 'form', _href=URL('form')), _class='test', _id=0),
        LI(A('', 'sqlform', _href=URL('sqlfrom')), _class='test', _id=0),
        LI(A('', 'formfactory', _href=URL('formfactory')), _class='test', _id=0),
        LI(),

        LI(A('', 'showbooleffect', _href=URL('showbooleffect')), _class='test', _id=0),
        LI(A('', 'show_examples_fieldtypenquery', _href=URL('show_examples_fieldtypenquery')), _class='test', _id=0),
        LI(A('', 'populate_examples_fieldtypenquery', _href=URL('populate_examples_fieldtypenquery')), _class='test', _id=0),
        LI(A('DOES NOT WORK:', 'examples_fieldtypenquery_drop', _href=URL('examples_fieldtypenquery_drop')), _class='test', _id=0),
        LI(A('', 'examples_request_playing', _href=URL('examples_request_playing')), _class='test', _id=0),
        LI(A('Calling a function from a module:', 'call_foo', _href=URL('call_foo')), _class='test', _id=0),
        LI(A('Calling a function from a module:', 'call_more_complex', _href=URL('call_more_complex')), _class='test', _id=0),
        #LI(A('', '', _href=URL('')), _class='test', _id=0),

        #LI(A('', '', _href=URL('')), _class='test', _id=0),
                )
    return locals()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():
    response.flash = "There was an error"

    # msw: is there a way to retrieve here in this function an meaningful error message?
    err_mes = T('please figure out how to write a meaningful error message from within this function')
    return dict(err_mes=err_mes)



###################
# Python examples #
###################

# This is just a list of some python examples (how to ...)
def pythonexamples():

    # convert a list into a dict:
    lst=('dog','cat','mouse')
    mydict = {k: v for k, v in enumerate(lst)}
    print "mydict:",mydict

    # concatenate strings
    h = "hello"
    w = "world"
    c_1 = h+w
    c_2 = "this is the %s example of the %s" % (h,w)
    print c_1
    print c_2

    # loop and cont at the same time
    my_lst = ['a',9999,'hugo']
    for i, val in enumerate(my_lst):
        print 'number %d, value %s' % (i, val)


    return locals()

##############################################
# Basics on controllers (an other functions) #
##############################################

# Controllers are functions. where
# - their name refers to the calling URL
# - they do NOT have parameters
#
# if controllers return a dictionary, a view.html is taken for further info

# this is a controller, called via the URL "http://127.0.0.1:8000/Asylum/examples/my_first_controller
# if it returns a string or a dict, it is rendered with the help of ../views/examples/my_first_controller.html
def my_first_controller():
    text_to_display = "This is my first communication with a view file, ..., hi view-file!"
    return dict(text_to_display=text_to_display) # string

# you can push variables from the action to the view via a dict
def communication():
    singledict = {"key": "value"}
    return singledict # dict


# - controller functions with parameters or which start with '__' are not callable via an URL. they are 'helpers'
#   and must be called from within a real controller
def foo1(tmp=9):
    return 'foo1: the value of tmp is: %d' % tmp

def __foo2():
    return 'you called __foo2!'

def callhelpers():
    retdict = {'foo1' : foo1(), 'foo2' : __foo2()}
    return retdict

####################
# The view helpers #
####################

# this could one day be a long example list of the web2py view helpers
def test_view():
    a = DIV(SPAN('a', 'b'), 'c')
    code=CODE("print code",styles={'CODE':'margin: 0;padding: 5px;border: none;'})
    markmin = MARKMIN("``abab``:custom", extra=dict(custom=lambda text: text.replace('a', 'c')))
    textarea = TEXTAREA('hallo du schoener hase', _class="test")

    return locals()
# --------------
def test_view_action():
    retval = "Hello World"
    return dict(retval=retval)

###################
# Forms and Grids #
###################

# --------------
def form():
    #example of a form
    form = "Please implement code for form"
    return dict(form=form)

# --------------
def sqlfrom():
    form = "Please implement code for sqlform"
    return dict(form=form)

# --------------
def formfactory():
    form = "Please implement code for formfactory"
    return dict(form=form)


########################################
# Widget, redirect, session and others #
########################################

# - create and show a SQLFORM
# - set a black border for the form
# - validate form and retrieve the results, store results in 'session'
# - redirect to the next page and show results there
def widget_examples():

    form = SQLFORM.factory(
        Field('name', requires=IS_NOT_EMPTY()),
        Field('sex', requires=IS_IN_SET(['female','male','other'])),
        Field('yesno', type='boolean', widget = SQLFORM.widgets.boolean.widget),
        #Field('comment', 'string', widget=SQLFORM.widgets.text.widget)
        Field('blautext', type='string',
              widget = lambda field,value: SQLFORM.widgets.string.widget(field,value,_style='color:blue')),
        Field('radio', requires=IS_IN_SET(['a','b','c','hund']),
              widget = lambda field,value: SQLFORM.widgets.radio.widget(field,value, style='table')),
                                                                            #''"table", "ul", or "divs"),
    )
    form['_style']='border:1px solid black'

    #if form.accepts(request,session):
    if form.process().accepted:

        response.flash = 'form accepted'
        session.mswname = form.vars.name
        session.mswsex = form.vars.sex
        session.mswyesno = form.vars.yesno
        session.mswblautext = form.vars.blautext
        session.mswradio = form.vars.radio
        redirect(URL('widget_examples_results'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'


    return dict(form=form)


#SQLFORM.widgets.string.widget
#SQLFORM.widgets.text.widget
#SQLFORM.widgets.password.widget
#SQLFORM.widgets.integer.widget
#SQLFORM.widgets.double.widget
#SQLFORM.widgets.time.widget
#SQLFORM.widgets.date.widget
#SQLFORM.widgets.datetime.widget
#SQLFORM.widgets.upload.widget
#SQLFORM.widgets.boolean.widget
#SQLFORM.widgets.options.widget
#SQLFORM.widgets.multiple.widget
#SQLFORM.widgets.radio.widget
#SQLFORM.widgets.checkboxes.widget
#SQLFORM.widgets.autocomplete

# --------------------
def widget_examples_results():
    langlist = (session.mswname,
    session.mswsex,
    session.mswyesno,
    session.mswblautext,
    session.mswradio,)
    resultdict = {k: v for k, v in enumerate(langlist)}

    return locals()



##################################
# 'Manually; display information #
##################################

# manually display a person (give id-number as first arg: e.g. asylum/msw/display_form/2)
# uses list_records() defined below
# taken from book, ch 7, "Links to referencing records"
def display_form():
    record = db.examples_person(request.args(0)) or redirect(URL('index'))
    url = URL('download')
    link = URL('list_records', args='db')

    # make the form
    form = SQLFORM(db.examples_person, record, deletable=True,
                  upload=url, linkto=link,
                  labels = {'examples_dog.dog_owner':"This person's dogs"})

    # make an extra element
    my_extra_element = TR(LABEL('I agree to the terms and conditions'),
                         INPUT(_name='agree',value=True,_type='checkbox'))
    form[0].insert(-1,my_extra_element)

    # process the form
    if form.process().accepted:
        response.flash = 'form accepted'

        print "form.vars.agree:",form.vars.agree

        if form.vars.agree == 'on':
            print "checkbox was 'on'!"
        elif form.vars.agree == None:
            print
            "checkbox was 'None'!"
        else:
            print "very strange"

    elif form.errors:
        response.flash = 'form has errors'

    return dict(form=form)

# ---------------------------------
#
# taken from book, ch 7, "Links to referencing records"
# this function is called from within display_form() (see above)
def list_records():
    import re
    REGEX = re.compile('^(\w+).(\w+).(\w+)\=\=(\d+)$')
    match = REGEX.match(request.vars.query)
    if not match:
        redirect(URL('error'))
    table, field, id = match.group(2), match.group(3), match.group(4)
    records = db(db[table][field]==id).select()
    return dict(records=records)

# --------------------
# use a grid to display all persons
@auth.requires_login()
def grid_person():
    grid = SQLFORM.grid(db.examples_person)
    return locals()

##########
# Manage #
##########
# manage any table using a grid, give table name as arg(0), e.g. .../<app>/<controller>/examples_manage/<table_name>
@auth.requires_login()
def examples_manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table], args=request.args[:1],)
    return locals()

# --------------------
@auth.requires_login()
def two_tables():
    form = SQLFORM.grid(db.examples_checklist,left=db.examples_human.on(db.examples_human.checklist==db.examples_checklist.id))
    return dict(form=form)

# --------------------
@auth.requires_login()
def two_smart_tables():
    form = SQLFORM.smartgrid(db.examples_checklist,linked_tables=['examples_human'])
    #form = SQLFORM.smartgrid(db.examples_human, linked_tables=['examples_checklist','examples_mobility'])
    #form = SQLFORM.smartgrid(db.examples_human, linked_tables=['examples_checklist'])

    return dict(form=form)

# --------------------
#@auth.requires_membership('managers')
@auth.requires_login()
def powermanage():
    table = request.args(0) or 'auth_user'
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.smartgrid(db[table],args=request.args[:1])
    return locals()
# --------------------
# show two (linked) tables together (using a grid)
@auth.requires_login()
def person_and_dog():
    grid = SQLFORM.grid(db.examples_person,left=db.examples_dog.on(db.examples_dog.dog_owner==db.examples_person.id))

    return locals()

# --------------------
# show two (linked) tables together (using a smartgrid)
@auth.requires_login()
def person_and_dog_smart():
    grid = SQLFORM.smartgrid(db.examples_person,linked_tables=['examples_dog'])
    return locals()

# --------------------
# show three (linked) tables together (using a smartgrid)
@auth.requires_login()
def person_dog_thing_smart():
    grid = SQLFORM.smartgrid(db.examples_person,linked_tables=['examples_dog','examples_thing'])
    return locals()

#
# -----------------------
#

def examples_pbase():

    form = SQLFORM(db.examples_pbase,
                deletable=True, # creates the delete checkbox
                submit_button = 'Please submit this msw',
                showid=True,
                #fields = ['name'],
                #col3 = {'name':A('what is this?', _href='http://www.google.com/search?q=define:name'),'firstname':"This is the col3!"},
                formstyle = 'bootstrap3_inline',
                    #formstyle = "bootstrap3_stacked",
                    #formstyle = "bootstrap2", does not exist
                    #formstyle="table3cols",
                    #formstyle="table2cols",
                    #formstyle="ul",
                    #formstyle="divs",
                    #formstyle="bootstrap",

                    #buttons=[INPUT(_name='test', _value='a', value='b'),
                    #         TAG.button ('Next',_type="submit"),
                    #         TAG.button('Back',_type="button",_onClick = "parent.location='%s' " % URL('index')),
                    #         A("Go to another page",_class='btn',_href=URL("default","index")),]
                   )
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    #mymenu = MENU([['One', False, 'link1', [['Two', False, 'link2']]]])
    #return dict(form=form,mymenu=mymenu)
    return dict(form=form)

# --------------------------
def display_examples_pbase():
   record = db.examples_pbase(request.args(0)) or redirect(URL('index'))

   form = SQLFORM(db.examples_pbase, record,
                  deletable=True, # creates the delete checkbox
                  )

   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(form=form)


# from book: the use of a smartgrid!!
# --------------------------
def display_examples_child():
    record = db.examples_child(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.examples_child, record, deletable=True)

    if form.process().accepted: response.flash = 'form accepted'
    elif form.errors: response.flash = 'form has errors'
    else: response.flash= 'form shown for the first time'

    return dict(form=form)

@auth.requires_login()
def parentmanager():
    #form = SQLFORM.grid(db.parent)
    #form = SQLFORM.grid(db.child)
    #form = SQLFORM.grid(db.parent,left=db.child.on(db.child.parent==db.parent.id))
    form = SQLFORM.smartgrid(db.parent,linked_tables=['child', 'car', 'job'])

    return dict(form=form)

#
# show a field dependig on a switch (possibly in the same table)
#
def showbooleffect():

    db.examples_booltest.moreinfo1.show_if = (db.examples_booltest.showbool == True)
    db.examples_booltest.moreinfo2.show_if = (db.examples_booltest.showbool == True)

    # or try this
    #print 'request.args:' type(request.args)
    #print 'request.vars:' type(request.vars)


    form = SQLFORM.grid(db.examples_booltest)
    return locals()

#
# field types, drop/prepopulate and simple queries
#
def show_examples_fieldtypenquery():

    form = SQLFORM.grid(db.examples_fieldtypenquery2)
    return locals()

def populate_examples_fieldtypenquery():

    # ask for the number of new entries via a simple FORM
    form = FORM('How many entries should I create:',
              INPUT(_name='nofentries', requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(1,1e4)]),
              INPUT(_type='submit')
                )

    # process and validate the form, if number correct, populate table and redirect to the controller/page of this table
    if form.process().accepted:
        from gluon.contrib.populate import populate

        populate(db.examples_fieldtypenquery2, form.vars.nofentries)

        session.flash = 'entries created'
        redirect(URL('show_examples_fieldtypenquery'))

    elif form.errors: response.flash = 'form has errors'
    else: response.flash = 'please fill the form'

    # if you like, add some buttons just because you know how to do it
    form.add_button('Index', URL('index'))
    form.add_button('web2py', 'http://www.web2py.com')

    return dict(form=form)

def examples_fieldtypenquery_drop():
    # something strange with 'drop'. i can drop the table, however the data seems to still be there. this could be
    # due to the comment below. removing files like "examples_fieldtypenquery.table does not seem to have an effect:
    # the data is still in the browser (cache?). running the fuction again gives a very bad ticket and sais:
    # OperationalError: table "examples_fieldtypenquery" already exists
    # my suspicion is, that the list:integer fields use some workaround to emulate their behaviour - and this
    # seem to still have some 'remnants' to the 'droped' table.
    # please investigate this further, as it is not good to not be able to drop a table

    # drop the table
    #if db(db.examples_fieldtypenquery.id).count() > 3:
    #    db.examples_fieldtypenquery.drop()

    # ... however (see book, chapter DAL): Note for sqlite: web2py will not re-create the dropped table until you
    # navigate the file system to the databases directory of your app, and delete the file associated
    # with the dropped table.

    import os
    cwd = os.getcwd() # get current working directory
    print cwd
    #db_filename =

    #os.remove(db_filename)

#
# request.args and request.vars
#

# - request.args is a list, args follow after main path a/c/f/arg0/arg1/arg0
# - request.vars is a dictionary. they follow after a '?' (questionmark), like ...?var0=9
# - request.args[i] raises exception while request.args(i) returns 'None'

def examples_request_playing():

    # you always get this info (however, in most cases you should know where you are)
    requapp = request.application
    requcon = request.controller
    requfun = request.function

    arg0=-999
    arg9999 = -999
    arglist = []
    arg0different = -999

    if request.args(0)==None:
        print 'you have no request.arg entries'
    else:
        print request.args
        arg0 = request.args(0)
        arg9999 = request.args(9999) # None
        #arg9999 = request.args[9999]  # if you use [9999] you get a ticket
        arg0different = request.args[:1]
        for a in request.args:
            arglist.append(a)

    var0 = -999
    vardict = request.vars

    if len(request.vars)<=0:
        print 'you have no request.vars'
    else:
        #var0 = request.vars(0) #makes no sense, as dicts have no order
        for key, value in request.vars.iteritems():
            print 'key=%s, value=%s' % (key,value)



    ## and there is the request.env object:
    env_path = request.env.path_info
    env_dict = request.env

    return locals()

#
# writing your own modules
#

# place a file in ../modules/<examples_module>.py
#    - import gluon stuff: from gluon import *
#    - write fuctions/classes: def foo(): return 'hello world'
#
# include and use it:
import examples_module

def call_foo():
    return examples_module.foo()

def call_more_complex():
    form = examples_module.more_complex()
    return dict(form=form)

