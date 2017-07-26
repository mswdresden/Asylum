# from iban import iban
#import iban

if not session.my_language:
    pass
else:
    T.force(session.my_language)

# -------------
def index():
    #return "hallo welt"
    linklist = UL(
        LI("call controller: ", A("show_pbase",             _href=URL("show_pbase")), _class='test', _id=0),
        LI("call controller: ", A("create_pbase",           _href=URL("create_pbase")), _class='test', _id=0),
        LI("call controller: ", A("update_pbase",           _href=URL("update_pbase")), _class='test', _id=0),
        LI("call controller: ", A("grid1_pbase",            _href=URL("grid1_pbase")), _class='test', _id=0),
        LI("call controller: ", A("grid_healthinsurance",   _href=URL("grid_healthinsurance")), _class='test', _id=0),
        LI("call controller: ", A("grid_accommodation",     _href=URL("grid_accommodation")), _class='test', _id=0),
        #LI("call controller: ", A("", _href=URL("")), _class='test', _id=0),
        LI("Manager",UL(
            LI("", A("asylum_accommodation", _href=URL("manage", args=['asylum_accommodation'])), _class='test', _id=0),
            LI("", A("asylum_pbase", _href=URL("manage", args=['asylum_pbase'])), _class='test', _id=0),
            LI("", A("asylum_healthinsurance", _href=URL("manage", args=['asylum_healthinsurance'])), _class='test', _id=0),
            LI("", A("asylum_address", _href=URL("manage", args=['asylum_address'])), _class='test', _id=0),
            LI("", A("asylum_checklist", _href=URL("manage", args=['asylum_checklist'])), _class='test', _id=0),
            LI("", A("asylum_edu", _href=URL("manage", args=['asylum_edu'])), _class='test', _id=0),
            LI("", A("asylum_socialwellfare", _href=URL("manage", args=['asylum_socialwellfare'])), _class='test', _id=0),
            #LI("", A("", _href=URL("manage", args=[''])), _class='test', _id=0),
            #LI("", A("", _href=URL("manage", args=[''])), _class='test', _id=0),
        ))
    )
    a = A(T("this is an example of an 'link to grid1', pushed from the controller to the this html"),_href=URL("grid1_pbase"))
    return locals()

# -------------
def ret99(): # only a test
    return dict(retval=99)

# -------------
def index_helper():
    #print "\n index_helper():"
    #print request.args
    #print my_arg

    data = request.args(0)
    vars = request.vars

    for key, value in vars.iteritems():
        print key
        print value

    response.flash = 'Data received: %s' % data
    #response.flash = 'variables received: %s' % vars

    print request.args
    print vars

    return DIV(BR(),UL('Return anything ...','a second row'))



# --------------------
# manage table manually using a grid, give table name as arg(0)
@auth.requires_login()
def manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table], args=request.args[:1], links_in_grid=True,
            )

    return locals()




