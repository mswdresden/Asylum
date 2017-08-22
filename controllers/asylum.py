
#  import things if you need them
from gluon import * # is this really needed, as we import also in the model, hmmm?
import collections

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
        LI(A('', 'asylum_manage healthinsurance', _href=URL('asylum_manage', args=('asylum_healthinsurance'))), _class='test', _id=0),
        LI(A('', 'asylum_manage accommodation', _href=URL('asylum_manage', args=('asylum_accommodation'))), _class='test',
           _id=0),
        LI(A('', 'asylum_manage pbase', _href=URL('asylum_manage', args=('asylum_pbase'))), _class='test', _id=0),
        LI(A('', 'asylum_manage checklist', _href=URL('asylum_manage', args=('asylum_checklist'))), _class='test', _id=0),
        LI(A('', 'asylum_manage address', _href=URL('asylum_manage', args=('asylum_address'))), _class='test', _id=0),
        LI(A('', 'asylum_manage edu', _href=URL('asylum_manage', args=('asylum_edu'))), _class='test', _id=0),
        LI(A('', 'asylum_manage socialwellfare', _href=URL('asylum_manage', args=('asylum_socialwellfare'))), _class='test', _id=0),
        LI(A('', 'asylum_manage mobility', _href=URL('asylum_manage', args=('asylum_mobility'))), _class='test', _id=0),
        LI(A('', 'asylum_manage child', _href=URL('asylum_manage', args=('asylum_child'))), _class='test', _id=0),
        # LI(A('', '', _href=URL('')), _class='test', _id=0),
    )
    linklist2 = UL(
        LI(A('', 'asylum_pbasegrid', _href=URL('asylum_pbasegrid')), _class='test', _id=0),
        LI(A('', 'asylum_querygrid', _href=URL('asylum_querygrid#gridanchor')), _class='test', _id=0),
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
        LI(A('', 'asylum_smartgrid', _href=URL('asylum_smartgrid')), _class='test', _id=0),
        LI(A('', 'asylum_truncate', _href=URL('asylum_truncate')), _class='test', _id=0),
        LI(A('', 'asylum_prepopulate', _href=URL('asylum_prepopulate')), _class='test', _id=0),
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
def asylum_manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table], args=request.args[:1],)
    return locals()


