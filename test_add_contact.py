# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("1first_name_test", "1middle_name_test", "last_name_test", "nickname_test",
                            "title_test", "company_test", "address_test", "home_test", "123456789", "work_test",
                            "fax_test", "e-mail_test", "e-mail_test2", "email_test3", "homepage_test", "18",
                            "June", "1800", "15", "September", "1900", "address_test_secondary",
                            "home_test_secondary", "notes_test_secondary"))
    app.logout()

