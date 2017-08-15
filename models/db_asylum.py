
import uuid # this is needed for the creation of an uuid

# does this help in case of a broken/stuck database?
#from gluon import IS_NOT_EMPTY
from gluon import *

from customvalidators import IS_IBAN_CUSTOM


msw_dev = 0

####################################################################
# define some simple data-sets (e.g. for dropdown items in fields) #
# define helping tables                                            #
####################################################################

# simple lists (no databese needed, however, admin must edit this file to change things)
asylum_citizenship = [T('Germany'),T('EU'),T('Albania'),T('Turkey'),T('Syria'),T('Irak'),
    T('Iran'),T('GUS'),T('Afganistan'),T('Lybia'),T('Africa (other)'),T('Europe (other)'),T('Asia (other'),
    T('Middel East'),T('America'),T('other')]

asylum_familyreunion = [
        T('possibility 1'),T('possibility 2'),T('possibility 3'),T('possibility 4'),T('possibility 5'),
]

asylum_heatingok= ['ok','defunct','not known']
asylum_langlevels = ['00','A1','A2','B1','B2','C',T('not known')]
asylum_edulevels=[
        T('none'),T('elementary'),T('secondary'),T('hight school'),T('university'),T('phd'),T('professor')]

asylum_ynu = [T('Yes'),T('No'),T('unknown')]

asylum_posslanguages = [ (0, T('English')),
                    ( 1,T('French')),
                    ( 2,T('German')),
                    ( 3,T('Arabic (standard)')),
                    ( 4,T('Arabic (local)')),
                    ( 5,T('Russian')),
                    ( 6,T('Farsi')),
                    ( 7,T('Dutch')),
                    ( 8,T('Italian')),
                    ( 9,T('Bantu')),
                    (10,T('Chinese')),
                         ]

asylum_aufenthaltsgestattung = [T('Possibility 1'), T('Moeglichkeit 2'),
                                T('hier fehlt Text'), T('huhuhu'), T('lalala'), ]


##################
#  simple tables #
##################
# possible health insurances
db.define_table('asylum_healthinsurance',
    Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),
    Field('name', type='string', length=50, requires=IS_NOT_EMPTY(), label=T('Name') ),
    Field('address', type='string', length=512, label=T('Address'), comment=T('Adress: Street, Number, ZIP and City')),

    auth.signature,
    format='%(name)s',
    )

# addresses of appartments
db.define_table('asylum_accommodation',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),

    Field('street', requires=IS_NOT_EMPTY()),
    Field('housenumber', requires=IS_NOT_EMPTY()),
    Field('appcode', label=T('Appartment Code'),
          comment=T("Appartment name/number/code, e.g. 'OG-links', 'Room 602', '3.OG, rechts")),

    Field('zip', label=T('Zip Code'), comment=T('Zip Code')),
    Field('city', label=T('City'), comment=T('City')),


    auth.signature,
    format = '%(street)s %(housenumber)s %(appcode)s, %(zip)s %(city)s',
    )





################################################################
# define the tables, include some logic via validators/lambdas #
################################################################