# -------------
def show_pbase():
    # very simple, just return the data base
    #form = db(db.asylum_pbase).select(orderby=db.asylum_pbase.name)
    # form = db(db.asylum_pbase).select(orderby=db.asylum_pbase.arrivaldate)

    # more elaborate, use a SQLFORM
    form = SQLFORM(db.asylum_pbase,
                   #formstyle='bootstrap3_stacked'
                   #formstyle='divs'
                   #formstyle = 'bootstrap'
                   #formstyle='ul'
                   # msw: klappt nicht: buttons = [TAG.button('Back',_type="button",_onClick = "parent.location='%s' " % 'http://www.spiegel.de', TAG.button('Next',_type="submit"))]
                    deletable=True,
                    buttons = [A("Go to another page",_class='btn',_href="http://www.spiegel.de")]

                   )
    #form = SQLFORM(db.asylum_pbase,
    #    record=None,     # The optional second argument turns the INSERT form into an UPDATE form for the
    #                      # specified record (see next subsection
    #    deletable=False, # If deletable is set to True, the UPDATE form displays a "Check to delete" checkbox.
    #                      # The value of the label for this field is set via the delete_label argument.
    #    linkto=None,      #linkto and upload are optional URLs to user-defined controllers that allow the form to deal with reference fields. This is discussed in more detail later in the section.
    #    upload=None,
    #    fields=None,       # fields is an optional list of field names that you want to display.
    #                       #  If a list is provided, only fields in the list are displayed
    #    labels=None,      # labels is a dictionary of field labels. The dictionary key is a field name and the
    #                       # corresponding value is what gets displayed as its label. If a label is not provided,
    #                       # web2py derives the label from the field name (it capitalizes the field name and replaces
    #                       # underscores with spaces). For example: labels = {'name':'Your Full Name:'}
    #    col3={},           # col3 is a dictionary of values for the third column. For example:
                            # col3 = {'name':A('what is this?', _href='http://www.google.com/search?q=define:name')}
    #    submit_button='Submit', # submit_button sets the value of the submit button.

    #    delete_label='Check to delete:',
    #    showid=True,      # The "id" of the record is not shown if showid is set to False.
    #    readonly=False,   # readonly. If set to True, displays the form as readonly
    #    comments=True,    # comments. If set to False, does not display the col3 comments
    #    keepopts=[],
    #    ignore_rw=False,
    #    record_id=None,         # ??? id_label sets the label of the record "id" ???
    #    formstyle='table3cols',formstyle determines the style to be used when serializing the form in html.
    #                           In a modern app based on the Welcome scaffolding app, the default formstyle is set in db.py using the
    #                           application's private/appconfig.ini file; the default is currently bootstrap3_inline. Other options are
    #                           "bootstrap3_stacked","bootstrap2", "table3cols", "table2cols" (one row for label and comment,
    #                           and one row for input), "ul" (makes an unordered list of input fields), "divs" (represents the form using css
    #                           friendly divs, for arbitrary customization), "bootstrap" which uses the bootstrap 2.3 form class "
    #                           form-horizontal". formstyle can also be a function which generates everything inside the FORM tag.
    #                           You pass to your form constructor function two arguments, form and fields.
    #                           Hints can be found in the source code file sqlhtml.py (look for functions named formstyle_)
    #    buttons=['submit'],    #buttons is a list of INPUTs or TAG.buttons (though technically could be any
    #                           combination of helpers) that will be added to a DIV where the submit button would go.
    #    separator=': ',
    #    **attributes)


    return dict(form=form)

# -------------
@auth.requires_login()
def create_pbase():
    form = SQLFORM(db.asylum_pbase)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL('show_pbase'))

    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

    #form = crud.create(db.asylum_pbase, next='show_pbase')
    #return locals()

# -------------
@auth.requires_login()
def update_pbase():
    #pbase = db.company(request.args(0)) or redirect(URL('show_pbase'))
    record = db.asylum_pbase(request.args(0)) or redirect(URL('show_pbase'))
    form = SQLFORM(db.asylum_pbase, record)

    if form.process().accepted:
        session.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

    #form = crud.update(db.asylum_pbase, , next='companies')
    #return locals()

