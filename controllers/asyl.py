
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


# disable some export options in grids
export_classes = dict(csv_with_hidden_cols=False, tsv=False, html=False,
                          tsv_with_hidden_cols=False, json=False, xml=False)


###############
# First steps #
###############

# you should always have a 'index' controller (the default, if no fuction is given in the url)
def index():

    linklist1 = UL(
        LI(A('', 'asyl_manage healthinsurance', _href=URL('asyl_manage', args=('asyl_healthinsurance'))), _class='test', _id=0),
        LI(A('', 'asyl_manage accommodation', _href=URL('asyl_manage', args=('asyl_accommodation'))), _class='test',
           _id=0),
        LI(A('', 'asyl_manage pbase', _href=URL('asyl_manage', args=('asyl_pbase'))), _class='test', _id=0),
        LI(A('', 'asyl_manage checklist', _href=URL('asyl_manage', args=('asyl_checklist'))), _class='test', _id=0),
        LI(A('', 'asyl_manage address', _href=URL('asyl_manage', args=('asyl_address'))), _class='test', _id=0),
        LI(A('', 'asyl_manage edu', _href=URL('asyl_manage', args=('asyl_edu'))), _class='test', _id=0),
        LI(A('', 'asyl_manage socialwellfare', _href=URL('asyl_manage', args=('asyl_socialwellfare'))), _class='test', _id=0),
        LI(A('', 'asyl_manage mobility', _href=URL('asyl_manage', args=('asyl_mobility'))), _class='test', _id=0),
        LI(A('', 'asyl_manage child', _href=URL('asyl_manage', args=('asyl_child2'))), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
    )
    linklist2 = UL(
        LI(A('', 'asyl_pbasegrid', _href=URL('asyl_pbasegrid')), _class='test', _id=0),

        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
    )

    linklist3 = UL(
        LI(A('', 'show_pbase', _href=URL('show_pbase', args=[1])), _class='test', _id=0),
        LI(A('', 'show_checklist', _href=URL('show_checklist', args='1')), _class='test', _id=0),
        LI(A('', 'show_address', _href=URL('show_address', args=[1])), _class='test', _id=0),
        LI(A('', 'show_edu', _href=URL('show_edu', args=[1])), _class='test', _id=0),
        LI(A('', 'show_socialwellfare', _href=URL('show_socialwellfare', args=[1])), _class='test', _id=0),
        LI(A('', 'show_mobility', _href=URL('show_mobility', args=[1])), _class='test', _id=0),
        LI(A('', 'show_children', _href=URL('show_children', args=[1])), _class='test', _id=0),
        LI(A('', 'asyl_smartgrid', _href=URL('asyl_smartgrid')), _class='test', _id=0),
        LI(A('', 'asyl_truncate', _href=URL('asyl_truncate')), _class='test', _id=0),
        LI(A('', 'asyl_prepopulate', _href=URL('asyl_prepopulate')), _class='test', _id=0),
        LI(A('', 'export_import', _href=URL('export_import')), _class='test', _id=0),

    )

        #LI(A('', '', _href=URL('')), _class='test', _id=0),

    return locals()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():

    tmp = request.vars.message or 'There was an error (but no error message given)'
    message = T("Error: %s") % (tmp)

    response.flash = message
    err_mes = T(message)
    return dict(err_mes=err_mes)

# ---------------
# manage any table using a grid, give table name as arg(0), e.g. .../<app>/<controller>/examples_manage/<table_name>
@auth.requires_login()
def asyl_manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table], args=request.args[:1],)
    return locals()


# ---------------
@auth.requires_login()
def export_import():
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
                open(file_name, 'wb').write(str(db(db['asyl_accommodation'].id).select()))
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
# controllers for asyl #
########################


# --------------------
#show checklist for pbase_id number arg(0)
@auth.requires_login()
def show_checklist():

    pbase_id = request.args(0)
    record = db.asyl_checklist(db.asyl_checklist.pbase_id == pbase_id)
    if not record:
        message = '\n asyl/show_checklist:\n arg0 (%s) leads to no existing pbase' % pbase_id
        redirect(URL('error',  vars=dict(message=message)))

    iname = record.internalname
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")

    form = SQLFORM(db.asyl_checklist, record,
                   #deletable=False,
                   #buttons = [
                   #TAG.button(T('submit'), _type="submit", _class="btn btn-primary"),
                   #TAG.button(T('Pbase'), _type="button",
                   #         _onClick="parent.location='%s' " % URL('show_pbase', args=pbase_id)),
                   #TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=pbase_id)),
                   # ],
                    )

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'


    return locals()

