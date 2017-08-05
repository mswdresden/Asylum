
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

    linklist1 = UL(
        LI(A('', 'asyl_manage healthinsurance', _href=URL('asyl_manage', args=('asyl_healthinsurance'))), _class='test', _id=0),
        LI(A('', 'asyl_manage pbase', _href=URL('asyl_manage', args=('asyl_pbase'))), _class='test', _id=0),
        LI(A('', 'asyl_manage checklist', _href=URL('asyl_manage', args=('asyl_checklist'))), _class='test', _id=0),
        LI(A('', 'asyl_manage address', _href=URL('asyl_manage', args=('asyl_address'))), _class='test', _id=0),
        LI(A('', 'asyl_firstcontroller', _href=URL('asyl_firstcontroller')), _class='test', _id=0),
        LI(),
        LI(A('', 'asyl_pbasegrid', _href=URL('asyl_pbasegrid')), _class='test', _id=0),
        LI(A('', 'show_checklist', _href=URL('show_checklist', args='1')), _class='test', _id=0),
        LI(A('', 'show_address', _href=URL('show_address')), _class='test', _id=0),
        LI(A('', 'show_pbase', _href=URL('show_pbase')), _class='test', _id=0),
        LI(),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
    )
    linklist2 = UL(
        LI(A('', 'asyl_smartgrid', _href=URL('asyl_smartgrid')), _class='test', _id=0),
    )

        #LI(A('', '', _href=URL('')), _class='test', _id=0),

    return locals()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():
    response.flash = "There was an error"

    # msw: is there a way to retrieve here in this function an meaningful error message?
    err_mes = T('please figure out how to write a meaningful error message from within this function')
    return dict(err_mes=err_mes)

# ---------------
# manage any table using a grid, give table name as arg(0), e.g. .../<app>/<controller>/examples_manage/<table_name>
@auth.requires_login()
def asyl_manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table], args=request.args[:1],)
    return locals()

########################
# controllers for asyl #
########################


# --------------------
def asyl_firstcontroller():
    print 'list all fields of a table, db.asyl_pbase.fields:'; print db.asyl_pbase.fields
    # THIS DOES NOT WORK ...
    # print 'value of field internalname:'; print db.asyl_pbase.internalname

    # ... get database, do a query, select and loop over all the rows
    table = db.asyl_pbase
    for row in db(table.id > 0).select():
        print row
        print 'internalname is:', row.internalname

    retval = 'hellow world'
    return dict(retval=retval)

# --------------------
#show checklist for pbase_id number arg(0)
def show_checklist():
    request.flash = 'this is show_checklist'

    pbase_id = request.args(0)
    print 'pbase_id:', pbase_id

    print 'you can loop'

    rowsall = db().select(db.asyl_checklist.ALL)
    for row in rowsall:
        print 'id=%s, name=%s, pbase_id=%s, pbase_id.name=%s' % (row.id, row.name, row.pbase_id, row.pbase_id.name)

    print 'i count:', db(db.asyl_checklist.pbase_id == pbase_id).count()

    print 'select the rows with pbase_id equals the desired id (there should be one and only one)'
    rows = db(db.asyl_checklist.pbase_id==pbase_id).select()
    for row in rows:
        print  'ROW: id=%s, name=%s, pbase_id=%s, pbase_id.name=%s' % (row.id, row.name, row.pbase_id, row.pbase_id.name)


    print'\nget the internalname of the person'
    rows = db(db.asyl_pbase.id == pbase_id).select()
    for row in rows:
        print row

    iname = rows[0].internalname
    print iname

    url = URL('download')
    link = URL('list_records', args='db')

    record = db.asyl_checklist(db.asyl_checklist.pbase_id == pbase_id)
    form = SQLFORM(db.asyl_checklist, record,
                   deletable=True,
                   upload=url, linkto=link,
                   buttons = [
                   TAG.button(T('submit'), _type="submit"),
                   TAG.button(T('Pbase'), _type="button",
                             _onClick="parent.location='%s' " % URL('show_pbase', args=id)),
                  # TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=id)),
                    ],)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return dict(pbase_id=pbase_id,rows=rows, form=form, iname=iname)

