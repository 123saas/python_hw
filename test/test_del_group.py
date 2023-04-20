# -*- coding: utf-8 -*-
from model.group import Group

# тестовый метод
def test_delete_first_group(app):
    if app.group.count() == 0: # если нет ни одной группы
        app.group.create_group(Group(name="test_group_name1", header="test_group_header1", footer="test_group_footer1"))  # нужно группу предварительно создать
    old_groups = app.group.get_group_list()
    # вспомогательные методы
    app.group.test_delete_first_group()
    new_groups = app.group.get_group_list()
    # надо сделать простую проверку: Убедимся, что новый список на единицу длиннее, чем старый. Проверки в тестах делаются с помощью ключевого слова assert
    assert len(old_groups) - 1 == len(new_groups)  # мы должны написать выражение, от которого требуется, чтобы оно было истинным: длина старого списка групп (len(old_groups)) + 1 = длине нового списка групп (len(new_groups))
