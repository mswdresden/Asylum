#
# examples: by msw
#
if not session.my_language:
    pass
else:
    T.force(session.my_language)

# ---------------
# you should always have a index controller
# - controller functions (called via an URL) do NOT have parameters
def index():
    # returning a dict(...) means that web2py will look for a
    # corresponding ../views/<controller>/<function>.html file and call/evaluate/render it
    return dict()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():
    response.flash = "There was an error"

    # msw: is there a way to retrieve here in this function an meaningful error message?
    err_mes = T('please figure out how to write a meaningful error message from within this function')
    return dict(err_mes=err_mes)



# --------------------
# this could one day be a long example list of the web2py view helpers
def test_view():
    a = DIV(SPAN('a', 'b'), 'c')
    code=CODE("print code",styles={'CODE':'margin: 0;padding: 5px;border: none;'})
    return locals()
# --------------
# called from within the view (in the 'A' section)
def test_view_action():
    retval = "Hello World"
    return dict(retval=retval)

# --------------
# you can push variables from the action to the view via a dict
def communication():
    singledict = {"key": "value"}
    return locals()

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

# --------------
@auth.requires_login()
def my_manage():
    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    mygrid = SQLFORM.grid(db[table],args=request.args[:1])
    return locals()

# --------------
def pythonexamples():
    # here we have some pythonexamples

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
    return locals()

# ------------------------
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



#
# ----------------
#

# ---------------
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

# --------------------
# manage table manually using a grid, give table name as arg(0)
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

# --------------------------
def display_examples_child():
    record = db.examples_child(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.examples_child, record, deletable=True)

    if form.process().accepted: response.flash = 'form accepted'
    elif form.errors: response.flash = 'form has errors'
    else: response.flash= 'form shown for the first time'

    return dict(form=form)


@auth.requires_login()
def testerli():
    #form = SQLFORM.grid(db.parent)
    #form = SQLFORM.grid(db.child)
    #form = SQLFORM.grid(db.parent,left=db.child.on(db.child.parent==db.parent.id))
    form = SQLFORM.smartgrid(db.parent,linked_tables=['child', 'car'])

    return dict(form=form)