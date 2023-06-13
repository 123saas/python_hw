import re

def test_phones_on_home_page(app): # в качестве параметра в этот метод будет передаваться фикстура app. Фикстура инициализирует объект типа Application и там имеется ссылка на ContactHelper и именно через нее мы будем получать необходимую информацию
    # contact_from_home_page - это объект, который прочитали с главной страницы. в этом объекта информации о телефонах по отдельности нет
    contact_from_home_page = app.contact.get_contact_list()[0] # проверку буду делать не для всех контактов, а только для первого (индекс 0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # теперь получаем информацию о контакте из формы редактирования и в качетве индекса тоже передаем 0
    # после того, как мы получили эти два объекта - можно сравнивать их между собой
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page) # сравнивать с результатом склейки, который мы будем делать с помощью специальной функции merge_phones_like_on_home_page() и склеивать мы будем данные, которые хранятся в объекте contact_from_edit_page


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.home_phone2]))))  # склеивать нужно будет при помощи перевода строки, поэтому используем функцию join, которой в качестве параметра должны передать какой-то список,
    # список будет состоять из телефонов([contact.home_phone, contact.work_phone, contact.mobile_phone, contact.home_phone2])
    # и надо написать return "\n".join([contact.home_phone, contact.work_phone, contact.mobile_phone, contact.home_phone2]) - вернуть получившийся резкльтат склейки


# что происходит в merge_phones_like_on_home_page(contact)?
# исходный список [contact.home_phone, contact.work_phone, contact.mobile_phone, contact.home_phone2] из 4 элеметнтов
# отфильтровывается (filter(lambda x: x is not None) из него выкидываются все пустые, то есть имеющие значение None,
# потом к оставшимся применяется функция clear, которая в этих элементах удаляет все лишние символы (map(lambda x: clear(x)),
# потом, если в результате этой очистки у нас возникли пустые строки, то они тоже отфильтровываются (filter(lambda x: x != ""),
# и наконец, то что осталось склеивается при помощи перевода строки ("\n".join)