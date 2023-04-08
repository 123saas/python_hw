# -*- coding: utf-8 -*-
# тестовый метод
def test_delete_first_contact(app):
    # вспомогательные методы
    app.session.login(username="admin", password="secret")
    app.contact.test_delete_first_contact()
    app.session.logout()