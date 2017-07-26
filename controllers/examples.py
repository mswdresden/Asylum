#
# examples: by msw
#

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
def grid():
    form = "Please implement code for grid"
    return dict(form=form)

# --------------
def pythonexamples():
    # here we have some pythonexamples

    # convert a list into a dict:
    lst=('dog','cat','mouse')
    mydict = {k: v for k, v in enumerate(lst)}
    print "mydict:",mydict

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
def manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table],
                        args=request.args[:1],
                        links_in_grid=True)
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