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

        LI(A('', 'index'			, _href=URL('index' 			   )), _class='test', _id=0),
        LI(A('', 'error'			    , _href=URL('error' 			   )), _class='test', _id=0),
        LI(A('', 'pythonexamples'		    , _href=URL('pythonexamples'		   )), _class='test', _id=0),
        LI(A('', 'my_first_controller'		    , _href=URL('my_first_controller'		   )), _class='test', _id=0),
        LI(A('', 'communication'		    , _href=URL('communication' 		   )), _class='test', _id=0),
        LI(A('', 'callhelpers'			    , _href=URL('callhelpers'			   )), _class='test', _id=0),
        LI(A('', 'test_view'			    , _href=URL('test_view'			   )), _class='test', _id=0),
        LI(A('', 'test_view_action'		    , _href=URL('test_view_action'		   )), _class='test', _id=0),
        LI(A('', 'form' 			    , _href=URL('form'  			   )), _class='test', _id=0),
        LI(A('', 'sqlform_basic'		    , _href=URL('sqlform_basic' 		   )), _class='test', _id=0),
        LI(A('', 'sqlform_v1'			    , _href=URL('sqlform_v1'			   )), _class='test', _id=0),
        LI(A('', 'formfactory'			    , _href=URL('formfactory'			   )), _class='test', _id=0),
        LI(A('', 'widget_examples'		    , _href=URL('widget_examples'		   )), _class='test', _id=0),
        LI(A('', 'widget_examples_results'	    , _href=URL('widget_examples_results'	   )), _class='test', _id=0),
        LI(A('', 'display_form' 		    , _href=URL('display_form'  		   )), _class='test', _id=0),
        LI(A('', 'grid_person'			    , _href=URL('grid_person'			   )), _class='test', _id=0),
        LI(A('', 'examples_manage'		    , _href=URL('examples_manage'		   )), _class='test', _id=0),
        LI(A('', 'two_tables'			    , _href=URL('two_tables'			   )), _class='test', _id=0),
        LI(A('', 'two_smart_tables'		    , _href=URL('two_smart_tables'		   )), _class='test', _id=0),
        LI(A('', 'powermanage'			    , _href=URL('powermanage'			   )), _class='test', _id=0),
        LI(A('', 'person_and_dog'		    , _href=URL('person_and_dog'		   )), _class='test', _id=0),
        LI(A('', 'person_and_dog_smart' 	    , _href=URL('person_and_dog_smart'  	   )), _class='test', _id=0),
        LI(A('', 'person_dog_thing_smart'	    , _href=URL('person_dog_thing_smart'	   )), _class='test', _id=0),
        LI(A('', 'examples_pbase'		    , _href=URL('examples_pbase'		   )), _class='test', _id=0),
        LI(A('', 'display_examples_pbase'   , _href=URL('display_examples_pbase')), _class ='test', _id= 0),
        LI(A('', 'display_examples_child'	, _href=URL('display_examples_child'	   )), _class='test', _id=0),
        LI(A('', 'parentmanager'		    , _href=URL('parentmanager' 		   )), _class='test', _id=0),
        LI(A('', 'trunc_n_fill' 		    , _href=URL('trunc_n_fill'  		   )), _class='test', _id=0),
        LI(A('', 'smartgrid_pbase'		    , _href=URL('smartgrid_pbase'		   )), _class='test', _id=0),
        LI(A('', 'showbooleffect'		    , _href=URL('showbooleffect'		   )), _class='test', _id=0),
        LI('Simple Form, prepopulating a list, dropping a list (does not work) and simple queries:'),
        LI(A('', 'show_examples_fieldtypenquery'    , _href=URL('show_examples_fieldtypenquery'    )), _class='test', _id=0),
        LI(A('', 'populate_examples_fieldtypenquery', _href=URL('populate_examples_fieldtypenquery')), _class='test', _id=0),
        LI(A('', 'examples_fieldtypenquery_drop'    , _href=URL('examples_fieldtypenquery_drop'    )), _class='test', _id=0),
        LI('Playing with args and vars:'),
        LI(A('', 'examples_request_playing'	    , _href=URL('examples_request_playing'	   )), _class='test', _id=0),
        LI(A('', 'call_foo'			    , _href=URL('call_foo'			   )), _class='test', _id=0),
        LI(A('', 'call_more_complex'		    , _href=URL('call_more_complex'		   )), _class='test', _id=0),
        LI(A('', 'validatorwidget'		    , _href=URL('validatorwidget'		   )), _class='test', _id=0),
        LI('Playing with tables and field'),
        LI(A('', 'fieldplay'			    , _href=URL('fieldplay'			   )), _class='test', _id=0),
        LI(A('', 'query_set_rows'		    , _href=URL('query_set_rows'		   )), _class='test', _id=0),
        LI(A('', 'query_set_rows2'	    	, _href=URL('query_set_rows2'		   )), _class='test', _id=0),
        LI(A('', 'girl_cat_queries'		    , _href=URL('girl_cat_queries'		   )), _class='test', _id=0),
        LI(A('', 'autoinsert'			    , _href=URL('autoinsert'			   )), _class='test', _id=0),
        LI(A('', 'custom_validator'		    , _href=URL('custom_validator'		   )), _class='test', _id=0),
        LI(A('', 'downbutton_manip'		    , _href=URL('downbutton_manip'		   )), _class='test', _id=0),
        LI(A('', 'css_test'			        , _href=URL('css_test'			   )), _class='test', _id=0),
        LI(A('', 'table_test'			    , _href=URL('table_test'			   )), _class='test', _id=0),
        LI(A('', 'examples_export_import'   , _href=URL('examples_export_import')), _class='test', _id=0),
        LI(A('', 'examples_massimo'         , _href=URL('examples_massimo')), _class='test', _id=0),
        LI(A('', 'examples_customform'      , _href=URL('examples_customform')), _class='test', _id=0),
        LI(A('', 'examples_customformfactory', _href=URL('examples_customformfactory')), _class='test', _id=0),
        #LI(A('', '', _href=URL('')), _class='test', _id=0),
        #LI(A('', '', _href=URL('')), _class='test', _id=0),
        #LI(A('', '', _href=URL('')), _class='test', _id=0),
    )
    return locals()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():

    tmp = request.vars.message or 'There was an error (but no error message given)'
    message = T("Error: %s") % (tmp)

    response.flash = message
    err_mes = T(message)
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

    # simple for loop
    for x in range(0, 3):
        print x

    # a list can store watchalike
    lst = ["is", 1, "nice", "but strange", " ... thing", "delme", "delme", "delme"]

    # insert something at the beginning and remove an (one) specific entry
    lst.insert(0,"Love")
    lst.remove("but strange")

    # remove all entries of an value
    lst = [x for x in lst if x!="delme"]

    print "\nlooping a list is easy"
    for l in lst:
        print l


    # loop and cont at the same time
    my_lst = ['a',9999,'hugo']
    for i, val in enumerate(my_lst):
        print 'number %d, value %s' % (i, val)

    # loop over a dict
    dic = dict(a=1,b=12,c="hallo")
    for key, value in dic.iteritems():
        print "the key is %s and the values is %s" % (key, value)
        #print key, value

    # reverse a list
    lst = [1,2,3,4,5]
    lst.append("dog")
    reverse_lst = lst[::-1]

    print lst
    print reverse_lst
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

    #input0 = INPUT(_name='input0', _value='a', value='b') # ???

    form = FORM('Your name:', INPUT(_name='name'), INPUT(_type='submit'))

    link0 = A('go to index', _href=URL('index'))
    link1 = A('what does the callback thing do?', callback=URL('index'), target="t")
    link2 = A('Button?', _href=URL('index'), _class="btn")
    link3 = A('Default?', _href=URL('index'), _class="btn btn-default")
    link4 = A('Primary', _href=URL('index'), _class="btn btn-primary")
    link5 = A('Success', _href=URL('index'), _class="btn btn-success")
    link6 = A('Info', _href=URL('index'), _class="btn btn-info")
    link7 = A('Warning', _href=URL('index'), _class="btn btn-warning")
    link8 = A('Danger', _href=URL('index'), _class="btn btn-danger")
    link9 = A('Link', _href=URL('index'), _class="btn btn-link")

    return locals()
