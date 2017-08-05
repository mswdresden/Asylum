

# Asylum on web2py

## installation of web2py


#### 'Manual' script
These instructions work for ubuntu linux'es and the following is a merge of a installation script (sahana eden: https://raw.githubusercontent.com/nursix/sahana-setup/master/prod/debian/cherokee-postgis-install.sh) combined with my personal experience.
 

### update your system an get all needed python stuff
- Update system

	``# sudo apt-get update``

	``# sudo apt-get upgrade``

	``# sudo apt-get clean``

### Install Admin Tools
``# sudo apt-get install -y unzip psmisc mlocate telnet lrzsz vim elinks-lite rcconf htop sudo p7zip dos2unix curl`` (fails due to missing elinks-lite)

``#sudo apt-get install unzip psmisc mlocate telnet lrzsz vim  rcconf htop sudo p7zip dos2unix curl``

### Install Git
``# sudo apt-get install git-core``

``# sudo apt-get clean``

### Email
``# sudo apt-get install exim4-config exim4-daemon-light``

``sudo apt-get clean``

# Python
``sudo apt-get install libgeos-c1``

``sudo apt-get install libgeos-dev``

``sudo apt-get install python-dev``

``sudo apt-get install python-lxml python-setuptools python-dateutil python-pip``

``sudo apt-get install python-serial``

``sudo apt-get install python-imaging``

``sudo apt-get install python-matplotlib``

``sudo apt-get install python-requests``

``sudo apt-get install python-xlwt``

``sudo apt-get install build-essential``

``sudo apt-get clean``


### additional info from an installation on a different laptop (64-debian)
 **for web2py**: 
 
``apt-get install -y unzip psmisc mlocate telnet lrzsz vim elinks-lite rcconf htop sudo p7zip dos2unix curl`` or
``sudo apt-get install -y unzip psmisc mlocate telnet lrzsz vim  htop sudo p7zip dos2unix cur``

``sudo apt-get install libgeos-c1v5``

``sudo apt-get install python-lxml python-setuptools python-dateutil python-pip``

``sudo apt-get install libgeos-dev``

``sudo apt-get install python-dev``

``sudo apt-get install python-lxml python-setuptools python-dateutil python-pip``

``sudo apt-get install python-serial``

``sudo apt-get install python-imaging``

``sudo apt-get install python-matplotlib``

``sudo apt-get install python-requests``

``sudo apt-get install python-xlwt``

``sudo apt-get install build-essential``

``sudo apt-get install libodbc1``

``sudo apt-get install python-openid``

from: http://eden.sahanafoundation.org/wiki/InstallationGuidelines/Linux/Developer/Manual#InstallPythonLibraries

``sudo apt-get install python-lxml``

``sudo apt-get install python-shapely``

``sudo apt-get install python-reportlab``

``sudo apt-get install python-imaging``

``sudo apt-get install python-imaging``

``sudo apt-get install python-dateutil``

``sudo apt-get install python-xlwt``

``sudo apt-get install python-xlrd``

``sudo apt-get install python-numpy``

``sudo apt-get install python-matplotlib``

``sudo apt-get install python-setuptools``

``sudo apt-get install python-serial``

``sudo apt-get install python-tz``

``sudo apt-get install python-mysqldb``
  	
**Web2Py**

``sudo apt-get install libodbc1``

 For some reason insalled also (msw):
 
``sudo apt-get install python-openid``

### get web2py and reset it to last stable version, which is compatible with sahana-eden###
``git clone --recursive git://github.com/web2py/web2py.git``

``cd web2py/``

``git reset --hard cda35fd``

``git submodule update``

(in an older manual it read: git submodule update --init --recursive )

### get sahana-eden
cd applications

git clone git://github.com/mswdresden/eden

### run web2py (setting admin password to "pass")
python web2py.py -a pass

