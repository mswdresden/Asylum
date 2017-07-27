#Tables are defined in the DAL via define_table:
#	>>> db.define_table('person',
#                    Field('name'),
#                    id=id,
#                    rname=None,
#                    redefine=True
#                    common_filter,
#                    fake_migrate,
#                    fields,
#                    format,
#                    migrate,
#                    on_define,
#                    plural,
#                    polymodel,
#                    primarykey,
#                    redefine,
#                    sequence_name,
#                    singular,
#                    table_class,
#                    trigger_name)
#
#
#- These are the default values of a Field constructor:
#
#	Field(fieldname,
# type='string',
# length=None,
# default=None,
# required=False,
# requires='<default>',
# ondelete='CASCADE',
# notnull=False,
# unique=False,
# uploadfield=True,
# widget=None,
# label=None,
# comment=None,
# writable=True,
# readable=True,
# update=None,
# authorize=None,
# autodelete=False,
# represent=None,
# compute=None,
# uploadfolder=None,
# uploadseparate=None,
# uploadfs=None,
# rname=None)
#
#  	To avoid unwanted migrations on upgrades, we recommend that you always specify the length for string, password and upload fields.
#  	=> Field('', type=string, label=T(''), comment=T(''), length=512, requires=None, ...)
#	   and: writeable, readable
#
# see detailed info in the book:
#  http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#Table-constructor

import uuid # this is needed for the creation of an uuid

# does this help in case of a broken/stuck database?
#from gluon import IS_NOT_EMPTY
from gluon import *
#from gluon import auth

k_redefine = True

# define lists for dropdown menues
asylum_citizenship = [T('Germany'),T('EU'),T('Albania'),T('Turkey'),T('Syria'),T('Irak'),
    T('Iran'),T('GUS'),T('Afganistan'),T('Lybia'),T('Africa (other)'),T('Europe (other)'),T('Asia (other'),
    T('Middel East'),T('America'),T('other')]

asylum_familyreunion = [
        T('possibility 1'),T('possibility 2'),T('possibility 3'),T('possibility 4'),T('possibility 5'),
]

# possible accomodations
db.define_table('asylum_accommodation',
                Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
                Field('name', type='string', length=50, label=T('Name'), comment=T('A short description of the location')),
                Field('postaddress', type='string', length=512, requires=IS_NOT_EMPTY(), label=T('Address'), comment=T('Street, Number, ZIP, City'
                                                                                                                       )),
                Field('landlord', type='string', length=512, label=T('Owner'), comment=T('The owner of this housing facility')),
                auth.signature,
                format='%(postaddress)s',
                redefine=k_redefine,)


# ------------------
db.define_table('asylum_address',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),

    Field('street', type='string', length=200, requires=IS_NOT_EMPTY(),
          label=T('Street'), comment=T('The street name of the appartment')),

    Field('housenumber', type='integer', requires=IS_INT_IN_RANGE(0, 100, error_message='too small or too large!'),
          label=T('Number'), comment=T('The number of the house')),
    Field('numberadd', default="",
          label=T("Additional Info"), comment=T('additional info (e.g. backside, only during daytime, ...)')),
    Field('zip',  type='integer', requires=IS_NOT_EMPTY(), label=T('ZIP'), comment=T('ZIP of the appartment')),
    Field('city', length=100, requires=IS_NOT_EMPTY(), label=T('City'), comment=T('Name of City')),
    Field('mobile', type='integer', label=T('Mobile'), comment=T('Mobile Number (this is an int!)')),

    auth.signature,
    format='%(street)s',
    redefine=k_redefine,
    )


# --------------------
db.define_table('asylum_checklist',
    Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),
    Field('name', type='string',requires=IS_NOT_EMPTY(),
          label='Last Name', comment='A last name for testing'),

    Field('moveindate', type='date', requires=IS_EMPTY_OR(IS_DATE()),
          label=T('Move-In Date'), comment=T('The date the person moved into the current accommodation')),
    Field('dezi', type='boolean',
          label=T('Dezi Appartment'), comment=T('Is this a dezi-appartment')),
    Field('mailbox_labeled', type='boolean', requires=IS_NOT_EMPTY(),
          label=T('Mailbox Labeled'), comment=T('Is there a name label on the mailbox?')),
    Field('appkey',  type='integer', requires=IS_IN_SET([0,1,2,3,4,5]), label=T('Number of Keys'), comment=T('Total number of keys the person posesses (for this appartment)')),
    Field('mailkey', type='integer', requires=IS_IN_SET([0,1,2,3,4,5]), label=T('Number of Mailbox Keys'),
                      comment=T('Total number of mailbox keys the person posesses (for this appartment)')),

    Field('bail', type='double', requires=IS_INT_IN_RANGE(0, 100, error_message=T('too small or too large!')),
          label=T('Bail for key(s)'), comment=T('The total bail for all the keys')),
    Field('heatingok', type='string', requires=IS_IN_SET(['ok','defunct','not known']), default='not known',
          label=T('Heating OK'), comment=T('Is the heating of the appartment ok?')),
    Field('bamfaddress', 'reference asylum_address', requires=IS_IN_DB(db,'asylum_address.name', '%(name)s'),
          label=T('Address for BAMF'), comment=T('The address the BAMF uses for communication')),
    auth.signature,
    #format='%(postaddress)s',
    redefine=k_redefine,
                )


