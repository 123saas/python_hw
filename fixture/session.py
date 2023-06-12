
# помощник по работе с сессиями
# в этот класс переносятся вспомогательные методы login и logout
class SessionHelper:
    # делаем конструктор
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # login
        wd = self.app.wd
        self.app.open_home_page() # пытаемся открыть главную страницу, но метод open_home_page() остался в фикстуре, поэтому обращаемся так: self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        # выход
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd  # понадобиться ссылка на драйвер
        # нужно проверить "А мы всё еще внутри активной сессии находимся или уже снаружи?". Если находимся снаружи, то делать ничего не надо
        # надо проверить, "А есть ли на странице вот эта ссылка wd.find_element_by_link_text("Logout")? Если ссылка есть, то нужно по ней кликать, если ссылки нет, то мы уже находимся на форме логина и ничего делать не надо

        if self.is_logged_in():  # этот метод (elements) вернет все элементы, которые присутсвуют на странице и удовлетворяют заданному критерию и нужно узнать сколько их. ->
            # -> нас конкретное точное количество не интересует. нам важно знать, что их количество, то есть длина этого списка (len) > 0, то есть хотя бы один такой элемент есть
            self.logout()  # если такой элемент присутствует на странице, значит надо выполнять logout, иначе, ничего делать не надо

    def is_logged_in(self):
        wd = self.app.wd  # понадобиться ссылка на драйвер
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd  # понадобиться ссылка на драйвер
        return self.get_logged_user() == username  # у найденного элемента нужно взять текст. этот текст надо стравнить с именем пользователя, но взятое в круглые скобки

    def get_logged_user(self): # определяем метод get_logged_user
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]  # метод будет делать следующее: читает текст (.text) из окна браузера, который содержит имя пользователя, а потом мы из этого текста делаем вырезку, нам надо отрезать первый и последний символы, поэтому мы делаем вырезку от 1 до предполседнего символа

    def ensure_login(self, username, password):
        wd = self.app.wd  # понадобиться ссылка на драйвер
        # надо проверить, что мы в систему уже вошли
        if self.is_logged_in():
            # надо проверить, что мы зашли как пользователь с таким именем, поэтому добавляем вторую проверку
            if self.is_logged_in_as(username):  # если вошли в систему is_logged_in_as(username)
                return  # в это случае ничего делать не надо, можно сразу завершить (return). выход из этого метода и всё
            else:  # иначе, вошли в систему, но пользователь не тот
                self.logout()  # сначала надо сделать logout()
                # после этого надо делать self.login(username, password), но и в ситуации, когда мы не вошли в систему - тоже надо делать self.login(username, password)
        self.login(username, password)  # поэтому self.login(username, password) сделаем в самом конце. До этой строки мы доберемся в двух случаях: 1. если пользователь не залогинин и тогда мы сразу проваливаемся в эту строчку
        # и 2 ситуация, когда он залогинин, о имя не совпадает, тогда мы сначала попадем на self.logout()  и потом вновь сюда self.login(username, password)
        # а если пользователь залогинин, причем залогинин именно тот, который нужен, значит преждевременный выход из этого метода (return) и делать ничего не надо