# --------------------
#show address for pbase_id number arg(0)
def show_address():
    request.flash = 'this is show_address'

    pbase_id = request.args(0)

    record = db.asyl_address(db.asyl_address.pbase_id == pbase_id)
    form = SQLFORM(db.asyl_address, record,
                   deletable=False,
                   buttons=[
                       TAG.button(T('submit'), _type="submit"),
                       TAG.button(T('Pbase'), _type="button",
                                  _onClick="parent.location='%s' " % URL('show_pbase', args=id)),
                       # TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=id)),
                   ],
                   )
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return locals()

# --------------------
#show  for pbase_id number arg(0)
def show_pbase():
    request.flash = 'this is show_pbase'

    pbase_id = request.args(0)

    record = db.asyl_pbase(db.asyl_pbase.id == pbase_id)

    url = URL('download')
    link = URL('list_records', args='db')
    form = SQLFORM(db.asyl_pbase, record,
                   deletable=True,
                   upload=url, linkto=link,
                   labels = {'asyl_checklist.pbase_id':"This's persons Checklist",
                             'asyl_address.pbase_id': "This's persons Address",},
                   )

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return locals()



# --------------------
# shows the pbase in a grid
@auth.requires_login()
def asyl_pbasegrid():

    def my_oncreate(form):
        print 'create!'
        print  form.vars
        print  form.vars.name
        print  form.vars.internalname


        # def my_onvalidate(form):
        # def my_onaccepted(form):
        # def my_ondelete()

    query = db.asyl_pbase.id > 0

    #for row in db(query).select():
    #    print row
    #    print 'internalname is:', row.internalname

    # show only CSV and disable other formats.
    # see: http://rootpy.com/Export-in-SQLFORM-grid/

    #
    export_classes = dict(csv_with_hidden_cols=False, tsv=False, html=False,
                          tsv_with_hidden_cols=False, json=False, xml=False)

    form = SQLFORM.grid(db.asyl_pbase,
        links = [lambda row: A('Checklist',
                                   _href=URL('show_checklist',args=[row.id])),
                 lambda row: A('Address',
                                    _href=URL('show_address', args=[row.id])),

                 ],
        showbuttontext = False,  # don't show button text, just icons
        exportclasses = export_classes,
        oncreate  = my_oncreate,
        #onvalidate= my_onvalidate,
        #onupdate  = my_onaccepted,
        #ondelete  = my_ondelete,
    )


    return locals()


# --------------------
# shows the pbase in a grid
@auth.requires_login()
def asyl_checklistgrid():

    form = SQLFORM.grid(db.asyl_checklist)

    return locals()


# --------------------
# show all (linked) tables together (using a smartgrid)
@auth.requires_login()
def asyl_smartgrid():
    grid = SQLFORM.smartgrid(db.asyl_pbase,linked_tables=['asyl_checklist', 'asyl_address'],
            showbuttontext=False, # don't show button text, just icons
            exportclasses = dict(csv=True, json=False, html=False,
                          tsv=False, xml=False, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False),

            )

    return locals()
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

    # book: records = db(db[table][field]==id).select()
    record = db[table](db[table][field] == id)

    #url = URL('download')
    #link = URL('list_records', args='db')

    form = SQLFORM(db[table], record,
                   #upload=url, linkto=link,
                   #labels = {'asyl_checklist.pbase_id':"This's persons Checklist",
                   #buttons = [A("Go to another page",_class='btn',_href="http://www.spiegel.de")]
                   buttons = [
                        TAG.button(T('submit'), _type="submit"),
                        TAG.button(T('Pbase'),_type="button",_onClick = "parent.location='%s' " % URL('show_pbase', args=id)),
                        #TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=id)),
                          ]
                   )
    return locals()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
