# переносим сюда все вспомогательные методы, которые относятся к работе с группами
class GroupHelper:
    # делаем конструктор, в который будет передаваться ссылка на Application (главный класс фикстуры)
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # открытие страницы группы
        wd = self.app.wd #доступ к драйверу теперь получается через ссылку на основной класс Application (именно там она хранится общая для всех) (поэтому дописывается app)
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

    def return_to_groups_page(self):
        # возврат на страницу со списком групп
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

