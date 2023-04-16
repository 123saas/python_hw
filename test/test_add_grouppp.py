# -*- coding: utf-8 -*-
from model.group import Group


# тестовый метод
def test_add_group(app):
    # вспомогательные методы
    app.group.create_group(Group(name="test_group_name", header="test_group_header", footer="test_group_footer"))

