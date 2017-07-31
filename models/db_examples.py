################################################################
# some test data structures for the examples controllers/views #
################################################################

# allways start with including everything from gluon
from gluon import *

# further imports
import uuid # this is needed for the creation of an uuid

#######################
# General Information #
#######################

# - Important:
#   - Models in the same folder/subfolder are executed in alphabetical order.
#   - Any variable defined in a model will be visible to other models following alphabetically,
#     to the controllers, and to the views.
#
# one can think of situations where defining something 'generic' for you model like
examples_standardstring = 'Examples make life much easier to understand - please write your own and then SHARE THEM!'
# seems reasionable to do (e.g. in order to quickly create your 'own' globals (and not messing with the db.py)) ...
# ... however ...
# ... it surtenly is crying for chaos if you define things like 'myval' or 'foo' here globaly


# - book: It is sometimes useful to create your own Storage objects. You can do so as follows:
# from gluon.storage import Storage
# my_storage = Storage()  # empty storage object
# =>> LEARN HOW TO USE THIS!!

############################
# The usage of own modules #
############################

# Modules (python code for generic use within your app) is stored in /application/<app>/modules.
# This location is allways searched first if you call an 'import'. In this way, you can add to your app
# a) your own modules
# b) all possible python modules, wich stick to your (this) app.
# (modules that belong to your 'web2py' environment go to .../web2py/site-packages)
#
# Models are usually (the python way) read only once. So if you edit them, you must restart your web2py server (or even
# restart your browser?!). It is probably convenient to set track_changes True only for development. Then the modules
# files are re-read for each function call:
from gluon.custom_import import track_changes
track_changes(True)   # the modules are read at each call to a fuction (you see changes right away)
#track_changes(False) # load modules only once (after any edit a restart of web2py is required). This makes it faster.


#
# first example
#
db.define_table('examples_person',
                Field('name', label='Name', requires=IS_NOT_EMPTY()),
    )

db.define_table('examples_dog',
                Field('dog_owner', 'reference examples_person'),
                Field('dog', label='Dog Name', requires=IS_NOT_EMPTY()),
                )
db.examples_dog.dog_owner.requires = IS_IN_DB(db,db.examples_person.id,'%(name)s')

#
db.define_table('examples_thing',
                Field('thing_owner', 'reference examples_person'),
                Field('name', label=(T('Thing Name')), requires=IS_NOT_EMPTY()),
                )
db.examples_thing.thing_owner.requires = IS_IN_DB(db,db.examples_person.id,'%(name)s')


#######################################################
#               second examples                       #
#######################################################

# The following is a second try to make a set of (referenced) tables which can be managed by a smartgrid
#
# see: two_tables, two_smart_tables,

db.define_table('examples_checklist',
        Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
        Field('name', default=T('not set')),
        Field('moveindate', type='date', requires=IS_EMPTY_OR(IS_DATE()),
                      label=T('Move-In Date'), comment=T('The date the person moved into the current accommodation')),
        Field('dezi', type='boolean',
                      label=T('Dezi Appartment'), comment=T('Is this a dezi-appartment')),
        Field('mailbox_labeled', type='boolean',
                      label=T('Mailbox Labeled'), comment=T('Is there a name label on the mailbox?')),

        auth.signature,
        format='%(name)s'
        )

db.define_table('examples_mobility',
        Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
        Field('name', default=T('not set')),

        Field('ticket', type='boolean'),
        Field('expires', type='date'),
        auth.signature,
        format='%(name)s'
        )

db.define_table('examples_edu',
        Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
        Field('name', default=T('not set')),
        Field('job', requires=IS_NOT_EMPTY()),
        Field('edu', requires=IS_IN_SET(["none", 'elementary', 'high school', 'university', 'phd'])),
        Field('german', requires=IS_IN_SET(['A0','A1','B0','B1','C'])),
        auth.signature,
        format='%(name)s'
        )

db.define_table('examples_housing',
        Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
        Field('name', default=T('not set')),

        Field('address', requires=IS_NOT_EMPTY()),
        Field('landlord',),
        Field('contact_address', ),
        Field('contact_phone', ),

        auth.signature,
        format='%(name)s'
        )

db.define_table('examples_human',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('checklist', 'reference examples_checklist',
                            requires=IS_IN_DB(db, db.examples_checklist.id, '%(name)s',
                                              zero=XML(A('create new',_href=URL('index'))))),
                Field('mobility', 'reference examples_mobility'),
                #            requires=IS_IN_DB(db, db.examples_mobility.id, '%(name)s')),
                #Field('edu', 'reference examples_edu',
                #            requires=IS_IN_DB(db, db.examples_edu.id      , '%(name)s')),
                #Field('housing', 'reference examples_housing',
                #            requires=IS_IN_DB(db, db.examples_housing.id  , '%(street)s')),
                      )

db.define_table('examples_pbase',
        Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),

        Field('name', type='string', length=100, requires=IS_NOT_EMPTY()),
        Field('firstname', type='string', length=50, requires=IS_NOT_EMPTY(), label=T('First Name'), comment=T('first and middle names')),
        Field('fullname', type='string'),
        Field('checklist', 'reference examples_checklist',
                      #requires=IS_IN_DB(db, db.asylum_checklist.uuid, '%(uuid)s'),
                      requires=IS_IN_DB(db, db.examples_checklist.id, '%(name)s'),
                      label='Checklist', comment="the checklist of this person"),
        Field('examples_mobility', 'reference examples_mobility',requires=IS_IN_DB(db, db.examples_checklist.id, '%(name)s')),
        Field('examples_edu'     , 'reference examples_edu',requires=IS_IN_DB(db, db.examples_edu, '%(name)s')),
        Field('examples_housing' , 'reference examples_housing',requires=IS_IN_DB(db, db.examples_housing.id, '%(address)s')),
        auth.signature,
        format= '%(name)s' #''%(name)s/%(id)s',
                )