# --------------
def test_view_action():
    retval = "Hello World"
    return dict(retval=retval)

###########################
# Form, SQLFORM and Grids #
###########################

# --------------
def form():
    #example of a form
    print " --------- \n form: PLEASE CREATE EXAMPLE CODE"
    response.flash = "PLEASE CREATE EXAMPLE CODE"

    #form = SQLFORM(<table>, record=None,
    #    deletable=False, linkto=None,
    #    upload=None, fields=None, labels=None,
    #    col3={}, submit_button='Submit',
    #    delete_label='Check to delete:',
    #    showid=True, readonly=False,
    #    comments=True, keepopts=[],
    #    ignore_rw=False, record_id=None,
    #    formstyle='table3cols',
    #    buttons=['submit'], separator=': ',
    #    **attributes)

    return dict()

# --------------
def sqlform_basic():
    # the full signature of a SQLFORM is:
    #SQLFORM(table, record=None,
    #    deletable=False, linkto=None,
    #    upload=None, fields=None, labels=None,
    #    col3={}, submit_button='Submit',
    #    delete_label='Check to delete:',
    #    showid=True, readonly=False,
    #    comments=True, keepopts=[],
    #    ignore_rw=False, record_id=None,
    #    formstyle='table3cols',
    #    buttons=['submit'], separator=': ',
    #    **attributes)

    # therefore, the simples way to use a SQLFORM is to create it and return it as a dictionary
    # to the view (../views/examples/sqlform_basic.html)
    form = SQLFORM(db.examples_person)

    # as you do not define anything to do after something is submitted, the form just shows
    # itself and 'selfsubmits' on submission (goes to the same URL again)
    return dict(form=form)

