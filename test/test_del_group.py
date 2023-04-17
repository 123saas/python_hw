# -*- coding: utf-8 -*-
from model.group import Group

# тестовый метод
def test_delete_first_group(app):
    if app.group.count() == 0: # если нет ни одной группы
        app.group.create_group(Group(name="test_group_name1", header="test_group_header1", footer="test_group_footer1"))  # нужно группу предварительно создать
    # вспомогательные методы
    app.group.test_delete_first_group()