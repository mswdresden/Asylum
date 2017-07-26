db.define_table('msw_person',
                Field('name', label='Name', requires=IS_NOT_EMPTY()),
    )

db.define_table('msw_dog',
                Field('dog_owner', 'reference msw_person'),
                Field('dog', label='Dog Name', requires=IS_NOT_EMPTY()),
                )
db.msw_dog.dog_owner.requires = IS_IN_DB(db,db.msw_person.id,'%(name)s')

#
db.define_table('msw_thing',
                Field('thing_owner', 'reference msw_person'),
                Field('name', label=(T('Thing Name')), requires=IS_NOT_EMPTY()),
                )
db.msw_thing.thing_owner.requires = IS_IN_DB(db,db.msw_person.id,'%(name)s')