# --------------
def sqlform_v1():
    # the full signature of a SQLFORM is:
    #SQLFORM(table, record=None,
    #    deletable=False, linkto=None,
    #    upload=None, fields=None, labels=None,
    #    col3={}, submit_button='Submit',
    #    delete_label='Check to delete:',
    #    showid=True, readonly=False,
    #    comments=True, keepopts=[],
    #    ignore_rw=False, record_id=None,
    #    formstyle='table3cols',
    #    buttons=['submit'], separator=': ',
    #    **attributes)

    print 'request.args(0)=', request.args(0)
    print 'db.examples_person(request.args(0))', db.examples_person(request.args(0))

    url = URL('download')
    link = URL('list_records', args='db')

    form = SQLFORM(db.examples_person,
                   # record defines kind of the type of your form
                   #record=None,    # this is only a input form
                   # now it's an update form, if a number (person_id) is given in the UPL (e.g. .../sqlform_v1/1)
                   #record=db.examples_person(request.args(0) or redirect(URL('index'))),
                   record=db.examples_person(request.args(0)), # this should work for insert and update, correct?
                   #record=5, # this sets the 5'th data-set (kind of hardcoded)

                   deletable=True, # this makes delete checkbox

                   linkto=link, #links to the URL of the list_records funciton

                   # upload needs a download fuction! the reason seems to be, that upload/download is so much individual
                   # that web2py does not have one included. to make it work you need three things:
                   # - the field must be defined as upload field in the table (model)
                   # - the upload variable here must name an function
                   # - there needs to be a function in this controller, named as the entry here
                   upload=URL('download'),
                   #fields=None, labels=None,
                   #    col3={},
                   #submit_button='Submit this form',
                   #    delete_label='Check to delete:',
                   #    showid=True, readonly=False,
                   #    comments=True, keepopts=[],
                   #    ignore_rw=False, record_id=None,
                   #    formstyle='table3cols',
                   #    buttons=['submit'], separator=': ',
                   #    **attributes)
                   )

    # process the form and do things according to what has happened
    if form.process(keepvalues=True).accepted:
        name = form.vars.name # all info of the form is stored in <formname>.vars
        response.flash = 'form accepted! Hi %s' % name

    elif form.errors:
        response.flash = 'form contains errors'
    else:
        response.flash = 'please fill the form'

    return dict(form=form)

# define a download function for SQLFORMS to use
def download():
    return response.download(request, db)


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


# --------------------
# truncate data from some tables or create new example data
def trunc_n_fill():

    if len(request.vars)<=0:
        request.flash = 'you need var: trunc==True'
        session.flash = 'you need var: trunc==True'
        print 'you need var: trunc==True'
    else:
        trunc=request.vars.trunc
        print 'trunc=', trunc
        print 'type(trunc)=', type(trunc)

        if trunc=='True':
            db.examples_pbase.truncate()
            db.examples_checklist.truncate()
            db.examples_mobility.truncate()
            db.examples_edu.truncate()
            db.examples_housing.truncate()
            db.examples_child.truncate()
        else:
            db.examples_pbase.insert(name='Amir1', firstname="Abu1", fullname='Abu Amir 1', zab='012345')
            db.examples_pbase.insert(name='Amir2', firstname="Abu2", fullname='Abu Amir 2', zab='012346')
            db.examples_pbase.insert(name='Amir3', firstname="Abu3", fullname='Abu Amir 3', zab='012347')

            db.examples_checklist.insert(name='Abu Amir', pbase_id=1, moveindate='2017-05-05',dezi='On', mailbox_labeled=False)
            db.examples_checklist.insert(name='Baba Basu', pbase_id=2, moveindate='2014-05-05', dezi=True, mailbox_labeled=False)
            db.examples_checklist.insert(name='Charly Cheen', pbase_id=3, moveindate='2011-01-02', dezi=True, mailbox_labeled='On')

            db.examples_mobility.insert(name='Abu Amir', pbase_id=1, ticket=True, expires='2017-09-16')
            db.examples_mobility.insert(name='autoset', pbase_id=2, ticket=False, expires='2017-10-16')
            db.examples_mobility.insert(name='autoset', pbase_id=3, ticket=True, expires='2018-05-20')

            db.examples_edu.insert(name='Abu Amir', pbase_id=1, job='Worker' , edu='none', german='A0')
            db.examples_edu.insert(name='autoset', pbase_id=2, job='Nurse'  , edu='elementary', german='B1')
            db.examples_edu.insert(name='autoset', pbase_id=3, job='Student', edu='phd', german='B2')

            db.examples_housing.insert(name='Abu Amir', pbase_id=1, address='Am Hang 1', landlord='LH DD', contact_address='Bergstr. 1', contact_phone='0351 1234567')
            db.examples_housing.insert(name='autoset', pbase_id=2, address='Ind der Stadt 5', landlord='VONOVIA', contact_address='', contact_phone='111 1111111')
            db.examples_housing.insert(name='autoset', pbase_id=3, address='Wanderweg 8', landlord='Herr Krause', contact_address='', contact_phone='')

            db.examples_child.insert(name='Amir', pbase_id=1, firstname='Bob', birthdate='2011-03-03')
            db.examples_child.insert(name='Schneider', pbase_id=2, firstname='Carla', birthdate='2011-09-13')
            db.examples_child.insert(name='Simson', pbase_id=3, firstname='Sam', birthdate='2010-03-03')

        redirect(URL('examples_manage', args=('examples_checklist')))

    return 'end of trunc_n_fill controller reached'