# the basic information of an asylum person
db.define_table('asylum_pbase',
                Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),

                Field('name', type='string', length=35,requires=IS_NOT_EMPTY(), comment=T('The family name (as written in the passport)')),
                Field('firstname', type='string', length=50,requires=IS_NOT_EMPTY(), label=T('First Name'), comment=T('first and middle names')),
                Field('identno', type='string',  # unique=True, <<== fix this! (probably need to make a new table)
                      requires=[IS_NOT_EMPTY()]),  # IS_NOT_IN_DB(db, 'db.asylum_pbase')]), <<== and this
                #Field('internalname', type='string', compute=lambda r: str(r['firstname'] +' ' + r['name'] +',  ' + r['identno'] )),
                Field('internalname', type='string', default='will be filled automatically' ),

                Field('birthday', type='date',
                      label=T('Date of Birth'), comment=T('The date of birh')),
                Field('arrivaldate', type='date',
                      label=T('Date of Arrival'),  comment=T('Date of first registration in Germany')),
                Field('citizenship', requires=IS_IN_SET(asylum_citizenship),
                    label=T('Citizenship'), comment=T('Citizenship of this person')),
                Field('residentstatus',type='string', length=512,
                      label=T('Residental Status'), comment=T('Current Status (you can give comments)')),
                Field('healthinsurance',type='string', length=512,
                      requires=IS_IN_DB(db,'asylum_healthinsurance.name', '%(name)s'),
                      label=T('Health Insurance'), comment=T('Healtinsurance of this person (e.g. AOK, IKK, ...')),
                Field('bamfid', type='string', length=15,
                      label=T('BAMF ID'), comment=T('The BAMF identification number')),
                Field('bankiban',type='string', requires=IS_EMPTY_OR(IS_IBAN_CUSTOM()),
                      label=T('IBAN'), comment=T('IBAN Number: e.g. DE29100500001061045672')),  # check for IBAN
                Field('familyreunion', requires=IS_IN_SET(asylum_familyreunion),
                      label=T('Staus of familyreunion'), comment=T('Staus of familyreunion')),
                Field('zab',type='integer', requires=IS_INT_IN_RANGE(0,999999)),

                auth.signature,
                format='%(name)s',
                )
# make the id a hidden field
db.asylum_pbase.id.writable = False
#db.asylum_pbase.id.readable = False
db.asylum_pbase.internalname.readable = False
db.asylum_pbase.internalname.writeable = False

# --------------------
db.define_table('asylum_checklist',
    Field('uuid', length=64, default=lambda:str(uuid.uuid4()),writable=False, readable=False),

    Field('name', type='string', length=35, requires=IS_NOT_EMPTY(),default=T('will be filled automatically')),
    Field('firstname', type='string', length=50,  default=T('will be filled automatically'),
          label=T('First Name'), comment=T('first and middle names')),
    Field('identno', type='string', #unique=True,
          requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'asylum_checklist.identno')] ),
    Field('internalname',  default=T('will be filled automatically')),

    Field('moveindate', type='date', requires=IS_EMPTY_OR(IS_DATE()),
          label=T('Move-In Date'), comment=T('The date the person moved into the current accommodation')),
    Field('dezi', type='boolean'),

    Field('mailbox_labeled', type='boolean',
          label=T('Mailbox Labeled'), comment=T('Is there a name label on the mailbox?')),
    Field('appkey',  type='integer', requires=IS_IN_SET([0,1,2,3,4,5]),
          label=T('Number of Keys'), comment=T('Total number of keys the person posesses (for this appartment)')),
    Field('mailkey', type='integer', requires=IS_IN_SET([0,1,2,3,4,5]),
          label=T('Number of Mailbox Keys'),
                      comment=T('Total number of mailbox keys the person posesses (for this appartment)')),

    Field('bail', type='double', default=0, requires=IS_INT_IN_RANGE(0, 100, error_message=T('Number too small or too large!')),
          label=T('Bail for key(s)'), comment=T('The total bail for all the keys')),
    Field('heatingok', type='string', requires=IS_IN_SET(asylum_heatingok), default=asylum_heatingok[2],
          label=T('Heating OK'), comment=T('Is the heating of the appartment ok?')),
    Field('bamfaddress', 'reference asylum_accommodation',
          requires=IS_IN_DB(db,db.asylum_accommodation.id, '%(street)s %(housenumber)s %(appcode)s, %(zip)s %(city)s'),
          label=T('Address for BAMF'), comment=T('The address the BAMF uses for communication')),


    Field('pbase_id','reference asylum_pbase', requires=IS_IN_DB(db,db.asylum_pbase.id,'%(name)s',)),
    auth.signature,
    format='%(name)s',
    )

if msw_dev ==0:
    db.asylum_checklist.id.writable = False
    db.asylum_checklist.id.readable = False
    db.asylum_checklist.name.writable = False
    db.asylum_checklist.name.readable = False
    db.asylum_checklist.firstname.writable = False
    db.asylum_checklist.firstname.readable = False
    db.asylum_checklist.identno.writable = False
    db.asylum_checklist.identno.readable = False
    db.asylum_checklist.internalname.writable = False
    db.asylum_checklist.internalname.readable = False
    db.asylum_checklist.pbase_id.readable = False
    db.asylum_checklist.pbase_id.writable = False

