# -*- coding: utf-8 -*-

def test_modification_contact(app):
    app.session.login("admin", "secret")
    app.contact.modification_first_contact()
    app.session.logout()
