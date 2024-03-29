# -*- coding: utf-8 -*-
from model.contact import Contact



def test_create_contact(app, json_contacts):
    contact = json_contacts
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
