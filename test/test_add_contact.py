# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_group import constant as testdata

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