# --------------------
# show (linked) tables of pbase together (using a smartgrid)
@auth.requires_login()
def smartgrid_pbase():

    grid = SQLFORM.smartgrid(db.examples_pbase,
            linked_tables=['examples_checklist','examples_mobility','examples_edu','examples_housing', 'examples_child'],
            headers= {},

            )

    return locals()


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
    my_text = MARKMIN("Example of the existing field types look into db.examples_fieldtypequery [[NEWLINE]]\
                      - here: just show the data in a default grid [[NEWLINE]]\
                        however: you most probably like to redirect to such a page after different 'actions' (other functions)[[NEWLINE]]\
                        (see redirect statements in functions below)[[NEWLINE]]\
                        [[NEWLINE]]\
                      - You can also do a (simple) interactive query[[NEWLINE]]\
                        click on search and figure out how to add different constraints to the query[[NEWLINE]]\
                        [[NEWLINE]]\
                        "
                      )

    form = SQLFORM.grid(db.examples_fieldtypenquery2)
    return locals()

def populate_examples_fieldtypenquery():
    my_text = MARKMIN("Example of **prepopulating** a database with random data: [[NEWLINE]]\
                          - how to ask via a form how many entries you like [[NEWLINE]]\
                          - how to propopulate the datebase  [[NEWLINE]]\
                          - how to add some buttons (just an exercise, not really needed)"
                      )

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

    return locals()

def examples_fieldtypenquery_drop():
    my_text = MARKMIN("Example of dropping a table: **does not work this way! read comment in function\
                       and investigate!**")

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

    # Workaround: reamove all table data using appadmin

    #import os
    #cwd = os.getcwd() # get current working directory
    #print cwd
    #db_filename =

    #os.remove(db_filename)
    return locals()

#################################
# request.args and request.vars #
#################################

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


############################
# writing your own modules #
############################

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


##################################################################
# Validators and widgets define the behaviour of forms and grids #
##################################################################

@auth.requires_login()
def validatorwidget():

    form = SQLFORM(db.examples_validatorwidget)

    return dict(form=form)


##################################
# Playing with tables and field  #
##################################

@auth.requires_login() # every fuction with grids should require (at least) login
def fieldplay():
    my_text = MARKMIN('Look at the code and the output on the web2py console for this example!')

    print "\n\n ---------\n fieldplay: "
    print 'you can access/change table an field things'
    print 'list all tables, db.tables:';  print db.tables
    print 'list all fields of a table, db.examples_fieldplay.fields:'; print db.examples_fieldplay.fields

    print '\naccess the field attributes'
    print 'db.examples_fieldplay.firstname.unique = ', db.examples_fieldplay.firstname.unique
    print 'db.examples_fieldplay.secondname.default = ' ,db.examples_fieldplay.firstname.unique

    print '\naccess the info of the parent (_table, _tablename, _db):'
    print '_table:', db.examples_fieldplay.firstname._table
    print '_tablename:', db.examples_fieldplay.firstname._tablename
    print '_db: too long, uncomment to see result' #, db.examples_fieldplay.firstname._db

    print '\nyou can use the validator of this field programatically'
    print 'John in firstname:', db.examples_fieldplay.firstname.validate('John')
    print 'void in firstname:', db.examples_fieldplay.firstname.validate('')


    print '\nYou can truncate the table, i.e., delete all records and reset the counter of the id'
    print db.examples_fieldplay.truncate() # in a modules you need also 'commit' (see book, chapter DAL)

    print '\ninsert a new record'
    print db.examples_fieldplay.insert(firstname='Dagobert')
    print db.examples_fieldplay.insert(secondname='Duck')


    #print 'update?' DOES NOT WORK THIS WAY!
    #print db.examples_fieldplay.update(firstname='Dagobert Dogmata')

    #
    print "\nand finally, you can show the database in a grid"
    form = SQLFORM.grid(db.examples_fieldplay,)
    return locals()

# --------------
@auth.requires_login()
def query_set_rows():
    my_text = MARKMIN('Look at the code and the output on the web2py console for this example!')

    print "\n\n -------------- \n query_set_rows"
    # store table in an variable
    table = db.examples_qsr

    print "\nyou can store fields in variables (the fields, NOT their values!)"
    name = db.examples_qsr.name # long way
    job  = table.job       # using the above created variable 'table'
    print 'name=', name
    print 'job=', job

    print "\nyou can truncate the data of a table (also resets the id-counter) ..."
    table.truncate()

    print "\n ... and fill with some data again"
    table.insert(name='Peter', job='Cleaning Woman')
    table.insert(name='Paul', job='Taxidriver')
    table.insert(name='Mary', job='Doctor')
    table.insert(name='Jane', job='Manager')

    print "\n you can define a query: q = job == 'Doctor'"
    q = job == 'Doctor'

    print "\ncalling a db with a query creates (or better defines) a set of data: s = db(q)"
    s = db(q)
    #s = db(job == 'Doctor') # this is in one line

    print "\n ... and select interacts with the pysical database and returns the result as a set of rows:\nrows = s.select()"
    rows = s.select()
    # you can also do all of this in one line
    #rows = db(db.examples_qsr.job == 'Doctor').select()

    print '\n you can loop and manually print the data you like of the rows (here: id ad name) ...'
    for row in rows:
        print "row.id=%s, row.name=%s" % (row.id, row.name)

    print '\n or select only some data (e.g. only column job)'
    rows = db(db.examples_qsr.job == 'Doctor').select(job)
    for row in rows:
        print "row.job:",  row.job
        print 'row.name => would raise an AttributeError'
        print 'row:', row

    print '\n the table attribute ALL allows you to specify all fields (printing the whole row):'
    for row in db().select(db.examples_qsr.ALL):
        print row

    print "\n and you can update a record ('Paul' gets 'web2py programmer' here)"
    for row in db(table.id > 0).select():
        if row.name=='Paul':
            row.update_record(job='web2py programmer')

    print "\n as allways, you can show the whole table in a grid"
    form = SQLFORM.grid(table)

    return locals()