#db.examples_pbase._before_insert = [lambda fields: fields.update(original=fields.get('firstname') ) ]

#if not db(db.examples_pbase).count():
#    db.examples_pbase.insert(name="Anderson",firstname="Alex")
#    db.examples_pbase.insert(name="Bernandone", firstname="Bert")
#    db.examples_pbase.bulk_insert([
#                            {'name':'Cordalis', 'firstname':'Costa'},
#                            {'name':'Dueren', 'firstname': 'Denise'},
#                            ])

db.define_table('examples_child',
        Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),

        Field('father_id', type='reference examples_pbase'),
        Field('firstname', length=50),
        Field('name', length=50,requires=IS_NOT_EMPTY()),
        Field('birthdate', type='date',requires=IS_NOT_EMPTY()),

        auth.signature,
        format='%(name)s'
        )
db.examples_child.father_id.requires = IS_IN_DB(db, db.examples_pbase.id,'%(name)s')

#if not db(db.examples_pbase.id).count():
#    id = uuid.uuid4()
#    db.examples_pbase.insert(name="Massimo", uuid=id)
#    db.examples_child.insert(father_id=id, name="Chair")


# ------------------
# skelleton
#db.define_table('asylum_',
#    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
#    Field('', type='', length=, requires=, label=T(''), comment=T('')),
#    auth.signature,
#    # format='%(name)s',
#    redefine=k_redefine,
#    )

###################################
# Smartgrid and referenced tables #
###################################

# from book: the use of a smartgrid!!
# see: parentmanager
db.define_table('parent',Field('name', requires=IS_NOT_EMPTY()), format='%(name)s')
db.define_table('child',
                Field('name'),
                Field('birthdate', type='date'),
                Field('parent','reference parent', requires=IS_IN_DB(db, db.parent.id, '%(name)s',)))

db.define_table('car',
                Field('name', requires = IS_IN_SET(['VW', 'BMW', 'Ford', 'other'])),
                Field('km', type = 'integer'),
                Field('parent','reference parent', requires=IS_IN_DB(db, db.parent.id, '%(name)s',))
                )

db.define_table('job',
                Field('name', requires = IS_IN_SET(['teacher', 'mailman', 'nurse', 'other'])),
                Field('salary', type = 'integer'),
                Field('parent','reference parent', requires=IS_IN_DB(db, db.parent.id, '%(name)s',))
                )

##################################################################
# show a field dependig on a switch (possibly in the same table) #
##################################################################

# see: showbooleffect()
db.define_table('examples_booltest',
                Field('name', requires = IS_NOT_EMPTY()),
                Field('showbool', type = 'boolean', default= 'off', label = 'shwo more info'),
                Field('moreinfo1', default = 'more ...'),
                Field('moreinfo2', default = '... info'),
                )

###############
# field types #
###############

# drop/prepopulate and simple queries
# http://www.web2pyref.com/reference/field-type-database-field-types
# # see: show_examples_fieldtypenquery, populate_examples_fieldtypenquery
db.define_table('examples_fieldtypenquery2',
                Field('my_string',        type = 'string', requires = IS_NOT_EMPTY()), #IS_LENGTH(length) default length is 512
                Field('my_text',          type = 'text'),        # IS_LENGTH(65536)
                Field('my_blob',          type = 'blob'),        # None
                Field('my_boolean',       type='boolean'),       # None
                Field('my_intnum',        type='integer'),       # IS_INT_IN_RANGE(-1e100, 1e100)
                Field('my_double',        type='double'),        # IS_FLOAT_IN_RANGE(-1e100, 1e100)
                Field('my_decimal',       type='decimal(0,10)'),  # IS_DECIMAL_IN_RANGE(-1e100, 1e100)
                Field('my_date',          type='date'),          # IS_DATE()
                Field('my_time',          type='time'),          # IS_TIME()
                Field('my_datetime',      type='datetime'),      # IS_DATETIME()
                Field('my_password',      type='password'),      # None
                Field('my_upload',        type='upload'),        # None
#                Field('my_reference <table>', type='reference <table>'), # IS_IN_DB(db,table.field,format)
                Field('my_list_string',   type='list:string'),   # None
                Field('my_list_integer',  type='list:integer'),  # None
#                Field('my_list:reference <table>', type='list:reference <table>'), #IS_IN_DB(db,table.field,format,multiple=True)
                #Field('my_json',          type='json'),          # IS_JSON()
                #Field('my_bigint',        type='bigint'),        # None msw: ???
                #Field('my_big_id',        type='big-id'),        # None msw: ???
                #Field('my_big_reference', type='big-reference'), # None msw: ???
                )

#####################
# Import/Export (1) #
#####################

# the book (chapter DAL)

# and maybe: https://groups.google.com/forum/#!topic/web2py/b-mW4VsajR4
#1.- Define the tables that are being pre-populate.
#2.- Insert all the data with appadmin.
#3.- Using the appadmin export the data to a .CSV (db_colors.csv) file
#and put it in the private folder of your app.
#4.- Do the same thing you are doing except for:
#
#db.color.import_from_csv_file(
#   open(os.path.join(request.folder, os.path.join('private',
#'db_colors.csv')), 'r')
#)
