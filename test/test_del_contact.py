# -*- coding: utf-8 -*-
from model.contact import Contact

# тестовый метод
def test_delete_first_contact(app):
    if app.contact.count() == 0:  # если нет ни одного контакта
        app.contact.create_new_contact(Contact("first_name_del", "middle_name_del", "last_name_del", "nickname_test",  # нужно группу предварительно создать
                    "title_test", "company_test", "address_test", "home_test", "123456789", "work_test",
                    "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                    "June", "1800", "15", "September", "1900", "address_test_secondary",
                    "home_test_secondary", "notes_test_secondary"))

    old_contacts = app.contact.get_contact_list()
    # вспомогательные методы
    app.contact.test_delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