go to URL: http://127.0.0.1:8000/
	- you can here login to web2py interface with the password ("pass") set earlier.
	  then you can go to the admin area, check 'eden' and edit things
	  
	  however, before everything runs, you have to edit web2py/applications/eden/models/000_config.py
	  ACTION REQUIRED: The following files were copied from templates and should be edited: models/000_config.py 
	  therefore: edit line (17) to read: FINISHED_EDITING_CONFIG_FILE = True
	  
	  now editing works from within the web2py interface.
	  now also works calling eden from your browser: http://127.0.0.1:8000/eden
	  
	  'register for an account' for the first time:
	  ATTENTION: the first user registered will be the administrator
		 - give some email (any random mail works, I use a real one, however)
		 - give a admin password (as long as you work only locally, do not bother too much with complex passwords)
		 - after 'OK' you should be logged in, ... log out and test if login works
	
	It most probably is usefull to edit also settings.base.debug to match
	settings.base.debug = True
	in 000_config.py
	 

## Git #

https://github.com/mswdresden/eden # repository

### push and pull
git push https://github.com/mswdresden/eden.git

git pull [seems to work w/o https://github.com/mswdresden/eden.git]

### updating from original master? 
#http://www.flossmanuals.net/sahana-eden/installing-a-developer-environment/

### once do: git remote add upstream git://github.com/flavour/eden.git
git pull upstream master # this should do the job?!


## Links 


### web2py
- http://www.web2py.com/book # the book!
	or get the book as an application from git:
	- install gitpython and install app via admin interface: https://github.com/mdipierro/web2py-book.git
		python web2py.py --port=7000 -a pass
		http://127.0.0.1:7000/book/default/chapter/29/07/forms-and-validators
	
- web2py API documentation:	http://web2py.readthedocs.io/en/l
- http://www.web2py.com/init/default/examples
- http://www.gbv.de/dms/tib-ub-hannover/71533753x.pdf
- Field types: http://www.web2pyref.com/reference/field-type-database-field-types 
- download different bootstraps for CSS http://bootswatch.com/ 
- some simple but important DAL examples https://joecodeswell.wordpress.com/category/web2py/

Documentation of the code
- http://web2py.readthedocs.io/en/latest/dal.html

web-course (7 parts) on web2py 
- https://www.youtube.com/watch?v=bW9lpN95zwQ&index=5&list=PL5E2E223FE3777851

web2py course by Massimo (some parts, here part 2)
- https://www.youtube.com/watch?v=_4to_44DcJU

 - part1:
 	--
	--
 	-- 1:59:00 second part of app2 (blog_post with comments)
 - part2: 
 	-- up to 48:30 tour through the code (web2py files)
	-- 48:30 DAL create tables and queries
	-- 1:27:00 rebuilding a reddit application (Reddit Clone)
 - part 3:
 	-- 0:00:00 (cont) Reddit Clone
	-- 1:00.20 Template language of web2py
		--- 1:01:00 basics of view HTML ... globals, python code, loops,
			'socket timeout'=='most probably bracket missing', bracket-rules,
			response.write, define functions in views, freaking use of
			HTML in functions (loop with different font sizes), div (header, footer, content),
			layout-file, extend, include, response.flash, ajax and flash-messages,
		--- 1:15:00 tour through layout.html 
		--- 1:27:00 menue.py
		1:28:30 blocks (e.g. left side bar)
	-- 1:31:50 a new app: surverys
		--- uuid, 
		--- 1:37:30 web2py UUID!! (is this important?)
		--- 1:42:00 loop in selfsubmitting form, count, and stuff + radio_button
		--- class "well" in a radio-button	
		--- 1:53:00 represents!	
		--- 1:57:00 !!! costomize grids	
		--- 			
			
		--- 
	-- 
 - part 4:
 	-- 00:00:00 tasks in todo lists
	-- 00:08:30 record versioning
	-- 2:08:05 populating databases with example junk
 
- exporting: http://rootpy.com/Export-in-SQLFORM-grid/
 
- database tutorial: http://www.pyguy.com/web2py/web2py-one-to-many-database-tutorial/


### Sahana Eden

- https://sahanafoundation.org/        # sahana foundation main page
- http://eden.sahanafoundation.org/    # eden at sahana foundation (and wiki)
- https://github.com/sahana/eden       # sahana eden on github
- http://flossmanuals.net/sahana-eden/ # sahana book!
- http://booki.flossmanuals.net/sahana-eden/

sahana-eden google groups mailing list
- https://groups.google.com/forum/#!forum/sahana-eden

the sahana eden wiki
- http://eden.sahanafoundation.org/
- http://eden.sahanafoundation.org/wiki/TitleIndex

demo on the net:
 - http://demo.eden.sahanafoundation.org/eden/

insalling local sahana instance on suse
- https://github.com/nursix/sahana-setup/wiki/Developer-Setup#opensuse

sahana components explained
- https://github.com/nursix/sahana-setup/wiki/Components

first long sahana tutorial
- # https://www.youtube.com/watch?v=UhvlxZFnUM8

gis (maps?) is something very cool and a little different
- http://eden.sahanafoundation.org/wiki/GIS

s3 documentation
- http://pub.nursix.org/eden/s3/
- http://eden.sahanafoundation.org/wiki/S3/S3Model/SuperEntities

IRC web interface
- http://webchat.freenode.net/?channels=sahana-eden&uio=d4 



# TODO #

######################################################
# msw's howto:                                       #
######################################################
// ---------------------------
*0. Web2py version*

	from: http://write.flossmanuals.net/sahana-eden/maintenance/

	Since Sahana Eden extends Web2Py, and the two are both undergoing rapid development, 
	the revision of Web2Py can be critical. Whilst the latest 'bleeding edge' version of Web2Py is usually stable,
	some Web2Py revisions have bugs which break a part of Sahana Eden. You can try upgrading to the latest 
	revision of Web2Py or else downgrading to an older version which does not exhibit this bug.

	Sometimes a new version of Sahana Eden may use features from a more recent Web2py than the currently 
	installed version.  This typically leads to an error ticket with a message indicating that some item was 
	not found.  Update to either the latest Web2py, or the latest known-stable Web2py revision, 
	the version number for which can be found in modules/s3_update_check.py

	It is also sometimes posted in the #sahana-eden IRC channel topic (see the Community chapter for 
	connecting to IRC).
	
	