# ------------------
db.define_table('asylum_address',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),

    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),
    Field('firstname', type='string', length=50, default=T('will be filled automatically'),
                label=T('First Name'), comment=T('first and middle names')),
    Field('identno', type='string',   unique=True,
                      requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'asylum_checklist.identno')]),
    Field('internalname',  default=T('will be filled automatically')),


    Field('showstanndard', type='boolean', default='off', label=T('Is this a Standard-Accommodation?')),

    Field('standardaccommodation', 'reference asylum_accommodation',
          requires=IS_IN_DB(db,db.asylum_accommodation.id, '%(street)s %(housenumber)s (%(appcode)s), %(zip)s %(city)s'),
          label=T('Address of Person'), comment=T('The official address of this person')),

    Field('street', type='string', length=200,
          label=T('Street'), comment=T('The street name of the appartment')),
    Field('housenumber', type='integer',
          requires=IS_EMPTY_OR(IS_INT_IN_RANGE(1, 9999, error_message=T('House number not in range 1-9999!'))),
          label=T('Number'), comment=T('The number of the house')),
    Field('numberadd', default="",
          label=T("Additional Info"), comment=T('additional info (e.g. backside, only during daytime, ...)')),
    Field('zip',  type='string', label=T('ZIP'), comment=T('ZIP of the appartment')),
    Field('city', length=100, label=T('City'), comment=T('Name of City')),
    Field('mobile', type='string', label=T('Mobile'), comment=T('Mobile Number(s)')),
    Field('email', requires = IS_EMAIL(error_message=T('invalid email!')),
          label=T('EMail'), comment=T('The EMail address of the person')),

    Field('pbase_id','reference asylum_pbase', requires=IS_IN_DB(db,db.asylum_pbase.id,'%(name)s',)),
    auth.signature,
    format='%(name)s',
    )

if msw_dev == 0:
    db.asylum_address.id.writable = False
    db.asylum_address.id.readable = False
    db.asylum_address.name.writable = False
    db.asylum_address.name.readable = False
    db.asylum_address.firstname.writable = False
    db.asylum_address.firstname.readable = False
    db.asylum_address.identno.writable = False
    db.asylum_address.identno.readable = False
    db.asylum_address.internalname.writable = False
    db.asylum_address.internalname.readable = False
    db.asylum_address.pbase_id.writable = False
    db.asylum_address.pbase_id.readable = False

# ------------------
db.define_table('asylum_edu',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),
    Field('firstname', type='string', length=50, default=T('will be filled automatically'),
                label=T('First Name'), comment=T('first and middle names')),
    Field('identno', type='string',  unique=True,
                      requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'asylum_edu.identno')]), # edit here
    Field('internalname',  default=T('will be filled automatically')),

    Field('bildungsagentur', requires=IS_IN_SET(asylum_ynu),# default='unknown',
            label=T('Education Agency'), comment=T('Is this person registerd at the Bildungsagentur')),
    Field('profession', type='string', length=30, label=T('Profession'), comment=T('The profession learned')),
    Field('germanlang', requires=IS_IN_SET(asylum_langlevels),
            label=T('German Language'), comment=T('The language skills')),
    Field('education', requires=IS_IN_SET(asylum_edulevels), default=T('unknown'),
            label=T('Formal education'), comment=T('Highest level of formal education')),
    Field('certificates', requires=IS_IN_SET(asylum_edulevels), default=T('unknown'),
            label=T('Certificates'), comment=T('Are all certificates (school, university) present?')),

    # try this later: https://books.google.de/books?id=cwjpG47z_7IC&pg=PT334&lpg=PT334&dq=web2py+multiselect+plugin&source=bl&ots=pzk7oHy8Np&sig=JH7Jc-OViERIn_mz5CE6ZaEkdG0&hl=en&sa=X&ved=0ahUKEwjRiNaEhsXVAhVMZVAKHS1NDloQ6AEIVjAI#v=onepage&q=web2py%20multiselect%20plugin&f=false
    #Field('languages', type='list:string', requires=IS_IN_SET(['en','de','es','ar'],multiple=True),
    #     label=T('Languages'), comment=T('The Languages spoken')),
    Field('languages', type='list:string', requires=IS_IN_SET(asylum_posslanguages, multiple=True),
            label=T('Languages'), comment=T('The Languages spoken')),

    Field('pbase_id', 'reference asylum_pbase', requires=IS_IN_DB(db, db.asylum_pbase.id, '%(name)s', )),
    auth.signature,
    format='%(name)s',
    )

