
# помощник по работе с сессиями
#в этот класс переносятся вспомогательные методы login и logout
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