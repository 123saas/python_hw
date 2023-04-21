# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modification_group(app):
    if app.group.count() == 0:  # если нет ни одной группы
        app.group.create_group(Group(name="test_group_name1", header="test_group_header1", footer="test_group_footer1"))  # нужно группу предварительно создать
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modification_group_name")
    group.id = old_groups[index].id
    app.group.modification_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    # надо сделать простую проверку: Убедимся, что новый список на единицу длиннее, чем старый. Проверки в тестах делаются с помощью ключевого слова assert
    assert len(old_groups) == len(new_groups)  # мы должны написать выражение, от которого требуется, чтобы оно было истинным: длина старого списка групп (len(old_groups)) + 1 = длине нового списка групп (len(new_groups))
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
