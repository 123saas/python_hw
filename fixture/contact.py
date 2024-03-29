from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        wd = self.app.wd
        # create new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_to_home(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/"):
            return
        # return to home
        wd.find_element_by_link_text("home").click()

    def modification_first_contact(self):
        self.modification_contact_by_index(0)

    def test_delete_first_contact(self):
        # Надо отправиться на страницу со списком контактов
        wd = self.app.wd
        self.return_to_home()
        # Надо выбрать первый контакт
        self.select_contact_by_index()
        # Потом удалить
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home()
        WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.return_to_home()
        # нам надо посчитать сколько чекбоксов присутствует на странице, то есть поискать все элементы, которые имеют имя "selected[]", взять длину (len) получившегося списка и вернуть ее (return)
        return len(wd.find_elements_by_name("selected[]"))  # количество групп, которые присутствуют в нашей адресной книге

    contact_cache = None  # создаем переменную

    def get_contact_list(self): # метод для загрузки списка, которыц читает таблицу на главной странице приложения и загружает оттуда информацию пока только имя и фамилию контакта
        if self.contact_cache is None:
            wd = self.app.wd  # получаем вебдрайвер
            self.return_to_home()  # отсюда будем читать информацию
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text  # можем получить текст
                firstname = cells[2].text
                # нам надо получить идентификатор
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text # в 5 столбце addressbook расположены номера телефонов и нарезать его не будем, а оставим в виде текста. куда в свойствах контакта пометить этот текст.
                # сделаем специальное свойство all_phones_from_home_page = all_phones. и all_phones_from_home_page надо добавить в model/contact
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def modification_contact_by_index(self, index, contact):
        # Надо отправиться на страницу со списком контактов
        wd = self.app.wd
        self.return_to_home()
        # Надо выбрать первый контакт
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click() # найти элемент "карандаш" и кликнуть по нему
        # Потом изменить
        self.fill_contact_form(contact)
        # обновить
        wd.find_element_by_name("update").click()
        self.return_to_home()
        self.contact_cache = None

    def test_delete_contact_by_index(self, index):
        # Надо отправиться на страницу со списком контактов
        wd = self.app.wd
        self.return_to_home()
        # Надо выбрать первый контакт
        self.select_contact_by_index(index)
        # Потом удалить
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home()
        WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_name("selected[]")[index].click()  # найти элемент по имени selected[] и кликнуть по нему

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        home_phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, home_phone2=home_phone2, email=email,
                       email2=email2, email3=email3)