# ---------------
@auth.requires_login()
def export_import():
    form = SQLFORM.factory(
        Field('table_name', requires=IS_NOT_EMPTY(),
              comment=T('ex/im: tablename, e.g. asylum_accommodation; ex/im-ALL: filename (in .../private/CSV/)')),
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
# controllers for asyl #
########################


# --------------------
#show checklist for pbase_id number arg(0)
@auth.requires_login()
def show_checklist():

    pbase_id = request.args(0)
    record = db.asylum_checklist(db.asylum_checklist.pbase_id == pbase_id)
    if not record:
        message = '\n asyl/show_checklist:\n arg0 (%s) leads to no existing pbase' % pbase_id
        redirect(URL('error',  vars=dict(message=message)))

    iname = record.internalname
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")

    form = SQLFORM(db.asylum_checklist, record,
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

    isempty = db(db.asylum_pbase.id == pbase_id).isempty()
    if isempty:
        message = '\n asyl/asylum_pbase:\n arg0 (%s) leads to no existing pbase (no id found)' % (pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    record = table(table.pbase_id == pbase_id)
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
    table = db.asylum_address
    pbase_id = request.args(0)

    db.asylum_address.standardaccommodation.show_if = (db.asylum_address.showstanndard == True)
    db.asylum_address.street.show_if = (db.asylum_address.showstanndard == False)
    db.asylum_address.housenumber.show_if = (db.asylum_address.showstanndard == False)
    db.asylum_address.numberadd.show_if = (db.asylum_address.showstanndard == False)
    db.asylum_address.zip.show_if = (db.asylum_address.showstanndard == False)
    db.asylum_address.city.show_if = (db.asylum_address.showstanndard == False)

    iname, linklist, form = __do_work(pbase_id=pbase_id, table=table)



    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()


# --------------------
@auth.requires_login()
def show_edu():
    table = db.asylum_edu
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
    table = db.asylum_socialwellfare
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
    table = db.asylum_mobility
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

    isempty = db(db.asylum_pbase.id == pbase_id).isempty()

    if isempty:
        message = '\n asyl/%s:\n arg0 (%s) leads to no existing pbase' % (db.asylum_pbase.name, pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    iname = db(db.asylum_pbase.id == pbase_id).select().first().internalname

    form = SQLFORM.grid(db.asylum_child.pbase_id == pbase_id,args=request.args[:1],
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
    isempty = db(db.asylum_pbase.id == pbase_id).isempty()
    if isempty:
        message = '\n asyl/%s:\n arg0 (%s) leads to no existing pbase' % (db.asylum_pbase.name, pbase_id)
        redirect(URL('error', vars=dict(message=message)))

    # get a (the, there is only one) record in order to fill the form with the 'hidden data'
    my_record = db.asylum_pbase(db.asylum_pbase.id == pbase_id)

    form = SQLFORM(db.asylum_child,)

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
    record = db.asylum_pbase(db.asylum_pbase.id == pbase_id)
    if not record:
        message = '\n asyl/show_pbase:\n arg0 (%s) leads to no existing pbase' % pbase_id
        redirect(URL('error',  vars=dict(message=message)))
    iname = record.internalname
    linklist = __nav_bottons(pbase_id, btn_style="btn btn-default")

    #url = URL('download')
    #link = URL('list_records', args='db')

    form = SQLFORM(db.asylum_pbase, record,
                   deletable=True,
                   #upload=url, linkto=link,
                   #labels = {'asylum_checklist.pbase_id':"This's persons Checklist",
                   #          'asylum_address.pbase_id': "This's persons Address",},
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

    row = db(db.asylum_pbase.id == pb_id).select().first()

    pb_name = row.name
    pb_firstname = row.firstname
    pb_identno  = row.identno
    pb_internalname = str(pb_name+', '+pb_firstname+', '+pb_identno)

    row.update_record(internalname=pb_internalname)

    db.asylum_checklist.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asylum_address.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asylum_edu.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                         pbase_id=pb_id)
    db.asylum_socialwellfare.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                         pbase_id=pb_id)
    db.asylum_mobility.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                         pbase_id=pb_id)

# -----------------
def pbasegrid_onaccepted(form):
    print '\n call to pbasegrid_onaccepted\n'

    pb_id = form.vars.id

    row = db(db.asylum_pbase.id == pb_id).select().first()

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
    row_cl = db(db.asylum_checklist.pbase_id == pb_id).select().first()
    row_cl.update_record(name        =pb_name)
    row_cl.update_record(firstname   =pb_firstname)
    row_cl.update_record(identno     =pb_identno)
    row_cl.update_record(internalname=pb_internalname)
    #print row_cl

    # update address
    row_ad = db(db.asylum_address.pbase_id == pb_id).select().first()
    row_ad.update_record(name        =pb_name)
    row_ad.update_record(firstname   =pb_firstname)
    row_ad.update_record(identno     =pb_identno)
    row_ad.update_record(internalname=pb_internalname)
    #print row_ad

    # update edu
    row_ed = db(db.asylum_edu.pbase_id == pb_id).select().first()
    row_ed.update_record(name=pb_name)
    row_ed.update_record(firstname=pb_firstname)
    row_ed.update_record(identno=pb_identno)
    row_ed.update_record(internalname=pb_internalname)
    # print row_ed

    # update socialwellfare
    row_sw = db(db.asylum_socialwellfare.pbase_id == pb_id).select().first()
    row_sw.update_record(name=pb_name)
    row_sw.update_record(firstname=pb_firstname)
    row_sw.update_record(identno=pb_identno)
    row_sw.update_record(internalname=pb_internalname)
    # print row_sw

    # update mobility
    row_mo = db(db.asylum_mobility.pbase_id == pb_id).select().first()
    row_mo.update_record(name=pb_name)
    row_mo.update_record(firstname=pb_firstname)
    row_mo.update_record(identno=pb_identno)
    row_mo.update_record(internalname=pb_internalname)
    # print row_mo

    # update children
    rows = db(db.asylum_child.pbase_id == pb_id).select()
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
def asylum_pbasegrid():

   # query = db.asylum_pbase.id > 0
#
    #export_classes = dict(csv_with_hidden_cols=False, tsv=False, html=False,
    #                      tsv_with_hidden_cols=False, json=False, xml=False)

    form = SQLFORM.grid(db.asylum_pbase,
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
        paginate=5,

    )
    return locals()



# --------------------
# show all (linked) tables together (using a smartgrid)
@auth.requires_login()
def asylum_smartgrid():
    grid = SQLFORM.smartgrid(db.asylum_pbase,linked_tables=['asylum_checklist', 'asylum_address'],
            showbuttontext=False, # don't show button text, just icons
            exportclasses = dict(csv=True, json=False, html=False,
                          tsv=False, xml=False, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False),

            )

    return locals()

# --------------------
@auth.requires_login()
def asylum_querygrid():

    # ----
    def _fill_show_odict(table, olist, lst):
        # params: db.table ordered_list list
        print '_fill_show_odict for table name= ', table.name.tablename

        manager = False
        fields_tmp = table.fields()

        for n in fields_tmp:
            #print n
            fill = False
            if manager == True:
                    fill = True
            elif table.name.tablename == 'asylum_pbase':
                #print 'pbase checking'
                #print table
                #print table.name

                if ((n != 'id') & (n != 'uuid') & (n != 'internalname') & (n != 'is_active') &
                        (n != 'created_on') & (n != 'created_by') & (n != 'modified_on') & (n != 'modified_by')):
                    fill = True
            else:
                #print 'other checking'
                if ((n != 'id') & (n != 'uuid') & (n != 'name') & (n != 'firstname') & (n != 'identno') & \
                        (n != 'internalname') & (n != 'pbase_id') & (n != 'is_active') & (n != 'created_on') & \
                        (n != 'created_by') & (n != 'modified_on') & (n != 'modified_by')):
                    fill = True
            if fill == True:
                #print 'fill is True'
                #print "table: ", table
                #print "n: ", n
                if  (table.name.tablename=='asylum_pbase') and (n=="name" or n=='firstname' or n=='identno'):
                    #print '\t\t => fill is True'
                    olist[n] = True  # set one thing to true for the start
                else:
                    #print '\t\t => fill is False'
                    olist[n] = False # default to false
                #lst.append(T('%s') % n)    # does not work
                #lst.append(T('%s'% n) )  # works, but gets confused by internationalization
                lst.append(n)  # works, but no transation
    # ----
    def _fill_widget_default_list(dic, lst):
        #print "\n _fill_widget_default_list(...)"
        for k, v in dic.iteritems():
            #print "key=%s, value=%s" % (k,v)
            if v==True:
                lst.append(k)
            else:
                lst.append(None)


    # Pbase
    pbase_show = collections.OrderedDict() # ordered dict of fields to show
    pbase_show_lst = [] # list containing all fields to show
    pbase_widget_default = [] # list containing value ore None for the default setting of the checkboxes
    _fill_show_odict(db.asylum_pbase, pbase_show, pbase_show_lst)
    _fill_widget_default_list(pbase_show, pbase_widget_default)

    # Checklist
    checklist_show = collections.OrderedDict()
    checklist_show_lst = []
    checklist_widget_default = []
    _fill_show_odict(db.asylum_checklist, checklist_show, checklist_show_lst)
    _fill_widget_default_list(checklist_show,checklist_widget_default)

    # Address
    address_show = collections.OrderedDict()
    address_show_lst = []
    address_widget_default = []
    _fill_show_odict(db.asylum_address, address_show, address_show_lst)
    _fill_widget_default_list(address_show,address_widget_default)

    # Edu
    edu_show = collections.OrderedDict()
    edu_show_lst = []
    edu_widget_default = []
    _fill_show_odict(db.asylum_edu, edu_show, edu_show_lst)
    _fill_widget_default_list(edu_show, edu_widget_default)

    # asylum_socialwellfare
    socialwellfare_show = collections.OrderedDict()
    socialwellfare_show_lst = []
    socialwellfare_widget_default = []
    _fill_show_odict(db.asylum_socialwellfare, socialwellfare_show, socialwellfare_show_lst)
    _fill_widget_default_list(socialwellfare_show, socialwellfare_widget_default)

    # asylum_mobility
    mobility_show = collections.OrderedDict()
    mobility_show_lst = []
    mobility_widget_default = []
    _fill_show_odict(db.asylum_mobility, mobility_show, mobility_show_lst)
    _fill_widget_default_list(mobility_show, mobility_widget_default)

    form_fields = [Field("hallo"), Field("ball")]
    form_test = SQLFORM.factory(*form_fields)


    fname_lst = ['showpbase', 'showchecklist', 'showaddress', 'showedu', 'showsocialwellfare', 'showmobility']
    qname_lst = ['querypbase', 'querychecklist', 'queryaddress', 'queryedu', 'querysocialwellfare', 'querymobility']
    form2_select_shown = SQLFORM.factory(
        Field(fname_lst[0], requires=IS_IN_SET(pbase_show_lst, multiple=True),
            #widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(pbase_show_lst), labels=['a','b','c'], _class='well', _width = '100%'),
            widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(pbase_show_lst),
                                                                            #label={v: T(v) for k, v in enumerate(pbase_show_lst)},
                                                                           _class='well', _width='100%'),

            default= pbase_widget_default,
            label=T('Select PBase Items')),
        Field(fname_lst[1], requires = IS_IN_SET(checklist_show_lst, multiple=True),
            widget = lambda field,value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(checklist_show_lst), _class='well',_width = '100%'),
            default=checklist_widget_default,
            label=T('Checklist')),
        Field(fname_lst[2], requires=IS_IN_SET(address_show_lst, multiple=True),
            widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(address_show_lst),
                _class='well',_width = '100%'),
                default=address_widget_default,
                label=T('Address')),
        Field(fname_lst[3], requires=IS_IN_SET(edu_show_lst, multiple=True),
              widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(edu_show_lst),
                                                                            _class='well', _width='100%'),
              default=edu_widget_default,
              label=T('Edu')),
        Field(fname_lst[4], requires=IS_IN_SET(socialwellfare_show_lst, multiple=True),
              widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(socialwellfare_show_lst),
                                                                            _class='well', _width='100%'),
              default=socialwellfare_widget_default,
              label=T('Socialwellfare')),
        Field(fname_lst[5], requires=IS_IN_SET(mobility_show_lst, multiple=True),
              widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(mobility_show_lst),
                                                                            _class='well', _width='100%'),
              default=mobility_widget_default,
              label=T('Mobility')),
        Field('showquery', type='boolean', default=False, label='Show the query fields'),

        Field(qname_lst[0], requires=IS_IN_SET(pbase_show_lst, multiple=True),
            widget=lambda field, value: SQLFORM.widgets.checkboxes.widget(field, value, cols=len(pbase_show_lst)),
            default= pbase_widget_default,
            label=T('Query PBase Items')),

        Field('bool1', type='boolean'),
        Field('bool2', type='boolean'),
        Field('bool3', type='boolean'),

        Field('querymovein',type='date', label=T('Move-In Date')),
        Field('querycitizenship', requires=IS_IN_SET(asylum_citizenship), label=T('Which Citizenship')),
    )
    form2_select_shown.add_button('Back', URL('index'))
    form2_select_shown['_style']='border:1px solid black'
    #form2_select_shown['_class'] = 'well'
    #form2_select_shown.no_table_field1.show_if = (False)

    query_dict = dict()

    if form2_select_shown.process(keepvalues=True, formname='form_two').accepted:

        for tab in fname_lst:
            fields_arr = form2_select_shown.vars[tab]
            for field in fields_arr:
                print "\t tab=%s, field=%s " % (tab, field)
                pbase_show[field] = True
                if tab =='showpbase':
                    pbase_show[field] = True
                if tab == 'showchecklist':
                    checklist_show[field] = True
                if tab == 'showaddress':
                    address_show[field] = True
                if tab == 'showedu':
                    edu_show[field] = True
                if tab == 'showsocialwellfare':
                    socialwellfare_show[field] = True
                if tab == 'showmobility':
                    mobility_show[field] = True

        query_dict['showquery']        = ['void', 'void', form2_select_shown.vars['showquery']]
        query_dict['querymovein']      = ['asylum_checklist', 'moveindate', form2_select_shown.vars['querymovein']]
        query_dict['querycitizenship'] = ['asylum_pbase', 'citizenship', form2_select_shown.vars['querycitizenship']]

    elif form2_select_shown.errors:
        response.flash = 'form2 has errors'


    # Query
    print "\n\n ------- \n ", query_dict.items()

    query_fields = [Field('myquery', label=T('My Query'))]
    for key, val in pbase_show.iteritems():
        print "key/value in ODict: %s %s" %  (key, val)
        if val == True:
            query_fields.append(Field((str(key)) ))


    query_form = SQLFORM.factory(*query_fields
        #Field('myquery', label=T('My Query'))
    )
    my_query = '1==1'
    if query_form.process(keepvalues=True, formname='query_form').accepted:
        my_query = query_form.vars.myquery

    response.flash = my_query

    # the query of everything
    query_all = (db.asylum_pbase.id == db.asylum_checklist.pbase_id) \
            & (db.asylum_pbase.id == db.asylum_address.pbase_id) \
            & (db.asylum_pbase.id == db.asylum_edu.pbase_id) \
            & (db.asylum_pbase.id == db.asylum_socialwellfare.pbase_id) \
            & (db.asylum_pbase.id == db.asylum_mobility.pbase_id) \
            #& (db.asylum_pbase.id<200)
            # & (my_query)
    #query = query_all & (db.asylum_pbase.birthday>'2001-05-05') # query date
    query = query_all & (db.asylum_pbase.name[:1]=='M') # query the first letter is an 'M'

    my_q = __get_query(query_dict)


    print "\n ooooooooooooooooo\n ", query_dict
    q=True
    if query_dict.has_key('showquery'):
        print "setting q"
        print query_dict.items()
        print query_dict['querymovein'][2]
        print query_dict['querycitizenship'][2]
        # TODO: test and debug, add more queries, at best 'all'
        # think of something nice and fancy to work with (custom form with automatically appearing fields)
        q =  ((db[query_dict['querycitizenship'][0]][query_dict['querycitizenship'][1]] == query_dict['querycitizenship'][2]) \
                if (query_dict['querycitizenship'][2] != '') else (True)) & \
                ((db[query_dict['querymovein'][0]][query_dict['querymovein'][1]] > query_dict['querymovein'][2]) \
                if (query_dict['querymovein'][2]!='') else (True)) #& \


        #for k, v in qdict.iteritems():
    #    if k == 'showquery':
    #        continue