# -------------
# msw: taken from the cookbook (p. 56) - what does this code do exactly?
def download(): return response.download(request, db)

# --------------
@auth.requires_login()
def query_set_rows2():
    my_text = MARKMIN('Some more on queries, look at the code and the output on the web2py console for this example!')

    print "\n\n -------------- \n query_set_rows2"

    # store table in an variable
    table = db.examples_qsr

    print "\nyou can truncate the data of a table (also resets the id-counter) ..."
    db.examples_qsr.truncate()

    print "\n ... and fill with some data again"
    table.insert(name='Peter', job='Cleaning Woman', birth='1967-01-01', bike=False)
    table.insert(name='Paul', job='Taxidriver', birth='1977-01-01', bike=False)
    table.insert(name='Mary', job='Doctor', birth='1987-01-01', bike=True)
    table.insert(name='Jane', job='Manager', birth='1997-01-01', bike=True)

    print "use the different example-queries in the code (and add more complex ones):"
    #q = (table.name == 'Peter') | (table.name == 'Paul') # peter and paul
    #q = (table.name >='N') # name start with letter 'bigger' 'n'
    q = (table.birth > '1990-01-01')

    s = db(q)
    rows = s.select()


    print "\n you can print the query to console:\n", q
    print "and loop over the rows and see what has been selected (use rows.render to see the 'represents' formatting " \
          "of the Field"
    for row in rows.render():
        print row


    "\n as allways, you can show the whole table in a grid, with the 'fields' parameter you can select the fields shown"
    form = SQLFORM.grid(q,
                        #fields=[table.name,table.job] # show only some fields
                        #fields=[db.examples_qsr.name,db.examples_qsr.job],
                        )

    return locals()

#---------------------
def girl_cat_queries():


    def __nof_cats(owner_id):
        q = db.examples_girl.id = db.examples_cat.owner_id

    print '\n ---------------------- \n girl_cat_queries()'
    my_text = MARKMIN('Some even more on queries, now including two tables.  [[NEWLINE]]\
        look at the code and the output on the web2py console for this example!')

    # first truncate all data ...
    db.examples_girl.truncate()
    db.examples_cat.truncate()

    # and refill to allways have a defined start
    db.examples_girl.insert(name='April', birth='2009-02-03', school='First School')
    db.examples_girl.insert(name='May'  , birth='2010-05-03', school='Second School')
    db.examples_girl.insert(name='June' , birth='2010-05-27', school='Third School')

    db.examples_cat.insert(name='Fluffi', owner_id = '1', doctordue ='2017-05-20', color = 'red')
    db.examples_cat.insert(name='Goldy', owner_id = '1', doctordue ='2017-05-26', color = 'black')
    db.examples_cat.insert(name='Glory' , owner_id = '2', doctordue ='2017-12-12', color = 'white')
    db.examples_cat.insert(name='Molly' , owner_id = '2', doctordue ='2017-09-11', color = 'white')
    db.examples_cat.insert(name='Berta' , owner_id = '3', doctordue ='2018-03-13', color = 'striped')


    print '\nshow cats of girl with id=1'
    for row in db(db.examples_cat.owner_id == 1).select():
        print row.name

    print '\nloop over girls and show their cats'
    print "IMPORTANTS: because of the link in 'examples_cat' to 'examples_girl', examples_girl now has a"
    print "new *attribute* (examples_girl.examples_cat)"
    for girl in db().select(db.examples_girl.ALL):
        #print girl
        print 'girls name: ', girl.name
        for cat in girl.examples_cat.select():
            print '\tcat:', cat.name

    print 'do a inner joint'
    q = db.examples_girl.id == db.examples_cat.owner_id
    s = [db.examples_girl.name, db.examples_cat.id, db.examples_cat.name, db.examples_cat.doctordue]
    rows = db(q).select(db.examples_girl.name, db.examples_cat.name, db.examples_cat.doctordue, groupby=db.examples_girl.name)
    #rows = db(q).select(*s)

    for row in rows:
        #print row
        print row.examples_girl.name,  ' has cat ', row.examples_cat.name

    table = SQLTABLE(rows,
			headers='fieldname:capitalize',
            truncate=100,
            upload=URL('download'),
			_width="50%",
			_border="2px solid black",
            _height="90px",
			#_text_align="center", # does not work, with '_text-align' gives ticket
                )

    #form = SQLFORM.grid(q,
    #                    fields=[db.examples_girl.name,db.examples_girl.school, db.examples_cat.name,],)
    #form = SQLFORM.grid(table) DOES NOT WORK AT ALL (seems obvious)
    #form = SQLFORM(rows)

    gridq = q
    #gridq = ((db.examples_girl.id == db.examples_cat.owner_id) & (db.examples_girl.birth >= '2010-05-03'))
    #gridq = (db.examples_girl.id == db.examples_cat.owner_id) & (db.examples_girl.birth >= '2010-05-03')


    #db(query).count()

    form = SQLFORM.grid(gridq,
                        fields=s,
                        )

    smart = SQLFORM.smartgrid(db.examples_girl, linked_tables=['examples_cat'], fields=s,)

    return locals()


