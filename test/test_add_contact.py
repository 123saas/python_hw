# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("3first_name_test234", "13middle_name_test34", "3last_name_test234", "nickname_test",
                      "title_test", "company_test", "address_test", "home_test", "123456789", "work_test",
                      "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                      "June", "1800", "15", "September", "1900", "address_test_secondary",
                      "home_test_secondary", "notes_test_secondary")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "-", "-", " ", "-",
                      "-", " ", " ", " ", " ")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