#
    #    print k, v
    #    if k == 'querymovein':
    #        q = (db[v[0]][v[1]] > '1990-01-01')
    #    if k == 'citizenship':
    #        pass


    #q = (db['asylum_pbase']['birthday'] > '1990-01-01')
    #q = (db[v[0]][v[1]] > '1990-01-01')
    print "\n -------- \n and the query is=: ",  q


    #my_q = db['asylum_pbase']['birthday'] > '1990-01-01'
    query = query_all & q

    #print 'putting together the fields, this is done for every call to the URL, so what is not set here is not displayed'
    fields = []
    #fields.append(db.asylum_pbase.name)

    # ---
    # uuid and stuff missing for manager stuff
    #if pbase_show['name']==True: fields.append(db.asylum_pbase.name)
    #name is always shown
    fields.append(db.asylum_pbase.name)

    if pbase_show['firstname']==True: fields.append(db.asylum_pbase.firstname)
    if pbase_show['identno']==True: fields.append(db.asylum_pbase.identno)
    if pbase_show['birthday']==True: fields.append(db.asylum_pbase.birthday)
    if pbase_show['arrivaldate']==True: fields.append(db.asylum_pbase.arrivaldate)
    if pbase_show['citizenship']==True: fields.append(db.asylum_pbase.citizenship)
    if pbase_show['residentstatus']==True: fields.append(db.asylum_pbase.residentstatus)
    if pbase_show['healthinsurance']==True: fields.append(db.asylum_pbase.healthinsurance)
    if pbase_show['bamfid']==True: fields.append(db.asylum_pbase.bamfid)
    if pbase_show['bankiban']==True: fields.append(db.asylum_pbase.bankiban)
    if pbase_show['familyreunion']==True: fields.append(db.asylum_pbase.familyreunion)
    if pbase_show['zab']==True: fields.append(db.asylum_pbase.zab)

    # ---
    # uuid and stuff missing for manager stuff (but first think of an intelligent logic)
    if checklist_show['moveindate']          == True: fields.append(db.asylum_checklist.moveindate)
    if checklist_show['dezi']                == True: fields.append(db.asylum_checklist.dezi  			)
    if checklist_show['mailbox_labeled' ]    == True: fields.append(db.asylum_checklist.mailbox_labeled)
    if checklist_show['appkey']              == True: fields.append(db.asylum_checklist.appkey 		)
    if checklist_show['mailkey']             == True: fields.append(db.asylum_checklist.mailkey		)
    if checklist_show['bail']                == True: fields.append(db.asylum_checklist.bail			)
    if checklist_show['heatingok']           == True: fields.append(db.asylum_checklist.heatingok  	)
    if checklist_show['bamfaddress']         == True: fields.append(db.asylum_checklist.bamfaddress    )

    # ---
    if address_show['showstanndard']         == True: fields.append(db.asylum_address.showstanndard)
    if address_show['standardaccommodation'] == True: fields.append(db.asylum_address.standardaccommodation)
    if address_show['street']                == True: fields.append(db.asylum_address.street)
    if address_show['housenumber']           == True: fields.append(db.asylum_address.housenumber)
    if address_show['numberadd']             == True: fields.append(db.asylum_address.numberadd)
    if address_show['zip']                   == True: fields.append(db.asylum_address.zip)
    if address_show['city']                  == True: fields.append(db.asylum_address.city)
    if address_show['mobile']                == True: fields.append(db.asylum_address.mobile)
    if address_show['email']                 == True: fields.append(db.asylum_address.email)

    #if address_show['pbase_id']              == True: fields.append(db.asylum_address.pbase_id)

    # ---
    if edu_show['bildungsagentur']        == True: fields.append(db.asylum_edu.bildungsagentur)
    if edu_show['profession']             == True: fields.append(db.asylum_edu.profession)
    if edu_show['germanlang']             == True: fields.append(db.asylum_edu.germanlang)
    if edu_show['education']              == True: fields.append(db.asylum_edu.education)
    if edu_show['certificates']           == True: fields.append(db.asylum_edu.certificates)
    if edu_show['languages']              == True: fields.append(db.asylum_edu.languages)
    #if edu_show['pbase_id']               == True: fields.append(db.asylum_edu.pbase_id)

    # socialwellfare
    if socialwellfare_show['wbsapplication'] == True: fields.append(db.asylum_socialwellfare.wbsapplication)
    if socialwellfare_show['wbsdate'] == True: fields.append(db.asylum_socialwellfare.wbsdate)
    if socialwellfare_show['chonicillness'] == True: fields.append(db.asylum_socialwellfare.chonicillness)
    if socialwellfare_show['aufenthaltsgestattung'] == True: fields.append(db.asylum_socialwellfare.aufenthaltsgestattung)
    if socialwellfare_show['passdeduction'] == True: fields.append(db.asylum_socialwellfare.passdeduction)
    #if edu_show['pbase_id']               == True: fields.append(db.asylum_socialwellfare.pbase_id)

    # ---
    if mobility_show['dvbaboticket']        == True: fields.append(db.asylum_mobility.dvbaboticket)
    if mobility_show['dvbexpires']             == True: fields.append(db.asylum_mobility.dvbexpires)

    form = SQLFORM.grid(query,
                        fields=fields,
                        field_id=db.asylum_pbase.id,
                        deletable=False,
                        editable=False,
                        details=False,
                        paginate=5,
                        )


    return locals()