# -------------
@auth.requires_login()
def grid1_pbase():

    # show entries depending on other conditions
    db.asylum_pbase.bankiban.show_if = (db.asylum_pbase.testbool == True)

    # use the superpower of grids
    grid = SQLFORM.grid(db.asylum_pbase, # the datebase or a query

                        # fields: leave "None" (==default) or specify names to show
                        #fields=[db.asylum_pbase.name, db.asylum_pbase.firstname],

                        # headers: ???
                        #headers={'auth_user.email' : 'Email Address'},

                        # selectable: create checkboxes for each entry and define what to do if submitted
                        #selectable = lambda ids : redirect(URL('asylum', 'writenames_test', vars=dict(id=ids))),
                        #selectable = ??? [('button label1',lambda=ids: redirect(ids)),('button label2',lambda=ids:redirect(ids))],

                        # links?
                        #links = dict(header='name',body=lambda row: A('link to spiegel', _href='http://www.spiegel.de')),


                        # exportclasses: suppress some output options or add new ones (how?)
                        #exportclasses = dict(xml=False, html=False),
                        onvalidation=my_onvalidate,
                        oncreate=my_oncreate,
                        onupdate= my_onaccepted,
                        ondelete=my_ondelete,

                        )
    #table_name = 'asylum_healthinsurance'
    #field_name = 'name'
    #element_id = 'w2p_value_%s-%s' % (table_name, field_name)
    #custom_select = SELECT('', 'value1', 'value2', 'value3', _id=element_id)
    #grid.element('input',_id=element_id, replace=custom_select)

    return locals()

    #return dict(grid=grid)

# -------------
@auth.requires_login()
def grid_healthinsurance():

    # show entries depending on other conditions
    #db.asylum_healthinsurance.name.show_if = <some db query> ex: (db.asylum_pbase.testbool == True)

    form = SQLFORM.smartgrid(db.asylum_healthinsurance,)
    return locals()


# -------------
@auth.requires_login()
def grid_accommodation():
    grid = SQLFORM.smartgrid(db.asylum_accommodation,)
    return locals()
# -------------
@auth.requires_login()
def grid_accommodation():
    grid = SQLFORM.smartgrid(db.asylum_accommodation,)
    return locals()

# -------------
def my_onvalidate(form):
    print "In onvalidation callback"
    #print 'args   =', request.args
    #print 'args(2)=', request.args(2)
    #print form.vars

    #form.errors= True  #this prevents the submission from completing (if any test below fails)

    # get the IBAN number out of the current form
    iban_tmp = str(form.vars.bankiban)
    print "IBAN to test:", iban_tmp

    #if not iban_tmp:
    if iban_tmp == "":
        #form.errors = False
        session.flash = T("warning: IBAN number is not set")

    elif check_IBAN(iban_tmp):
        print '\tIBAN is OK'
        #form.errors = False
        session.flash = "IBAN is OK, will get inserted into database" # use 'session.flash' as form has no errors
                                                                      # and will be redirected
    else:
        print '\tIBAN has errors'
        form.errors = True
        response.flash = "IBAN is WRONG - please give a correct number"


    print "\naaaaaaaaaaaaa"
    print form.vars
    print form.vars.healthinsurance
    helth_tmp = form.vars.healthinsurance

    print "\n request.args", request.args
    #db.asylum_pbase.insert(healthinsurance=helth_tmp)


    # return NOTHING: onvalidate functions do not return anything



# -------------
def my_oncreate(form):
    print "my_oncreate"
    print form.vars

# -------------
def my_onaccepted(form):
    print "my_onaccepted"
    print form.vars

# -------------
def my_ondelete():
    print "a call to my_ondelete"




# -------------
def check_IBAN(iban_tmp):
    """ check IBAN - this little peace of code is here in it's own module for demonstration purposes. In addition,
    it might be comfortable, to separate the functionality(s) form the my_onvalidate function (hmmmm).
    a valid IBAN-number for testing this fuction would be: ibannum = 'DE29100500001061045672' """
    # param: iban_tmp the iban to test (as a string)

    # import validators
    from validators import iban

    returnval = iban(iban_tmp)
    print "'D' check_IBAN(...) will return:", returnval

    return returnval

# -------------
def writenames_test():
    import sys
    print "sys.path=", sys.path
    #response.flash = "hallo", request.vars
    #print "a call to writename_test()"

    return dict()


# -------------
# msw: taken from the cookbook (p. 56) - what does this code do exactly?
def download(): return response.download(request, db)

# -------------
# msw: taken from the cookbook (p. 56) - what does this code do exactly?
def user(): return dict(form=auth())

# -------------

# -------------

# -------------
