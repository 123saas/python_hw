import pytest
from fixture.application import Application

# инициализация фикстуры

# такая метка (@pytest.fixture()) превращает функцию (app) в инициализатор фикстуры
# функция app создает фикстуру, т.е. объект типа Application и возвращать эту фикстуру
# для разрушения фикстуры в функцию, которая инициализирует фикстуру (app) может передаваться специальный параметр (request)
@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()  # объект типа Application
    fixture.session.login(username="admin", password="secret")
    # определяем маленькую локальную функцию
    def fin():
        fixture.session.logout()
        fixture.destroy()
    # указание на то, как эта фикстура должна быть разрушена
    request.addfinalizer(fin)  # в качестве финализатора теперь будет добавлена самодельная функция fin, которая будет выполнять сразу 2 действия и logout и destroy
    return fixture  # возвращает фикстуру