# the basic information of an asylum person
db.define_table('asylum_pbase',
                Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),
                #Field('modified_on', 'datetime', default=request.now),
                Field('name', type='string', length=35,requires=IS_NOT_EMPTY(), comment=T('The family name (as written in the passport)')),
                Field('firstname', type='string', length=50,requires=IS_NOT_EMPTY(), label=T('First Name'), comment=T('first and middle names')),
                Field('birthday', type='date', label=T('Date of Birth'), comment=T('The (official) date of birh')),
                Field('arrivaldate', type='date', label=T('Date of Arrival'),  comment=T('Date of first registration in Germany')),
                Field('residentstatus',type='string', length=512, label=T('Residental Status'), comment=T('Current Status (you can give comments)')),
                Field('healthinsurance',type='string', length=512,
                      requires=IS_IN_DB(db,'asylum_healthinsurance.name', '%(name)s'),
                      label=T('Health Insurance'), comment=T('')),
                Field('bamfid', type='string', length=15, label=T('BAMF ID'), comment=T('The BAMF identification number')),
                Field('bankiban',type='string', length=22, label=T('IBAN'), comment=T('IBAN Number: e.g. DE 10 0233 1111 ...')), # check for IBAN
                Field('accommodation',  type='string',
                        requires = IS_IN_DB(db, 'asylum_accommodation.postaddress','%(postaddress)s', zero=T('choose one')),
                        label=T('Accommodation'),comment=T('')),
                Field('citizenship', requires=IS_IN_SET(asylum_citizenship),
                        label=T('Citizenship'), comment=T('The official citizenship')),
                Field('familyreunion', requires=IS_IN_SET(asylum_familyreunion),
                        label=T('Family Reunion'), comment=T('Status of possible family reunion')),
                Field('checklist','reference asylum_checklist',
                      requires = IS_IN_DB(db, db.asylum_checklist.uuid, '%(uuid)s'),
                      label='Checklist',comment="the checklist of this person"),

                auth.signature,
                format='%(name)s',
                redefine=k_redefine,
                )

    #db.asylum_pbase.healthinsurance.represent = lambda value, row: A('get it', _href=URL('download', args=value))

## possible housing (probably broken through messing up field names)
#db.define_table('asylum_housing',
#                Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
#                Field('name', type='string', length=50, label=T('Name'), comment=T('A short description of the location')),
#                Field('postaddress', type='string', length=512, requires=IS_NOT_EMPTY(), label=T('Address'), comment=T('Street, Number, ZIP, City'
#                                                                                                                      )),
#                Field('landlord', type='string', length=512, label=T('Owner'), comment=T('The owner of this housing facility')),
#auth.signature,
#                format='%(address)s',
#)



# possible health insurances
db.define_table('asylum_healthinsurance',
                Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),
                Field('name', type='string', length=50, requires=IS_NOT_EMPTY(), label=T('Name') ),
                Field('address', type='string', length=512, label=T('Address'), comment=T('Adress: Street, Number, ZIP and City')),

                auth.signature,
                format='%(address)s',
                redefine = k_redefine,)



# -------------------
db.define_table('asylum_edu',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('bildungsagentur', type='boolean', label=T('Education Agency'), comment=T('')),
    Field('profession', type='string', length=30, label=T('Profession'), comment=T('The profession learned')),
    Field('germanlang', requires=IS_IN_SET(['00','A1','A2','B1','B2','C',T('not known')]),
          label=T('German Language'), comment=T('The language skills')),
    Field('education', requires=IS_IN_SET([
        T('none'),T('elementary'),T('secondary'),T('hight school'),T('university'),T('phd'),T('professor')
    ]), label=T('Formal education'), comment=T('Highest level of formal education')),
    Field('certificates', type='boolean',
          label=T('Certificates'), comment=T('Are all certificates (school, university) present?')),
    Field('languages', requires=IS_IN_SET(
        [T('English'),T('French'),T('German'),T('Arabic (standard)'),T('Arabic (local)'),
                              T('Russian'),T('Farsi'), T('Dutch'),T('Italian'), T('Bantu'),T('Chinese'),], multiple=True),
         label=T('Languages'), comment=T('The Languages spoken (min. at basic level)')),
                auth.signature,
    # format='%(name)s',
    redefine=k_redefine,
    )
# ------------------
db.define_table('asylum_socialwellfare',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('wbsapplication', type='boolean', label=T('WBS Application'), comment=T('Has an application for an WBS been done?')),
    Field('wbsdate', type='date', label=T('WBS date'), comment=T('Date when the WBS was approved')),
    Field('chonicillness', type='text', length=512,
          label=T('Chronic Illness'), comment=T('A description of chronic illnesses')),
    Field('aufenthaltsgestattung', requires=IS_IN_SET([T('Possibility 1'),T('Moeglichkeit 2'),T('hier fehlt Text'),T('huhuhu'),T('lalala'),]),
                                    label=T('Aufenthaltsgestattung'), comment=T('please give an explanation')),
    Field('passdeduction', type='integer', requires=IS_INT_IN_RANGE(0, 999),
          label=T('Reisepassgebührenermäßigung'), comment=T('Reisepassgebührenermäßigung in Euro')),
    #Field('', type='', length=, requires=, label=T(''), comment=T('')),
    auth.signature,
    # format='%(name)s',
    redefine=k_redefine,
    )

# ------------------
# skelleton
#db.define_table('asylum_',
#    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
#    Field('', type='', length=, requires=, label=T(''), comment=T('')),
#    auth.signature,
#    # format='%(name)s',
#    redefine=k_redefine,
#    )