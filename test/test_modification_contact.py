# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modification_contact(app):

    if app.contact.count() == 0:  # если нет ни одного контакта
        app.contact.create_new_contact(Contact("first_name_mod", "middle_name_mod", "last_name_mod", "nickname_test",  # нужно группу предварительно создать
                    "title_test", "company_test", "address_test", "home_test", "123456789", "work_test",
                    "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                    "June", "1800", "15", "September", "1900", "address_test_secondary",
                    "home_test_secondary", "notes_test_secondary"))
    app.contact.modification_first_contact(Contact("1first_name_modification", "1middle_name_modification", "last_name_test", "nickname_test",
                            "title_test", "company_test", "address_modification", "home_test", "123456789", "work_test",
                            "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                            "June", "1800", "15", "September", "1900", "address_test_secondary",
                            "home_test_secondary", "notes_test_secondary"))
