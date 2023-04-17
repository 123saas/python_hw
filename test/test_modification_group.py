# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_group(app):
    if app.group.count() == 0: # если нет ни одной группы
        app.group.create_group(Group(name="test_group_name1", header="test_group_header1", footer="test_group_footer1"))  # нужно группу предварительно создать
    app.group.modification_first_group()