if msw_dev == 0:
    db.asylum_edu.id.writable = False
    db.asylum_edu.id.readable = False
    db.asylum_edu.name.writable = False
    db.asylum_edu.name.readable = False
    db.asylum_edu.firstname.writable = False
    db.asylum_edu.firstname.readable = False
    db.asylum_edu.identno.writable = False
    db.asylum_edu.identno.readable = False
    db.asylum_edu.internalname.writable = False
    db.asylum_edu.internalname.readable = False
    db.asylum_edu.pbase_id.writable = False
    db.asylum_edu.pbase_id.readable = False

# ------------------
db.define_table('asylum_socialwellfare',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),
    Field('firstname', type='string', length=50, default=T('will be filled automatically'),
                label=T('First Name'), comment=T('first and middle names')),
    Field('identno', type='string',  unique=True,
                      requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'asylum_socialwellfare.identno')]), # edit here
    Field('internalname',  default=T('will be filled automatically')),


    Field('wbsapplication', requires=IS_IN_SET([T('Yes'),T('No'),T('unknown')]), default=T('unknown'),
          label=T('WBS Application'), comment=T('Has an application for an WBS been done?')),
    Field('wbsdate', type='date',
          label=T('WBS date'), comment=T('Date when the WBS was approved')),
    Field('chonicillness', type='text', length=512,
                      label=T('Chronic Illness'), comment=T('A description of chronic illnesses')),
    Field('aufenthaltsgestattung', requires=IS_IN_SET(asylum_aufenthaltsgestattung),
                      label=T('Aufenthaltsgestattung'), comment=T('please give an explanation')),
    Field('passdeduction', type='integer', requires=IS_INT_IN_RANGE(0, 999),
                      label=T('Reisepassgebührenermäßigung'), comment=T('Reisepassgebührenermäßigung in Euro')),
    # Field('', type='', length=, requires=, label=T(''), comment=T('')),


    Field('pbase_id', 'reference asylum_pbase', requires=IS_IN_DB(db, db.asylum_pbase.id, '%(name)s', )),
    auth.signature,
    format='%(name)s',
    )

if msw_dev == 0:
    db.asylum_socialwellfare.id.writable = False
    db.asylum_socialwellfare.id.readable = False
    db.asylum_socialwellfare.name.writable = False
    db.asylum_socialwellfare.name.readable = False
    db.asylum_socialwellfare.firstname.writable = False
    db.asylum_socialwellfare.firstname.readable = False
    db.asylum_socialwellfare.identno.writable = False
    db.asylum_socialwellfare.identno.readable = False
    db.asylum_socialwellfare.internalname.writable = False
    db.asylum_socialwellfare.internalname.readable = False
    db.asylum_socialwellfare.pbase_id.writable = False
    db.asylum_socialwellfare.pbase_id.readable = False

# ------------------
db.define_table('asylum_mobility',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),

    Field('name', default=T('will be filled automatically')),
    Field('firstname', default=T('will be filled automatically')),
    Field('identno', default=T('will be filled automatically')),
    Field('internalname',  default=T('will be filled automatically')),

    Field('dvbaboticket', requires=IS_IN_SET(asylum_ynu), default=T('unknown'),
          label=T('DVB Abo-Ticket'), comment=T('Does this person have a DVB ticket (abo)')),
    Field('dvbexpires', type='date',
          label=T('DVB-ticket expire date'), comment=T('Date when the abo-ticket will expire')),
    #Field('',
    #      label=T(''), comment=T('')),

                Field('pbase_id', 'reference asylum_pbase', requires=IS_IN_DB(db, db.asylum_pbase.id, '%(name)s', )),
    auth.signature,
    format='%(name)s',
    )