// ---------------------------
*1. Basics*
  - you need a running environment of web2py
  - you need web2py/applications/eden <= your instance of eden
  
  - in .../web2py
  	# python web2py.py -a pass
  
	- start a browser 
		- and navigate to http://localhost:8000/welcome/default/index
		- log in (password is pass)
  		- go to "my applications" 
	    - go to application -> eden
			- log in (email/password of first registered user is admin)
		
		- or directly navigate to http://localhost:8000/eden
			- log in (email/password of first registered user is admin)

		- or select	'edit' and edit eden (however, you will most probably later 
	  	  edit the files directly in an editor)
	
// ---------------------------
*1.b Start web2py python shell*
	- You can start a python shell and load the web2py modules (and models?)		  
	  # python web2py.py -S welcome -M
	  then, in order to get info on the classes/methods, you can do for example:
	  # help(db)
	  # help(session)
	  
// ---------------------------
*1.c Authentification*

	Detailed info in Chapter 9 of the web2py book.
	
	Quick intro:
		1. in your model file you need
			from gluon.tools import Auth
			... create the db object ...
			auth = Auth(db)
			auth.define_tables(username=True)
			
		2. you need in your controller	
			def user():
			 	return dict(form=auth())
				
		3. you simply controll the access to actions (in the controller) by writing 
		   above the function definition things like:
		   		@auth.requires_login()
				
	  
	  
// ---------------------------
*2. .../models/000_config.py*
		- is NOT part of git (gitignore). 
		  For changes to be committed, please also edit: modules/templates/000_config.py

		- basic setting
			- the template (choose using intuition templatenames found in modules/templates)
			- security settings must now be somewhere else!?
			- override here the settings of your template ...
			
			- for that copy modules/templates/default to modules/templates/<yourtemplate>
			  and look there in config.py which settings exist
			
			
// ---------------------------
*3. modules/templates/<yourtemplate>/config.py*
	- vast number of options you can change. either there or override values in 000_config.py (see above)
	- at the bottom there is the section where you can select/deselect the used modules
	  (can also be done in 000_config.py, it is however more nice and clean to do it in the config.py files)
	  

// ---------------------------
*4. Favicon, footer and basic layout*
	- needs to be found out!

