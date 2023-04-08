# -*- coding: utf-8 -*-

# тестовый метод
def test_delete_first_group(app):
    # вспомогательные методы
    app.session.login(username="admin", password="secret")
    app.group.test_delete_first_group()
    app.session.logout()