if msw_dev == 0:
    db.asylum_mobility.id.writable = False
    db.asylum_mobility.id.readable = False
    db.asylum_mobility.name.writable = False
    db.asylum_mobility.name.readable = False
    db.asylum_mobility.firstname.writable = False
    db.asylum_mobility.firstname.readable = False
    db.asylum_mobility.identno.writable = False
    db.asylum_mobility.identno.readable = False
    db.asylum_mobility.internalname.writable = False
    db.asylum_mobility.internalname.readable = False
    db.asylum_mobility.pbase_id.writable = False
    db.asylum_mobility.pbase_id.readable = False

# ------------------
db.define_table('asylum_child',
    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),

    Field('name', default=T('will be filled automatically')),
    Field('firstname', default=T('will be filled automatically')),
    Field('identno', default=T('will be filled automatically')),
    Field('internalname',  default=T('will be filled automatically')),


    Field('childname', requires=IS_NOT_EMPTY(),
          label=T('Name of child'), comment=T('First (and last) name of child')),

    Field('childbirth', requires=IS_NOT_EMPTY(),
          label=T('Birthday'), type='date', comment=T('Birthday')),

    Field('childschoolreg', type='boolean', default=False,
          label=T('Schoolregistration'), comment=T('Schoolregistration')),

    Field('childkindergarden', requires=IS_IN_SET(asylum_ynu), default=T('unknown'),
          label=T('Kindergarden'), comment=T('Kindergarden')),

    Field('childfeefreekg', type='boolean', default=False,
          label=T('Kindergarden without payment'), comment=T('Kindergarden without payment')),

    Field('childfeefreemeal', requires=IS_IN_SET(asylum_ynu), default=T('unknown'),
          label=T('Food without payment'), comment=T('Food without payment')),

    Field('childbildungsagentur', requires=IS_IN_SET(asylum_ynu), default=T('unknown'),
          label=T('Bildungsagentur'), comment=T('Bildungsagentur')),


    Field('pbase_id', 'reference asylum_pbase', requires=IS_IN_DB(db, db.asylum_pbase.id, '%(name)s', )),
    auth.signature,
    format='%(name)s',
    )

if msw_dev == 0:
    db.asylum_child.id.writable = False
    db.asylum_child.id.readable = False
    db.asylum_child.name.writable = False
    db.asylum_child.name.readable = False
    db.asylum_child.firstname.writable = False
    db.asylum_child.firstname.readable = False
    db.asylum_child.identno.writable = False
    db.asylum_child.identno.readable = False
    db.asylum_child.internalname.writable = False
    db.asylum_child.internalname.readable = False
    db.asylum_child.pbase_id.writable = False
    db.asylum_child.pbase_id.readable = False


## ------------------
#db.define_table('asylum_',
#    Field('uuid', length=64, default=lambda: str(uuid.uuid4()), writable=False, readable=False),
#    Field('name', type='string', length=100, requires=IS_NOT_EMPTY(), label=T('Name'), comment=T('A short description of the location')),
#    Field('firstname', type='string', length=50, default=T('will be filled automatically'),
#                label=T('First Name'), comment=T('first and middle names')),
#    Field('identno', type='string',  unique=True,
#                      requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'asylum_.identno')]), # edit here
#    Field('internalname',  default=T('will be filled automatically')),
#
#    Field('', type='', requires=IS_NOT_EMPTY(),
#          label=T(''), comment=T('')),
#
#    # add fields
#
#    auth.signature,
#    format='%(name)s',
#    )
#
#if msw_dev == 0:
#   db.asylum_.id.writable = False
#   db.asylum_.id.readable = False
#   db.asylum_.name.writable = False
#   db.asylum_.name.readable = False
#   db.asylum_.firstname.writable = False
#   db.asylum_.firstname.readable = False
#   db.asylum_.identno.writable = False
#   db.asylum_.identno.readable = False
#   db.asylum_.internalname.writable = False
#   db.asylum_.internalname.readable = False
#   db.asylum_.pbase_id.writable = False
#   db.asylum_.pbase_id.readable = False


