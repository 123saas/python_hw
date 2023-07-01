# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "-", "-", " ", "-",
                      "-", " ", " ", " ", " ")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
            home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage=random_string("homepage", 10), bday='16',
            bmonth='April', byear=random_string("byear", 4), aday='18',
            amonth='May', ayear=random_string("ayear", 4), address2=random_string("address2", 10),
            home_phone2=random_string("home_phone2", 10), notes=random_string("notes", 10))
    for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_create_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "-", "-", " ", "-",
#                       "-", " ", " ", " ", " ")
#     app.contact.create_new_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