#---------------------
@auth.requires_login()
def autoinsert():
    # Adding a value to the table which is computed/compused from other values in the table can
    # be done using the 'compute' attribute and a function/lambda.
    #
    # as far as I understand, the value of the computed field is not always updated (probably only
    # update in a form/grid?). if you have more complex database manipulation, look into virual fields or
    # invent something in the onvalidate fuction of your form/grid (are these lines true or nonsense?)

    form = SQLFORM.grid(db.examples_fieldplay)
    return locals()

####################
# Custom Validator #
####################

def custom_validator():

    id = db.examples_atable.insert(astring='hallo msw')
    row = db.examples_atable[id]
    # print '1:', db.examples_atable.formatter(row.astring)
    #print '2:', row.astring

    form = SQLFORM(db.examples_atable,
                   #record=1
                   )

    if form.process().accepted:
        response.flash = 'cool'
    elif form.errors:
        response.flash = 'errors'
    else: response.flash = 'please fill the form'

    return locals()

################################################
# Changing the default grid buttons for export #
################################################

def downbutton_manip():

    # 1. to remove one or more download buttons from the dafault grid,
    # give the grid contructor a dict like this
    export_classes = dict(
                        #csv=False # <= this will be shown
                        csv_with_hidden_cols=False, tsv=False, html=False,
                        tsv_with_hidden_cols=False, json=False, xml=False)

    form = SQLFORM.grid(db.examples_dog,
                        exportclasses = export_classes,
    )

    # 2. You can move the button alongside to the upper right (besides search) by
    # putting a script into the view file (see: downbutton_manip.html)
    # see: http://rootpy.com/Export-in-SQLFORM-grid/

    # 3. how to manipulate the export and the do import, please insert here some examples/explanations

    return locals()

#############
# CSS TESTS #
#############

def css_test():
    table = TABLE(TR('a', 'b'), TR('c', 'd'), _border="1px solid black")

    #form = SQLFORM.grid(table) DOES NOT WORK

    return locals()


##########
# Tables #
##########

# ---------------
def table_test():
    # start with something simple and set a css-property (inline) as parameter
    table0 = TABLE(TR('a', 'b'), TR('c', 'd'), _border="1px solid black")

    # fill the date of the table from a list (of lists)
    table1_data = [['Family Name', 'First Name'],
                   ['Bertone', 'Bernardo'],
                   ['Cesar', 'Julius'],
                   ]
    table1 = TABLE(TR(*table1_data[0]), TR(*table1_data[1]), TR(*table1_data[2]), _border="1px solid black")
    table2 = TABLE(TR(*table1_data[0]), TR(*table1_data[1]), TR(*table1_data[2]), _width="100%")

    # add links
    table1_data = [[B('Family Name'), B(I('First Name'))],
                   [A('Linker', _href=URL('index')), 'Index'],
                   ['Cesar', 'Julius'],
                   ]

    table3 = TABLE(TR(*table1_data[0]), TR(*table1_data[1]), TR(*table1_data[2]),
                   _width="50%", _border="2px solid black", _height="190px", )# gives ticket: _text-align="center" ??!!

    # do a query and put results in table

    header = ['girl name']
    girls = []
    rows = db(db.examples_girl).select()
    for row in rows:
        print row
        print row.name
        girls.append(row.name)

    table4 = TABLE(
                    TR(header[0]),
                    TR(girls[0]),
                    TR(girls[1]),

                    _width="50%",
                    _border="2px solid black",
                    _height="90px",
                )  # gives ticket: _text-align="center" ??!!


    return locals()

#####################
# Export and import #
#####################