# ------------------
def __get_query(qdict):
    print "'D' __get_query(...) ### START ###"
    q=True
    for k, v in qdict.iteritems():
        if k == 'showquery':
            continue

        print k, v
        if k == 'querymovein':
            q = (db[v[0]][v[1]] > '1990-01-01')
        if k == 'citizenship':
            pass

    #q = (db['asylum_pbase']['birthday'] > '1990-01-01')
    #q = (db[v[0]][v[1]] > '1990-01-01')
    print  q

    return q

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
                   #labels = {'asylum_checklist.pbase_id':"This's persons Checklist",
                   #buttons = [A("Go to another page",_class='btn',_href="http://www.spiegel.de")]
                   buttons = [
                        TAG.button(T('submit'), _type="submit"),
                        TAG.button(T('Pbase'),_type="button",_onClick = "parent.location='%s' " % URL('show_pbase', args=id)),
                        #TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=id)),
                          ]
                   )
    return locals()

# ----------------
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

# ----------------
def __nav_bottons(pbase_id, btn_style="btn btn-link"):

    linkover = A(T('Overview'),    _href=URL('asylum_pbasegrid'), _class='btn btn-primary')
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


# ---------------
@auth.requires_login()
def asylum_truncate():
    response.flash = 'THIS FUNCTION IS ONLY FOR DEVELOPMENT - REMOVE IN PRODUCTION!'

    ksure = False # ONLY FOR DEVELOPMENT!

    form = FORM.confirm('Do you really want to truncate all asyl tables?',{'Back':URL('index')})

    if form.accepted or ksure==True:
        db.asylum_pbase.truncate()
        db.asylum_checklist.truncate()
        db.asylum_address.truncate()
        db.asylum_edu.truncate()
        db.asylum_socialwellfare.truncate()
        db.asylum_mobility.truncate()
        db.asylum_child.truncate()

        #db.asylum_accommodation.truncate()

    return locals()

