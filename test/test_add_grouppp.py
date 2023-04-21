# -*- coding: utf-8 -*-
from model.group import Group


# тестовый метод
def test_add_group(app):
    # перед созданием группы нам нужно сначала сохранить старый список групп (old_groups)
    old_groups = app.group.get_group_list()  # загружать список будем с помощью вспомогательной функции, которую поместим в помощник по работе с группами - app.group.get_group_list()
    group = Group(name="test_group_name", header="test_group_header", footer="test_group_footer")
    # вспомогательные методы
    app.group.create_group(group)
    # после того, как действие выполнено, надо получить новый список
    new_groups = app.group.get_group_list()
    # надо сделать простую проверку: Убедимся, что новый список на единицу длиннее, чем старый. Проверки в тестах делаются с помощью ключевого слова assert
    assert len(old_groups) + 1 == len(new_groups) # мы должны написать выражение, от которого требуется, чтобы оно было истинным: длина старого списка групп (len(old_groups)) + 1 = длине нового списка групп (len(new_groups))
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# вначале следующего теста можем воспользоваться информацией списокм групп, который был получен в конце предыдущего
# теста (new_groups = app.group.get_group_list()). Если у нас тестов 100, то всего обращений к методу get_group_list()
# будет равно 200, но если вначале теста мы будем использовать кешированное значение, то количество реальных загрузок
# этого списка из браузера уменьшится с 200 до 101
# в методе get_group_list мы будем возвращать кешированное значение, если оно доступно

def test_add_empty_group(app):
    # перед созданием группы нам нужно сначала сохранить старый список групп (old_groups)
    old_groups = app.group.get_group_list()  # загружать список будем с помощью вспомогательной функции, которую поместим в помощник по работе с группами - app.group.get_group_list()
    group = Group(name="", header="", footer="")
    # вспомогательные методы
    app.group.create_group(group)
    # после того, как действие выполнено, надо получить новый список
    new_groups = app.group.get_group_list()
    # надо сделать простую проверку: Убедимся, что новый список на единицу длиннее, чем старый. Проверки в тестах делаются с помощью ключевого слова assert
    assert len(old_groups) + 1 == len(new_groups) # мы должны написать выражение, от которого требуется, чтобы оно было истинным: длина старого списка групп (len(old_groups)) + 1 = длине нового списка групп (len(new_groups))
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

