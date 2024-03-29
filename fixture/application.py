from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
# конструктор, который инициализирует ссылку на драйвер, потом инициализирует помощников (SessionHelper,GroupHelper, ContactHelper)
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path='C:\Windows\SysWOW64\geckodriver.exe')  # запуск драйвера
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path='C:\Windows\System32\chromedriver.exe')  # запуск драйвера
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path='C:\Windows\System32\IEDriverServer.exe')  # запуск драйвера
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self) # вот так помощник (SessionHelper) получается ссылку на объект класса Application. Это даст возможность в одном помощнике обратиться к какому-то другому помощнику через объект класса Application
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        # try except - это блок с перехватом исключений. если при выполнении этого блока возникают какие-то проблемы, генерируется исключение, то мы можем его перехватить и в блоке except написать какой-то обработчик, то есть как-то отреагировать на эту проблемную ситуацию. здесь мы это и делаем
        # если удалось у браузера получить текущий адрес, то всё хорошо
        try:
            self.wd.current_url # попросим у браузера, чтобы он нам сказал какой текущий адрес открытой страницы
            # если он сможет это сделать, значит всё хорошо и мы можем вернуть значение true
            return True
        # если не удалось, возникло какое-то исключение, значит альтернативный вариант - "Все плохо. Возвращаем False"
        # иначе, если возникли какие-то проблемы при попытке получить текущий адрес страницы, тогда return False
        except:
            return False


    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get(self.base_url)

# метод, который разрушает фикстуру (destroy), в частности, он останавливает браузер
    def destroy(self):
        self.wd.quit()