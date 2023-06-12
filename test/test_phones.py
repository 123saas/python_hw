

def test_phones_on_home_page(app): # в качестве параметра в этот метод будет передаваться фикстура app. Фикстура инициализирует объект типа Application и там имеется ссылка на ContactHelper и именно через нее мы будем получать необходимую информацию
    contact_from_home_page = app.contact.get_contact_list()[0] # проверку буду делать не для всех контактов, а только для первого (индекс 0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # теперь получаем информацию о контакте из формы редактирования и в качетве индекса тоже передаем 0
    # после того, как мы получили эти два объекта - можно сравнивать их между собой
    assert contact_from_home_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_home_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_home_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_home_page.home_phone2 == contact_from_edit_page.home_phone2