# ---------------
@auth.requires_login()
def examples_export_import():
    # you can export and import easily, however, some things are to be kept in mind
    #  - if the table does not have a uuid, all imported date will be *added*
    #  - if rows in an imported table are the same in the sense that on two machines the same
    #    entries where introduced manually, then of course all entries still have different uuid's
    #    (i.e. the data will be added and you have two 'John Smith'
    #  - if you import/export all, then really all data is menat (including user and auth data)
    #  - you can easily drop all data by removing all files in databases (rm databases/*). then, however,
    #    also all user/auth data is gone and you are unable to login! simply create a new user with appadmin.
    # this is only an example, please improve for better handling of the file/path-names and stuff like that.


    form = SQLFORM.factory(
        Field('table_name', requires=IS_NOT_EMPTY(),
              comment=T('ex/im: tablename, e.g. asyl_accommodation; ex/im-ALL: filename (in .../private/CSV/)')),
        Field('ex_or_im', requires=IS_IN_SET(['export', 'import', 'export-ALL', 'import-ALL']), label='Export or Import',
                widget = lambda field,value: SQLFORM.widgets.radio.widget(field,value, style='table')),

        #Field('export_file', 'upload'))
        #Field('query)
        )


    if form.process().accepted:
        table_name= form.vars.table_name
        style = form.vars.ex_or_im

        if style=='export' or style=='import':
            file_name = str('./applications/Asylum/private/CSV/'+table_name+'.csv')
            if style == 'export':
                open(file_name, 'wb').write(str(db(db[table_name].id).select()))
                response.flash = 'form accepted and data exported to file %s' % (file_name)

            elif style == 'import':
                db[table_name].import_from_csv_file(open(file_name, 'r'))
                response.flash = 'data imported form file %s' % (file_name)
            else:
                response.flash = 'verystrange in export/import'

        elif style == 'export-ALL' or style == 'import-ALL':
            file_name = str('./applications/Asylum/private/CSV/' + table_name)
            if style == 'export-ALL':
                db.export_to_csv_file(open(file_name, 'wb'))

            elif style == 'import-ALL':
                db.import_from_csv_file(open(file_name, 'rb'))
            else:
                response.flash = 'verystrange in export/import ALL'
        else:
            response.flash = 'verystrange in export/import (big if)'

    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'form shown for the fist time'

    return locals()



########################
# DAL examples massimo #
########################

# https://www.youtube.com/watch?v=_4to_44DcJU (0:48:xx)

