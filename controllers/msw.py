# ---------------
# you should always have a index controller
def index():
    return dict()


# ---------------
# with am error function defined, you can allways redirect(URL('error'))
def error():
    response.flash("There was an error")


# ---------------
# manually display a person (give id-number as first arg: e.g. asylum/msw/display_form/2)
# uses list_records() defined below
# taken from book, ch 7, "Links to referencing records"
def display_form():
    record = db.msw_person(request.args(0)) or redirect(URL('index'))
    url = URL('download')
    link = URL('list_records', args='db')

    # make the form
    form = SQLFORM(db.msw_person, record, deletable=True,
                  upload=url, linkto=link,
                  labels = {'msw_dog.dog_owner':"This person's dogs"})

    # make an extra element
    my_extra_element = TR(LABEL('I agree to the terms and conditions'),
                         INPUT(_name='agree',value=True,_type='checkbox'))
    form[0].insert(-1,my_extra_element)

    # process the form
    if form.process().accepted:
        response.flash = 'form accepted'

        print "form.vars.agree:",form.vars.agree

        if form.vars.agree == 'on':
            print "checkbox was 'on'!"
        elif form.vars.agree == None:
            print
            "checkbox was 'None'!"
        else:
            print "very strange"

    elif form.errors:
        response.flash = 'form has errors'

    return dict(form=form)

# ---------------------------------
#
# taken from book, ch 7, "Links to referencing records"
def list_records():
    import re
    REGEX = re.compile('^(\w+).(\w+).(\w+)\=\=(\d+)$')
    match = REGEX.match(request.vars.query)
    if not match:
        redirect(URL('error'))
    table, field, id = match.group(2), match.group(3), match.group(4)
    records = db(db[table][field]==id).select()
    return dict(records=records)

# --------------------
# use a grid to display all persons
@auth.requires_login()
def grid_person():
    grid = SQLFORM.grid(db.msw_person)
    return locals()

# --------------------
# manage table manually using a grid, give table name as arg(0)
@auth.requires_login()
def manage():

    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table],
                        args=request.args[:1],
                        links_in_grid=True)
    return locals()

# --------------------
# show two (linked) tables together (using a grid)
@auth.requires_login()
def person_and_dog():
    grid = SQLFORM.grid(db.msw_person,left=db.msw_dog.on(db.msw_dog.dog_owner==db.msw_person.id))

    return locals()

# --------------------
# show two (linked) tables together (using a smartgrid)
@auth.requires_login()
def person_and_dog_smart():
    grid = SQLFORM.smartgrid(db.msw_person,linked_tables=['msw_dog'])
    return locals()

# --------------------
# show three (linked) tables together (using a smartgrid)
@auth.requires_login()
def person_dog_thing_smart():
    grid = SQLFORM.smartgrid(db.msw_person,linked_tables=['msw_dog','msw_thing'])
    return locals()


# --------------------
def test_view():
    a = DIV(SPAN('a', 'b'), 'c')

    return locals()