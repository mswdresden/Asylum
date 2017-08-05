
import uuid # this is needed for the creation of an uuid

# does this help in case of a broken/stuck database?
#from gluon import IS_NOT_EMPTY
from gluon import *

from customvalidators import IS_IBAN_CUSTOM


####################################################################
# define some simple data-sets (e.g. for dropdown items in fields) #
# define helping tables                                            #
####################################################################

# simple lists
asylum_citizenship = [T('Germany'),T('EU'),T('Albania'),T('Turkey'),T('Syria'),T('Irak'),
    T('Iran'),T('GUS'),T('Afganistan'),T('Lybia'),T('Africa (other)'),T('Europe (other)'),T('Asia (other'),
    T('Middel East'),T('America'),T('other')]

asylum_familyreunion = [
        T('possibility 1'),T('possibility 2'),T('possibility 3'),T('possibility 4'),T('possibility 5'),
]

# simple tables

# possible health insurances
db.define_table('asyl_healthinsurance',
    Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),
    Field('name', type='string', length=50, requires=IS_NOT_EMPTY(), label=T('Name') ),
    Field('address', type='string', length=512, label=T('Address'), comment=T('Adress: Street, Number, ZIP and City')),

    auth.signature,
    format='%(name)s',
    )




################################################################
# define the tables, include some logic via validators/lambdas #
################################################################

# the basic information of an asylum person
db.define_table('asyl_pbase',
                Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),

                Field('name', type='string', length=35,requires=IS_NOT_EMPTY(), comment=T('The family name (as written in the passport)')),
                Field('firstname', type='string', length=50,requires=IS_NOT_EMPTY(), label=T('First Name'), comment=T('first and middle names')),
                Field('identno', type='string',  # unique=True, <<== fix this! (probably need to make a new table)
                      requires=[IS_NOT_EMPTY()]),  # IS_NOT_IN_DB(db, 'db.asyl_pbase')]), <<== and this
                Field('internalname', type='string', compute=lambda r: str(r['firstname'] +' ' + r['name'] +',  ' + r['internalname'] )),
                Field('birthday', type='date', label=T('Date of Birth'), comment=T('The date of birh')),
                Field('arrivaldate', type='date', label=T('Date of Arrival'),  comment=T('Date of first registration in Germany')),
                Field('residentstatus',type='string', length=512, label=T('Residental Status'), comment=T('Current Status (you can give comments)')),
                Field('healthinsurance',type='string', length=512,
                      requires=IS_IN_DB(db,'asylum_healthinsurance.name', '%(name)s'),
                      label=T('Health Insurance'), comment=T('')),
                Field('bamfid', type='string', length=15, label=T('BAMF ID'), comment=T('The BAMF identification number')),
                Field('bankiban',type='string', requires=IS_EMPTY_OR(IS_IBAN_CUSTOM()),
                      label=T('IBAN'), comment=T('IBAN Number: e.g. DE29100500001061045672')),  # check for IBAN
                Field('zab',type='integer', requires=IS_INT_IN_RANGE(0,999999)),

                auth.signature,
                format='%(name)s',
                )
# make the id a hidden field
#db.asyl_pbase.id.writable = False
#db.asyl_pbase.id.readable = False
#db.asyl_pbase.internalname.readable = True
#db.asyl_pbase.internalname.writeable = True
#db.asyl_pbase.identno.writeable = False

# --------------------
db.define_table('asyl_checklist',
    Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),

    Field('name', type='string', length=35, default=T('will be filled automatically'),
            comment=T('The family name (as written in the passport)')),
    Field('firstname', type='string', length=50,  default=T('will be filled automatically'), label=T('First Name'),
            comment=T('first and middle names')),
    Field('internalname',  default=T('will be filled automatically')),

    Field('moveindate', type='date', requires=IS_EMPTY_OR(IS_DATE()),
          label=T('Move-In Date'), comment=T('The date the person moved into the current accommodation')),
    Field('dezi', type='boolean'),
    #Field('pbase','reference asyl_pbase', requires=IS_IN_DB(db,db.asyl_pbase.id,'%(name)s',)),
    Field('pbase_id','reference asyl_pbase', requires=IS_IN_DB(db,db.asyl_pbase.id,'%(name)s',)),
    auth.signature,
    format='%(name)s',
    )



# ------------------
db.define_table('asyl_address',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),
    Field('internalname',  default=T('will be filled automatically')),

    Field('street', type='string', length=200, requires=IS_NOT_EMPTY(),
          label=T('Street'), comment=T('The street name of the appartment')),

    Field('housenumber', type='integer', requires=IS_INT_IN_RANGE(0, 999, error_message='too small or too large!'),
          label=T('Number'), comment=T('The number of the house')),
    Field('numberadd', default="",
          label=T("Additional Info"), comment=T('additional info (e.g. backside, only during daytime, ...)')),
    Field('zip',  type='integer', requires=IS_NOT_EMPTY(), label=T('ZIP'), comment=T('ZIP of the appartment')),
    Field('city', length=100, requires=IS_NOT_EMPTY(), label=T('City'), comment=T('Name of City')),
    Field('mobile', type='integer', label=T('Mobile'), comment=T('Mobile Number (this is an int!)')),
    #Field('pbase','reference asyl_pbase', requires=IS_IN_DB(db,db.asyl_pbase.id,'%(name)s',)),
    Field('pbase_id','reference asyl_pbase', requires=IS_IN_DB(db,db.asyl_pbase.id,'%(name)s',)),
    auth.signature,
    format='%(name)s',
    )
