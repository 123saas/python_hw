from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
# конструктор, который инициализирует ссылку на драйвер, потом инициализирует помощников (SessionHelper,GroupHelper, ContactHelper)
    def __init__(self):
        self.wd = webdriver.Firefox(executable_path='C:\Windows\SysWOW64\geckodriver.exe')  # запуск драйвера
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self) # вот так помощник (SessionHelper) получается ссылку на объект класса Application. Это даст возможность в одном помощнике обратиться к какому-то другому помощнику через объект класса Application
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

# метод, который разрушает фикстуру (destroy), в частности, он останавливает браузер
    def destroy(self):
        self.wd.quit()