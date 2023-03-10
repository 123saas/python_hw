# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_new_contact(Contact("1first_name_test", "1middle_name_test", "last_name_test", "nickname_test",
                            "title_test", "company_test", "address_test", "home_test", "123456789", "work_test",
                            "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                            "June", "1800", "15", "September", "1900", "address_test_secondary",
                            "home_test_secondary", "notes_test_secondary"))
    app.session.logout()

