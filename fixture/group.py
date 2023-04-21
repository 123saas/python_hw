from model.group import Group



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
        # после успешного выполнения метода create мы должны кеш сбросить:
        self.group_cache = None  # кеш стал невалидным и при следующем обращении к методу get_group_list() он будет построен заново

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
        # после успешного выполнения метода delete мы должны кеш сбросить:
        self.group_cache = None  # кеш стал невалидным и при следующем обращении к методу get_group_list() он будет построен заново

    def return_to_groups_page(self):
        # возврат на страницу со списком групп
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def modification_first_group(self, group):
        # Надо отправиться на страницу со списком групп
        wd = self.app.wd
        self.open_groups_page()
        # Надо выбрать первую группу
        wd.find_element_by_name("selected[]").click()  # найти элемент по имени selected[] и кликнуть по нему
        wd.find_element_by_name("edit").click()  # найти элемент по имени edit и кликнуть
        # Потом изменить
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        # после успешного выполнения метода modification мы должны кеш сбросить:
        self.group_cache = None  # кеш стал невалидным и при следующем обращении к методу get_group_list() он будет построен заново

    def count(self):
        wd = self.app.wd
        self.open_groups_page()  # перейти на страницу со списком групп
        # нам надо посчитать сколько чекбоксов присутствует на странице, то есть поискать все элементы, которые имеют имя "selected[]", взять длину (len) получившегося списка и вернуть ее (return)
        return len(wd.find_elements_by_name("selected[]"))  # количество групп, которые присутствуют в нашей адресной книге

    group_cache = None  # создаем переменную

    def get_group_list(self):
        # делаем проверку: если self.group_cache is None, то есть кеш пустой
        if self.group_cache is None:
            # тогда нужно загрузить информацию из браузера, то есть нужно выполнить следующие действия
            wd = self.app.wd  # получаем вебдрайвер
            self.open_groups_page()  # отсюда будем читать информацию
            self.group_cache = []
            for element in (wd.find_elements_by_css_selector("span.group")):  # находим все элементы by_css_selector и указываем, что мы ищем: span, который имеет класс group (wd.find_elements_by_css_selector("span.group")) и теперь нам нужно по этим элементам устроить цикл
                text = element.text  # можем получить текст
                # нам надо получить идентификатор
                id = element.find_element_by_name("selected[]").get_attribute("value")  # для этого мы внутри этого элемента span находим другой элемент, который имеет имя selected[] ( то есть чекбокс находящийся внутри элемента span) и у этого чекбокса получаем значение атрибута "value" (get_attribute("value"))
                # по этим двум свойствам мы должны построить объект типа Group и добавить его в какой-то список (groups), который будет в конце возвращаться
                self.group_cache.append(Group(name=text, id=id))  # добавляем новую группу. И в качестве параметров при конструировании нового объекта указываем name = text, id=id
        return list(self.group_cache)








