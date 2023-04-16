import pytest
from fixture.application import Application


fixture = None  # глобальная переменная (fixture) пока не будет определена (None)


# инициализация фикстуры

# такая метка (@pytest.fixture()) превращает функцию (app) в инициализатор фикстуры
# функция app создает фикстуру, т.е. объект типа Application и возвращать эту фикстуру
# для разрушения фикстуры в функцию, которая инициализирует фикстуру (app) может передаваться специальный параметр (request)
@pytest.fixture
def app(request):
    global fixture  # объявляем, что мы собираемся пользоваться этой глобальной переменной
    # выполняем проверку
    if fixture is None:
        # нужно фикстуру проинициализировать
        fixture = Application()  # объект типа Application
        # после инициализации выполняем login
        fixture.session.login(username="admin", password="secret")
        # альтернативная ситуация. предположим, что фикстура уже создана и надо проверить не испортилась ли она, поэтому добавляем вторую проверку
    else:
        if not fixture.is_valid():
            fixture = Application()  # объект типа Application
            # после инициализации выполняем login
            fixture.session.login(username="admin", password="secret")
    return fixture

# для финализации делаем отдельную фикстуру
@pytest.fixture(scope="session", autouse=True)  # которая будет иметь scope="session"
def stop(request):
    # определяем маленькую локальную функцию
    def fin():
        fixture.session.logout()
        fixture.destroy()
    # указание на то, как эта фикстура должна быть разрушена
    request.addfinalizer(fin)  # в качестве финализатора теперь будет добавлена самодельная функция fin, которая будет выполнять сразу 2 действия и logout и destroy
    return fixture  # возвращает фикстуру