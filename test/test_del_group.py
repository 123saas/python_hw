# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

# тестовый метод
def test_delete_some_group(app):
    if app.group.count() == 0: # если нет ни одной группы
        app.group.create_group(Group(name="test_group_name1", header="test_group_header1", footer="test_group_footer1"))  # нужно группу предварительно создать
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups)) # определим индекс удаляемой группы (randrange(len(old_groups))). randrange генерирует случайное число от 0 до указанного в качествве параметра значения (len(old_groups))
    # вспомогательные методы
    app.group.test_delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    # надо сделать простую проверку: Убедимся, что новый список на единицу длиннее, чем старый. Проверки в тестах делаются с помощью ключевого слова assert
    assert len(old_groups) - 1 == len(new_groups)  # мы должны написать выражение, от которого требуется, чтобы оно было истинным: длина старого списка групп (len(old_groups)) + 1 = длине нового списка групп (len(new_groups))
    old_groups[index:index+1] = []
    assert old_groups == new_groups