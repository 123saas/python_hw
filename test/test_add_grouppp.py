# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

# инициализация фикстуры

# такая метка (@pytest.fixture()) превращает функцию (app) в инициализатор фикстуры
# функция app создает фикстуру, т.е. объект типа Application и возвращать эту фикстуру
# для разрушения фикстуры в функцию, которая инициализирует фикстуру (app) может передаваться специальный параметр (request)
@pytest.fixture
def app(request):
    fixture = Application()  # объект типа Application
    # указание на то, как эта фикстура должна быть разрушена
    request.addfinalizer(fixture.destroy)  # у параметра request есть метод addfinalizer, а передать надо fixture.destroy
    return fixture  # возвращает фикстуру


# тестовый метод
def test_add_group(app):
    # вспомогательные методы
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_group_name", header="test_group_header", footer="test_group_footer"))
    app.logout()

