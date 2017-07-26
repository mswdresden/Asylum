#
# some test data structures for the examples controller
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