# --------------------
def __do_work(pbase_id, table):

    #print 'pbase_id: ' , pbase_id
    #print table.name

    isempty = db(db.asyl_pbase.id == pbase_id).isempty()
    record = table(table.pbase_id == pbase_id)

    #print isempty
    #print record

    #record2 = table(table.pbase_id == pbase_id)
    #record3 = db(table.pbase_id == pbase_id)
    #print 'record2: ', record2
    #print 'record3: ', record3

    #if not record:
    #    message = '\n asyl/show_checklist:\n arg0 (%s) leads to no existing pbase' % pbase_id
    #    redirect(URL('error',  vars=dict(message=message)))


    if isempty:
        message = '\n asyl/asyl_pbase:\n arg0 (%s) leads to no existing pbase (no id found)' % (pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    if not record:
        message = '\n asyl/%s:\n arg0 (%s) leads to no existing pbase' % (table.name, pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    iname = record.internalname
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")

    form = SQLFORM(table, record,
                   deletable=False, )

    return iname, linklist, form

# --------------------
#show address for pbase_id number arg(0)
@auth.requires_login()
def show_address():
    table = db.asyl_address
    pbase_id = request.args(0)
    iname, linklist, form = __do_work(pbase_id=pbase_id, table=table)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()


# --------------------
@auth.requires_login()
def show_edu():
    table = db.asyl_edu
    pbase_id = request.args(0)
    iname, linklist, form = __do_work(pbase_id=pbase_id, table=table)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()

# --------------------
@auth.requires_login()
def show_socialwellfare():
    table = db.asyl_socialwellfare
    pbase_id = request.args(0)
    iname, linklist, form = __do_work(pbase_id=pbase_id, table=table)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()

# --------------------
@auth.requires_login()
def show_mobility():
    table = db.asyl_mobility
    pbase_id = request.args(0)
    iname, linklist, form = __do_work(pbase_id=pbase_id, table=table)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()

# --------------------
@auth.requires_login()
def show_children():
    pbase_id = request.args(0)
    print 'pbase_id: ', pbase_id
    #

    isempty = db(db.asyl_pbase.id == pbase_id).isempty()

    if isempty:
        message = '\n asyl/%s:\n arg0 (%s) leads to no existing pbase' % (db.asyl_pbase.name, pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    iname = db(db.asyl_pbase.id == pbase_id).select().first().internalname

    form = SQLFORM.grid(db.asyl_child2.pbase_id == pbase_id,args=request.args[:1],
                        create=False,
                        searchable=False,
                        showbuttontext = False,  # don't show button text, just icons
                        exportclasses = export_classes,
    )

    link_ccreate = A(T('Add Child'), _href=URL('create_child', args=[pbase_id]), _class='btn btn-primary')
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")
    return locals()

# --------------------
@auth.requires_login()
def create_child():
    pbase_id = request.args(0)
    isempty = db(db.asyl_pbase.id == pbase_id).isempty()
    if isempty:
        message = '\n asyl/%s:\n arg0 (%s) leads to no existing pbase' % (db.asyl_pbase.name, pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    # get a (the, there is only one) record in order to fill the form with the 'hidden data'
    my_record = db.asyl_pbase(db.asyl_pbase.id == pbase_id)

    form = SQLFORM(db.asyl_child2,)

    form.vars.name = my_record.name
    form.vars.firstname= my_record.firstname
    form.vars.identno= my_record.identno
    form.vars.internalname= my_record.internalname
    form.vars.pbase_id= int(my_record.id)
    form.vars.childname = 'default childname'

    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL('show_children', args=[pbase_id]))
    elif form.errors:
        response.flash = 'form has errors'

    return dict(form=form)


# --------------------
#show  for pbase_id number arg(0)
def show_pbase():

    pbase_id = request.args(0)
    record = db.asyl_pbase(db.asyl_pbase.id == pbase_id)
    if not record:
        message = '\n asyl/show_pbase:\n arg0 (%s) leads to no existing pbase' % pbase_id
        redirect(URL('error',  vars=dict(message=message)))
    iname = record.internalname
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")

    #url = URL('download')
    #link = URL('list_records', args='db')

    form = SQLFORM(db.asyl_pbase, record,
                   deletable=True,
                   #upload=url, linkto=link,
                   #labels = {'asyl_checklist.pbase_id':"This's persons Checklist",
                   #          'asyl_address.pbase_id': "This's persons Address",},
                   )

    if form.process().accepted:
        pbasegrid_onaccepted(form)
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'

    return locals()


# ----------------
def pbasegrid_oncreate(form):
    print 'create!'
    #print  form.vars.name

    pb_id = form.vars.id

    row = db(db.asyl_pbase.id == pb_id).select().first()

    pb_name = row.name
    pb_firstname = row.firstname
    pb_identno  = row.identno
    pb_internalname = str(pb_name+', '+pb_firstname+', '+pb_identno)

    row.update_record(internalname=pb_internalname)

    db.asyl_checklist.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asyl_address.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asyl_edu.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asyl_socialwellfare.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                         pbase_id=pb_id)
    db.asyl_mobility.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                         pbase_id=pb_id)

# -----------------
def pbasegrid_onaccepted(form):
    print '\n call to pbasegrid_onaccepted\n'

    pb_id = form.vars.id

    row = db(db.asyl_pbase.id == pb_id).select().first()

    pb_name = row.name
    pb_firstname = row.firstname
    pb_identno  = row.identno
    pb_internalname = str(pb_name+', '+pb_firstname+', '+pb_identno)
    row.update_record(internalname=pb_internalname) # update pbase

    #print 'pb_name: ', pb_name
    #print 'pb_firstname: ', pb_firstname
    #print 'pb_identno: ', pb_identno
    #print 'pb_internalname: ', pb_internalname

    # update checklist
    row_cl = db(db.asyl_checklist.pbase_id == pb_id).select().first()
    row_cl.update_record(name        =pb_name)
    row_cl.update_record(firstname   =pb_firstname)
    row_cl.update_record(identno     =pb_identno)
    row_cl.update_record(internalname=pb_internalname)
    #print row_cl

    # update address
    row_ad = db(db.asyl_address.pbase_id == pb_id).select().first()
    row_ad.update_record(name        =pb_name)
    row_ad.update_record(firstname   =pb_firstname)
    row_ad.update_record(identno     =pb_identno)
    row_ad.update_record(internalname=pb_internalname)
    #print row_ad

    # update edu
    row_ed = db(db.asyl_edu.pbase_id == pb_id).select().first()
    row_ed.update_record(name=pb_name)
    row_ed.update_record(firstname=pb_firstname)
    row_ed.update_record(identno=pb_identno)
    row_ed.update_record(internalname=pb_internalname)
    # print row_ed

    # update socialwellfare
    row_sw = db(db.asyl_socialwellfare.pbase_id == pb_id).select().first()
    row_sw.update_record(name=pb_name)
    row_sw.update_record(firstname=pb_firstname)
    row_sw.update_record(identno=pb_identno)
    row_sw.update_record(internalname=pb_internalname)
    # print row_sw

    # update mobility
    row_mo = db(db.asyl_mobility.pbase_id == pb_id).select().first()
    row_mo.update_record(name=pb_name)
    row_mo.update_record(firstname=pb_firstname)
    row_mo.update_record(identno=pb_identno)
    row_mo.update_record(internalname=pb_internalname)
    # print row_mo

    # update children
    rows = db(db.asyl_child2.pbase_id == pb_id).select()
    for row in rows:
        row.update_record(name=pb_name)
        row.update_record(firstname=pb_firstname)
        row.update_record(identno=pb_identno)
        row.update_record(internalname=pb_internalname)


#def pbasegrid_ondelete():
#    print '\n\n call to pbasegrid_ondelete\n'
# --------------------
# shows the pbase in a grid
@auth.requires_login()
def asyl_pbasegrid():

   # query = db.asyl_pbase.id > 0
#
    #export_classes = dict(csv_with_hidden_cols=False, tsv=False, html=False,
    #                      tsv_with_hidden_cols=False, json=False, xml=False)

    form = SQLFORM.grid(db.asyl_pbase,
        links = [lambda row: A(T('Checklist'), _href=URL('show_checklist',args=[row.id])),
                 lambda row: A(T('Address'),   _href=URL('show_address', args=[row.id])),
                 lambda row: A(T('Edu'),       _href=URL('show_edu', args=[row.id])),
                 lambda row: A(T('SocWell'),   _href=URL('show_socialwellfare', args=[row.id])),
                 lambda row: A(T('Mob'),       _href=URL('show_mobility', args=[row.id])),
                 lambda row: A(T('Children'),  _href=URL('show_children', args=[row.id])),

                 ],
        showbuttontext = False,  # don't show button text, just icons
        exportclasses = export_classes,
        oncreate  = pbasegrid_oncreate,
        #onvalidate= pbasegrid_onvalidate, # does NOT exist for grid
        onupdate  = pbasegrid_onaccepted,
        #ondelete  = pbasegrid_ondelete,

    )
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

# ----------------
def __nav_bottons(pbase_id, btn_style="btn btn-link"):

    linkover = A(T('Overview'),    _href=URL('asyl_pbasegrid'), _class='btn btn-primary')
    link0 = A(T('Pbase'),          _href=URL('show_pbase',          args=[pbase_id]), _class=btn_style)
    link1 = A(T('Checklist'),      _href=URL('show_checklist',      args=[pbase_id]), _class=btn_style)
    link2 = A(T('Address'),        _href=URL('show_address',        args=[pbase_id]), _class=btn_style)
    link3 = A(T('Edu'),            _href=URL('show_edu',            args=[pbase_id]), _class=btn_style)
    link4 = A(T('Socialwellfare'), _href=URL('show_socialwellfare', args=[pbase_id]), _class=btn_style)
    link5 = A(T('Mobility'),       _href=URL('show_mobility',       args=[pbase_id]), _class=btn_style)
    link6 = A(T('Children'),       _href=URL('show_children',       args=[pbase_id]), _class=btn_style)

    return CENTER(linkover, link0,link1,link2,link3,link4,link5,link6,)

    #return link0, link1, link2
#
#  examples (clean up and move this to the examples)
#

# --------------------
#show checklist for pbase_id number arg(0)
def show_examples_checklist():
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

# ---------------
@auth.requires_login()
def asyl_truncate():
    response.flash = 'THIS FUNCTION IS ONLY FOR DEVELOPMENT - REMOVE IN PRODUCTION!'

    ksure = True # ONLY FOR DEVELOPMENT!

    form = FORM.confirm('Do you really want to truncate all asyl tables?',{'Back':URL('index')})

    if form.accepted or ksure==True:
        #response.flash = 'web2py confirmation form accepted'
        #print 'truncate'
        db.asyl_pbase.truncate()
        db.asyl_checklist.truncate()
        db.asyl_address.truncate()
        db.asyl_edu.truncate()
        db.asyl_socialwellfare.truncate()
        db.asyl_mobility.truncate()
        db.asyl_child2.truncate()

    return locals()

# -------------------
def asyl_prepopulate():
    # very simple way to quickly populate data in a defined manner (e.g. in order to learn and test queries)

    from random import randint

    def rand_date(min_y=2000, max_y=2017):
        y =randint(min_y, max_y)
        m = randint(1, 12)
        d = randint(1, 27)
        return str(str(y)+'-'+str(m)+'-'+str(d))

    # clean all asyl data
    #asyl_truncate(ksure=True)
    asyl_truncate()

    # define some data
    asylum_ynu = [T('Yes'), T('No'), T('unknown')]
    bool_tmp = [True, False]

    name_arr        = ['Ali','Horibi','Masuud','Krause','Schenk','Borani','Masado','Sonobene']
    firstname_arr   = ['Hassan','Marek','Ali','Mohammed','Babsi','Helene','Paul','Gertrud']
    citizenship_arr = ['Syrien', 'Irak', 'Iran', 'Albanien', 'EU', 'Africa', 'Brasilien', 'Marokko' ]
    pb_identno    = 1000
    pb_id         = 0

    for x in range(0, 20):
        pb_name         = name_arr[randint(0,7)]
        pb_firstname    = firstname_arr[randint(0,7)]
        pb_identno     += 1
        pb_id          += 1
        pb_internalname = str(pb_firstname + ", " + pb_name + ", " + str(pb_identno))
        citizenship     = citizenship_arr[randint(0,7)]

        db.asyl_pbase.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                          birthday= rand_date(1920,2017), healthinsurance="AOK", arrivaldate= rand_date(2014,2017), )
        db.asyl_checklist.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                          moveindate=rand_date(2016,2017),   pbase_id=pb_id)
        db.asyl_address.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                            citizenship=citizenship,  pbase_id=pb_id)
        db.asyl_edu.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                             pbase_id=pb_id)
        db.asyl_socialwellfare.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                             pbase_id=pb_id)
        db.asyl_mobility.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                            dvbaboticket=True,dvbexpires= rand_date(2017,2018),  pbase_id=pb_id)
        # add 0-3 children
        for i in range(1,randint(0,3)):
            db.asyl_child2.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                childname = firstname_arr[randint(0,7)],
                childbirth = rand_date(2000,2016),
                childschoolreg= bool_tmp[randint(0,1)],
                childkindergarden= asylum_ynu[randint(0,2)],
                childfeefreekg = bool_tmp[randint(0,1)],
                childfeefreemeal= asylum_ynu[randint(0,2)],
                childbildungsagentur=asylum_ynu[randint(0,2)],
                pbase_id = pb_id)

    redirect(URL('index'))