# -------------------
def asylum_prepopulate():
    # very simple way to quickly populate data in a defined manner (e.g. in order to learn and test queries)
    #
    # if you start from scratch, you need to fill first some healthinsurances and some accommodations.
    # first do with the cooresponding manager (found in asylum/index), the latter is best to import form
    # your accommodation file (if you have one) via the import/export functionality (also found in asylum/index)

    from random import randint

    def rand_date(min_y=2000, max_y=2017):
        y =randint(min_y, max_y)
        m = randint(1, 12)
        d = randint(1, 27)
        return str(str(y)+'-'+str(m)+'-'+str(d))

    def rand_helthinsurance(min_id=1, max_id=4):
        row = db(db.asylum_healthinsurance.id == randint(min_id, max_id)).select().first()
        hi = row.name
        return hi
    def rand_accommodation(min_id=1, max_id=30):
        row = db(db.asylum_accommodation.id == randint(min_id, max_id)).select().first()
        acco = row.street
        return acco

    # fill healthinsurance, if empty
    if db.asylum_healthinsurance.id <= 0:
        db.asylum_healthinsurance.insert(name="AOK",address="AOK Strasse 1")
        db.asylum_healthinsurance.insert(name="Techniker Krankenkasse", address="Bergstrasse 1")
        db.asylum_healthinsurance.insert(name="Barmer", address="Barmer-Strasse 1")
        db.asylum_healthinsurance.insert(name="IKK", address="IKK Strasse 1")

    # clean all asyl data
    #asylum_truncate(ksure=True)
    asylum_truncate()

    # define some data
    asylum_ynu = [T('Yes'), T('No'), T('unknown')]
    bool_tmp = [True, False]

    name_arr        = ['Ali','Horibi','Masuud','Krause','Schenk','Borani','Masado','Sonobene']
    firstname_arr   = ['Hassan','Marek','Ali','Mohammed','Babsi','Helene','Paul','Gertrud']
    #citizenship_arr = ['Syrien', 'Irak', 'Iran', 'Albanien', 'EU', 'Africa', 'Brasilien', 'Marokko' ]
    pb_identno    = 1000
    pb_id         = 0

    for x in range(0, 20):
        pb_name         = name_arr[randint(0,7)]
        pb_firstname    = firstname_arr[randint(0,7)]
        pb_identno     += 1
        pb_id          += 1
        pb_internalname = str(pb_firstname + ", " + pb_name + ", " + str(pb_identno))

        db.asylum_pbase.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                        birthday= rand_date(1920,2017), arrivaldate= rand_date(2014,2017),
                        citizenship=asylum_citizenship[randint(0,7)], healthinsurance=rand_helthinsurance(1,4), bamfid=pb_identno+1000,
                        familyreunion=asylum_familyreunion[randint(0, 4)], zab=pb_identno+2000, )

        db.asylum_checklist.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                        moveindate=rand_date(2016,2017), dezi=bool_tmp[randint(0,1)],
                        mailbox_labeled=bool_tmp[randint(0,1)], appkey=randint(0,5), mailkey=randint(0,5),
                        bail=randint(0,5)*10, heatingok=asylum_heatingok[randint(0,2)],bamfaddress=2,
                        pbase_id=pb_id)

        db.asylum_address.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                        street='Kaiserstrasse',housenumber=9,numberadd='HH',zip='01199',city='Dresden',
                        mobile='1771234567',
                        pbase_id=pb_id)

        db.asylum_edu.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname= pb_internalname,
                            bildungsagentur=asylum_ynu[randint(0,2)],profession = 'Doktor',
                            germanlang=asylum_langlevels[randint(1,5)], education=asylum_edulevels[randint(1,5)],
                            certificates=asylum_ynu[randint(0,2)], languages=asylum_posslanguages[randint(1,5)],
                            pbase_id=pb_id)

        db.asylum_socialwellfare.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno,
                                                                                    internalname=pb_internalname,
                            wbsapplication= asylum_ynu[randint(0,2)],
                            wbsdate= rand_date(2016,2017),
                            chonicillness= '',
                            aufenthaltsgestattung= asylum_aufenthaltsgestattung[randint(1,4)],
                            passdeduction= randint(0,9)*5,
                            pbase_id=pb_id)

        db.asylum_mobility.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                            dvbaboticket=asylum_ynu[randint(0,2)],dvbexpires= rand_date(2017,2018),
                            pbase_id=pb_id)

        # add 0-3 children
        for i in range(1,randint(0,3)):
            db.asylum_child.insert(name=pb_name, firstname=pb_firstname, identno=pb_identno, internalname=pb_internalname,
                childname = firstname_arr[randint(0,7)],
                childbirth = rand_date(2000,2016),
                childschoolreg= bool_tmp[randint(0,1)],
                childkindergarden= asylum_ynu[randint(0,2)],
                childfeefreekg = bool_tmp[randint(0,1)],
                childfeefreemeal= asylum_ynu[randint(0,2)],
                childbildungsagentur=asylum_ynu[randint(0,2)],
                pbase_id = pb_id)

    redirect(URL('index'))