def examples_massimo():
    # 0:53:00
    print db._uri # show uri
    print db._adapter # gloun contains an adapter (never used by user, but important to know)

    # 0:55:00
    print "you can refer to a field (type field) and to a person"
    print db.person
    print db.person.name

    # this is needed in order to make this example working (truncate the existing table)
    db.person.truncate()

    # 0:55:45
    db.person.insert(name='Max', phone='111')
    db.person.insert(name='Tim', phone='112')
    db.person.insert(name='John', phone = '113')

    print "\n get person with id == 1 or get first person?"
    row = db.person(1) # get person with id==1 or get first person?
    print row

    print "\n you can use bracket notation or the simple one to access data"
    print row['name']
    print row['phone']
    print row.name
    print row.phone

    print "\n what happens, if things do not exist"
    print db.person(9)
    print db.person[9]

    print "\you can search ..."
    print db.person(name='Max')
    print db.person(name = 'max') # case sensitive!!
    print db.person(phone = '112', name='Tim')

    # 00:58:05
    print "\n more complex queries"
    rows = db((db.person.name=='Max') | (db.person.name=='Tim')).select()
    print "\n print row by index:"
    print rows[0]
    print rows[1]

    print "\n first and length on rows:"
    print rows.first()
    print len(rows)

    print "\n select in string by gt, le, ..."
    rows = db((db.person.name >= 'Max') & (db.person.name <= 'Tim')).select()
    print rows

    rows = db((db.person.name > 'B') & (db.person.name <= 'X')).select()
    print rows

    rows = db(~(db.person.name <= 'M')).select()
    print  rows

    rows = db( db.person.name.startswith('j') ).select()
    print  rows

    rows = db(db.person.name.contains('m')).select()
    print rows

    rows = db(db.person.name.belongs('Max','Tim')).select()
    print rows

    # subset (seems to be case sensistive)
    rows = db(db.person.name[0:1].belongs('M', 'T')).select()
    print rows

    # 01:02:29
    print "\nsubset (third character is a 'x' or a 'h')"
    rows = db(db.person.name[2:3].belongs('x', 'h')).select()
    print rows


    print "\n you can allways see the last sql command (which may vary for backends)"
    print db._lastsql

    # 01:03:40
    print "\n using select to define the rows wanted"
    rows = db(db.person).select(db.person.name,db.person.phone)
    print  rows

    print "\n let's insert two more Max's persons with different phones"
    db.person.insert(name='Max', phone='211')
    db.person.insert(name='Max', phone='311')
    rows = db(db.person.name).select()
    print  rows

    print "\n we can group, e.g. by name"
    rows = db(db.person.name).select(db.person.name, groupby=db.person.name)
    print  rows

    print "\n we can group and count, e.g. by name"
    rows = db(db.person.name).select(db.person.name, db.person.id.count(), groupby=db.person.name)
    print rows

    print "\nlet's create another table 'dog'"
    db.dog.truncate()
    db.dog.insert(name='Skipper', dog_owner=1)
    db.dog.insert(name='Snoopy', dog_owner=1)
    db.dog.insert(name='Wolf', dog_owner=2)

    rows = db(db.dog).select()
    print rows

    print rows.first() # first row
    print rows.first().id # id of first row
    print rows.first().dog_owner # id of owner of this dog
    print rows.first().dog_owner.name # the name of the owner of this dog
    print rows.first().dog_owner.phone # everything else of the owner of this dog (here phone)

    ## 01:08:10
    print "\nretrieve info from db"
    print dir(db)

    # 01:08:21
    print "\n_timings somehow keeps track of how log queries took:"
    print db._timings[0]
    print db._timings[0][0]
    print db._timings[-1][0]
    print db._timings[-1][1]

    # 01:09:10
    print "\nback to example, which tables do we have?"
    print db.tables

    print "\nwhich fields does a table have"
    print db.person.fields
    print db.dog.fields

    print "\nwhat is the name, type and tablename of a field"
    print  db.dog.dog_owner.name
    print  db.dog.dog_owner.type
    print  db.dog.dog_owner.tablename

    print "\ndir(...) seems to give a summary of things of an object ..."
    print dir(db.dog.dog_owner)

    print "\n ... and e.g. you find the function 'count', so let's count"
    # form db, select table db.person, you are looking only for the person.id ... which is counted and the result is
    # stored in row
    # (where db(...) is NOT a function call to db, but rather a function called on
    # db with parameters ',,,' - IS THIS CORRECT???)
    row = db(db.person).select(db.person.id.count())
    print row

    print "\nlet's count how many dog each owner has"
    print db(db.dog).select(db.dog.dog_owner, db.dog.id.count(), groupby=db.dog.dog_owner)

    print "\n put results in rows and loop to do more things"
    rows = db(db.dog).select(db.dog.dog_owner, db.dog.id.count(), groupby=db.dog.dog_owner)
    for row in rows:
        #print row.dog.dog_owner.name, row[db.dog.id.count()]
        print row

    print "\n let's go to a joint, and first join everything"
    query = (db.dog.dog_owner == db.person.id)
    rows = db(query).select()
    print rows

    print "\n now let's only show some data (columns)"
    query = (db.dog.dog_owner == db.person.id)
    rows = db(query).select(db.person.name, db.dog.name)
    print rows

    rows = db(query).select(db.person.name, db.dog.id.count(), groupby=db.person.id)
    print rows
    #for row in rows:
    #    print row

    print "\n in case of a joint, you have to specify the table name, as field names can be ambigous. as seen before, " \
          "_extra elements like 'count' are accessed with square-backets"
    print rows[0]
    print rows[0].person.name
    print rows[0][db.dog.id.count()]

    print "\n what can you do with 'select'"
    print "ordered in alphabetical order"
    rows = db(db.person).select(orderby=db.person.name)
    print rows

    print "\nordered in alphabetical order and in reversed id order(in case name is the same)"
    rows = db(db.person).select(orderby=db.person.name|~db.person.id)
    print  rows

    print "\nordered by the second character of the name an then with reversed id order (in case character is the same)"
    rows = db(db.person).select(orderby=db.person.name[1:2] | ~db.person.id)
    print  rows

    print "\n limitby seems to just take the id in the range given (>fistnum and <= lastnum??)"
    #rows = db(db.person).select(limitby=(0, 9999))
    rows = db(db.person).select(limitby=(0,2))
    #rows = db(db.person).select(limitby=(2,4))
    print rows

    print "\n what we have learned about select in one line"
    rows = db(query).select(db.person.name, db.dog.name,
                            orderby=db.person.name,
                            groupby=db.person.name,
                            limitby=(0,2))
    print rows

    # 01:25;10
    print "\n outer joint"
    rows = db(db.person).select(db.person.name, db.dog.name, left=db.dog.on(db.person.id==db.dog.dog_owner))
    print rows

    #rows = db().select(db.person.ALL, db.thing.ALL,
    #                   left=db.thing.on(db.person.id == db.thing.owner_id))

    print "\n you can left-join multiple tables via a list(?) of join statements, ... "
    print "tutorial jumps to next topic - 01:27:05"
    #

    #form = SQLFORM.grid(rows)
    form = SQLFORM.smartgrid(db.person, linked_tables=['dog'],)

    return locals()




    ## 01:0:
    # print "\n"
    # rows = db(db.person.name[2:3].belongs('x', 'h')).select()
    # print  rows

    ## 01:0:
    # print "\n"
    # rows = db(db.person.name[2:3].belongs('x', 'h')).select()
    # print  rows

    return locals()

################
# Custom Forms #
################
def examples_customform():
    form = SQLFORM(db.person)
    form.process()
    return dict(form=form)

def examples_customformfactory():
    form = SQLFORM.factory(
        Field("name"),
        Field("aset", requires=IS_IN_SET(["dog", "cat", "mouse"])),
        Field("onetwothree", requires=IS_IN_SET(["one", "two", "three"], multiple=True),
            widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=3, _width = '50%'), #_class='well', _width = '100%'),
        ),
        Field("fourfivesix", requires=IS_IN_SET(["four", "five", "six"], multiple=True),
              widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=3, _width='50%'),
              # _class='well', _width = '100%'),
              ),
    )
    form.process()
    return dict(form=form)