// ---------------------------
*5. Import*
		- go to desired data (e.g. Organisation, Staff, Shelters)
		- click 'Import' in the menue
		- select 'download template' => it will be a .cvs file
		- open template in libreoffice
		    - character set: UTF-8 (unicode)
			- selector ","
			- text delimiter """
			- quoted field as text
		- edit and save file (as CSV!)
		- upload	
		
	TODO: how do the many colums in the csv file correspond to the insert-mask (which contains fewer data)?	
	TOMORROW: look here modules/templates/default/tasks.cfg
	
// ---------------------------
*6. Export*

    TODO: how to export CSV
	
	csv should be included as one of the standard export file-types 
	(http://write.flossmanuals.net/sahana-eden/data-export/).
	Unfortunately, I do not find the icon. It is, however, possible to export as XLS. 
	This opens libreoffice and you can save (*save as* - not 'Export') the file in the csv fomat 
	(komma, ", and text-filed in quotes).
	
	TODO: try to import such a file again (after changes)
	


// ---------------------------
*7. Favicon and Logo*
	- Favicon:
		- make a favicon file (.ico)
		- place this file in eden/static/favicon.ico (you may need to restart/flush-cache your browser)
		
	- Logo:	
		from: https://groups.google.com/forum/#!topic/sahana-eden/ikhl2dRqJGU%5B1-25%5D
		We prefer you to keep the 'Powered by Sahana Eden' in the footer, but 
		the main logo is often changed. 

		A full theme can be developed here: 
		http://eden.sahanafoundation.org/wiki/DeveloperGuidelines/Themes 

		or you can simply replace the file static/img/S3menu_logo.png 
		If the size is different then need to tweak the CSS too. 

		Best Wishes, 
		Fran. 

		- templates/Afropa/config.py : settings.base.theme = "Afropa"
		
		ATTENTION: changing theme is not so easy, as many settings seem to interact/interfere and
		one must find the correct settings in many files (hmmmm)
		
		
		=> or, to just change the logo (edit in templates/Afropa/config.py):
		settings.ui.menu_logo = URL(c="static", f="img", args=["afropaLogo.png"]) # msw

		
// ---------------------------
*8. Editing the homepage*
	
	The default homepage (http://127.0.0.1:8000/eden/default/index) has it's controller in
	controllers/default.py (function index()).
	
	The corresponding view is eden/views/default/index.html - so this would be the simplest way of editing this
	view file.
	
	It should according to the 'book', however, also be possible to have a custom index-file in the template/views
	directory. msw has not yet figured out how this actually works.
	
// ---------------------------
*9. Changing existing labels *
	- open the corresponding file in modules/s3db/...py
	- get tabelname, the label of the field and add at the end of modules/templates/<template_name>/config.py:

	def customise_org_organisation_controller(**attr): # the syntax seems to be "customize_<table_name>_controller"
    	table = current.s3db.org_organisation
    	table.year.label = T("Year Founded")
		[1]
	    return attr
	settings.customise_org_organisation_controller = customise_org_organisation_controller
	
	you can in addition change other things too. insert following lines above at [1] to change the
	help message.
	
	this work, however, only if you replace in config.py the lines
	#from gluon import current
	#from gluon.storage import Storage
	with
	from gluon import *

	
// ---------------------------
*10. Menus*
	If you change menus, you have to restart web2py!
	
	We have the main menu (the one on top) and the options menu (the one at the side).
	Both can be configured in the <template>/menus.py file.
	
	See examples an expanation there (Afropa).
	
// ---------------------------
*11. Internationalization*

	This is easy! Just wrap all strings with T("<string>"). If this string is not translated,
	and add an entry in your language file found in languages/<...>.py.
	
	More info in the web2py book: http://web2py.com/books/default/chapter/29/04/the-core?search=redirect#Internationalization--and-Pluralization-with-T
// ---------------------------
*12. *
// ---------------------------
*13. *

// ---------------------------
*14. *
// ---------------------------
*15. *
// ---------------------------
*16. *
// ---------------------------
*17. Incorporate a new model (short)*
	1. create file models/resource.py
	
	2. create data table:
	tablename = "afropa_client"
	db.define_table(tablename,
    # A 'name' field
    Field("name",length=128,label="Name", requires=IS_NOT_EMPTY()),
    Field("firstname",label="First Name"),
    ...
	 *s3_meta_fields())

	3.  set/update CRUD settings
		s3.crud_strings[tablename] = Storage(
        	label_create = T("Create Client basic info"),
			...)
	
	4. create controller file: controllers/<resource>.py
		def <task>():
		    return s3_rest_controller()
   

// ---------------------------
*2. Incorporate a new model*

First, think of two names:
resource : namebody    : something 'bigger' than your task
component: yourtaskhere: what you are trying to do

The recource/component names will be heavyly used to as programatically as in the URL.

1. You need two files:

	models/<namebody>.py
	controllers/<namebody>.py
	edit text according to examples (e.g. asylumseeker.py)
	
	It is very important that the 'namebody' of your file matches
	the fist part of tablename = "<namebody>_<yourtaskhere>"
	
	- models/<namebody>.py
		- create the model
		- (set CRUD setting)
		
	- controller/<namebody.py>
		def <yourtaskhere>():
		    return s3_rest_controller()

	=> you can see your page at eden/<namebody>/<yourtaskhere>
	=> you can add first data!
	
2. 	add an index.html
#cd eden/views
#mkdir <namebody>
#cp asylumseeker/index.html <namebody>
# edit <namebody>/index.html
	
	- now it should be possible to see: eden/<namebody>

3. Add model to system (also create a link in the main menu)
	
	add to 000_config.py
	
	settings.modules["<namebody>"] = Storage(
        name_nice=T("<Namebody>"),
        module_type=2)
		
	or - if you have a template - add to your config.py (in your template directory)
		("<namebody>", Storage(
            name_nice=T("Afropa"),
            #description = "Afropa Client (basic information)",
            restricted = False,
            module_type=2)),
		
	now the model ist known to the system and you can check (e.g. in the controller):
	
	if not settings.has_module(module):
    	raise HTTP(404, body="Module disabled: %s" % module)

	## msw: could be important
	## Did you import the table in models/00_tables
	##
	
4. Add a menu at the side
	- edit modules/s3menus.py or <mytemplate>/menues.py => see examples there
	
	example:
	# Afropa menue
    @staticmethod
    def afropa():
        """ Afropa Registry """

        return M(c="afropa")(
                    M("Clients", f="client")(
                    	M("Create", m="create"),
                    	M("Import", m="import"),
                    	M("Report", m="report"),
               			)
					)
			   
5. Write data to file
	- create one entry
	- click export as XLS
	- some soffice will open,
	- save file as csv (set filter to: delimiter "," (comma) and embrace text with '"')
	- edit 
	- save
	
6. Read data from file
	- ??
	
7. update language file(s)
	If other languages are desired, you most probably must add some translations to the
	.py file(s) in the language directory.


questions:
 - how to incorporate upload facility for user classes?
 - where to steer the look-and-feel of the page (number of entries, search, downlowd-options,...)
 - how to make user classes work with 'standard' classes.
 - where to alter the frontpage?
 - should one edit s3dm, ... or something else
 - new modules like in 'book' or as a new class?
 - is there a 'read more' button for classes with many data-points?
 - where is the 'homepage'
 - what isy module_type? (config.py)
 settings.modules["housing"] = Storage(
        name_nice=T("Housing"),
        module_type=2)
 - do we need ansible  http://docs.ansible.com/ansible/quickstart.html
 - ... 
		


// skeleton to own class
1. change skeleton case sensitive to your name (e.g. housing)
2. add new module in models/00_tables.py
3. add controller and index functions in ./controller/housing.py
4. edit eden/views/housing/index.html


#
# migrating to other db / transformin to a real server
#

look at /web2py/application/welcome/private/appconfig.ini
this seem to have someting to do with it (see: http://www.web2py.com/books/default/chapter/29/01/introduction)


# some info (18.12.16) on working installarion scripts (from the ML-digest):
Normally for Developer mode, I install manually all the required libraries and install web2py and then EDEN. 
That should not be much of work.
For production mode, the scripts are maintained here: https://github.com/sahana/eden_deploy. 
I used this few month ago and they worked out of the box.
You can use it for developer mode as well for installing libraries and configuring them.

#other links (temp)
importing problems: https://groups.google.com/forum/#!searchin/sahana-eden/import$20data%7Csort:relevance/sahana-eden/mkzawV_O4FA/vy3Km4cXAgAJ
https://groups.google.com/forum/#!topic/sahana-eden/ikhl2dRqJGU%5B1-25%5D