# --------------------
# kann das weg, ist nur example, oder?
##show checklist for pbase_id number arg(0)
#def show_examples_checklist():
#    request.flash = 'this is show_checklist'
#
#    pbase_id = request.args(0)
#    print 'pbase_id:', pbase_id
#
#    print 'you can loop'
#
#    rowsall = db().select(db.asylum_checklist.ALL)
#    for row in rowsall:
#        print 'id=%s, name=%s, pbase_id=%s, pbase_id.name=%s' % (row.id, row.name, row.pbase_id, row.pbase_id.name)
#
#    print 'i count:', db(db.asylum_checklist.pbase_id == pbase_id).count()
#
#    print 'select the rows with pbase_id equals the desired id (there should be one and only one)'
#    rows = db(db.asylum_checklist.pbase_id==pbase_id).select()
#    for row in rows:
#        print  'ROW: id=%s, name=%s, pbase_id=%s, pbase_id.name=%s' % (row.id, row.name, row.pbase_id, row.pbase_id.name)
#
#
#    print'\nget the internalname of the person'
#    rows = db(db.asylum_pbase.id == pbase_id).select()
#    for row in rows:
#        print row
#
#    iname = rows[0].internalname
#    print iname
#
#    url = URL('download')
#    link = URL('list_records', args='db')
#
#    record = db.asylum_checklist(db.asylum_checklist.pbase_id == pbase_id)
#    form = SQLFORM(db.asylum_checklist, record,
#                   deletable=True,
#                   upload=url, linkto=link,
#                   buttons = [
#                   TAG.button(T('submit'), _type="submit"),
#                   TAG.button(T('Pbase'), _type="button",
#                             _onClick="parent.location='%s' " % URL('show_pbase', args=id)),
#                  # TAG.button(T('Address'), _type="button", _onClick="parent.location='%s' " % URL('show_address', args=id)),
#                    ],)
#
#    if form.process().accepted:
#        response.flash = 'form accepted'
#    elif form.errors:
#        response.flash = 'form has errors'
#
#    return dict(pbase_id=pbase_id,rows=rows, form=form, iname=iname)
