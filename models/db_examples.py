#
# some test data structures for the examples controller
#

import uuid # this is needed for the creation of an uuid
from gluon import *

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

#if not db(db.examples_pbase.id).count()<10:
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

# from book
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
