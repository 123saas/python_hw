# -*- coding: utf-8 -*-

def test_modification_group(app):
    app.session.login("admin", "secret")
    app.group.modification_first_group()
    app.session.logout()
