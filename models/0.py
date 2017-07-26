# msw:
# The 'welcome' scaffolding app has no default configuration file, as everything seems to have a
# default value. in order to add own things or change others, this file is introduced.
# as the models in this folder are (most probably) read in alphabetical order, this file
# is read pretty much at the start.
#
# we also need adjustments in the db.py file later, if we like to pass info from this file into
# db.py (e.g. mail.settings.server = settings.email_server).
# after doing this, the 'configuration' can be done using only this file and not touching db.py again
#

from gluon.storage import Storage
settings = Storage()
settings.production = False
if settings.production:
    settings.db_uri = 'sqlite://production.sqlite'
    settings.migrate = False
else:
    settings.db_uri = 'sqlite://development.sqlite'
    settings.migrate = True

#settings.title = request.application
settings.title = 'MSW ist so krass'
settings.subtitle = '... mach mich besser!'

#settings.author = 'you'
#settings.author_email = 'you@example.come'
#settings.keywords = ''
#settings.description = ''
#settings.layout_theme = 'Default'
#settings.security_key = 'a098c897-724b-4e05-b2d8-8ee993385ae6'
#settings.email_server = 'localhost'
#settings.email_sender = 'you@example.com'
#settings.email_login = ''
#settings.login_method = 'local'
#settings.login_config = ''
