# переносим сюда все вспомогательные методы, которые относятся к работе с группами
class GroupHelper:
    # делаем конструктор, в который будет передаваться ссылка на Application (главный класс фикстуры)
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # открытие страницы группы
        wd = self.app.wd #доступ к драйверу теперь получается через ссылку на основной класс Application (именно там она хранится общая для всех) (поэтому дописывается app)
        # мы можем проверить: "Если мы находимся на нужной странице, то ничего делать не надо если это верно, значит мы находимся на нужной странице и переход делать не надо
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:  # поскольку другие разделы имеют такой же адрес, то надо добавить еще условие: количество элементов найденных по имени "new" больше 0 (len(wd.find_elements_by_name("new")) > 0)
            return
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        # заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # подтверждение
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def test_delete_first_group(self):
        # Надо отправиться на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        # Надо выбрать первую группу
        wd.find_element_by_name("selected[]").click()  # найти элемент по имени selected[] и кликнуть по нему
        # Потом удалить
        wd.find_element_by_name("delete").click()  # найти элемент по имени delete и кликнуть
        self.return_to_groups_page()
        # wd.switch_to.alert.accept()

    def return_to_groups_page(self):
        # возврат на страницу со списком групп
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def modification_first_group(self):
        # Надо отправиться на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        # Надо выбрать первую группу
        wd.find_element_by_name("selected[]").click()  # найти элемент по имени selected[] и кликнуть по нему
        wd.find_element_by_name("edit").click()  # найти элемент по имени edit и кликнуть
        # Потом изменить
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("modification_group_name")
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()  # перейти на страницу со списком групп
        # нам надо посчитать сколько чекбоксов присутствует на странице, то есть поискать все элементы, которые имеют имя "selected[]", взять длину (len) получившегося списка и вернуть ее (return)
        return len(wd.find_elements_by_name("selected[]"))  # количество групп, которые присутствуют в нашей адресной книге



