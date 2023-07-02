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
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    # выполняем проверку
    if fixture is None:
        # нужно фикстуру проинициализировать
        fixture = Application(browser=browser, base_url=base_url)  # объект типа Application
        # альтернативная ситуация. предположим, что фикстура уже создана и надо проверить не испортилась ли она, поэтому добавляем вторую проверку
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)  # объект типа Application
    fixture.session.ensure_login(username="admin", password="secret") # строчку нужно выполнять не только после того, как браузер запущен, а выносят сюда, чтобы она выполнялась при каждом обращении к функции (def app(request)) инициализирующей фикстуру ->
    # -> точно так же как и с logout нам не надо выполнять login, нам надо выполнять его интеллектуально, поэтому сделаем вспомогательный метод ensure_login, который будет выполнять проверку "Нужно выполнять login или не нужно?". Eсли мы уже залогинились как правильные пользователи, то делать ничего не надо
    return fixture

# для финализации делаем отдельную фикстуру
@pytest.fixture(scope="session", autouse=True)  # которая будет иметь scope="session"
def stop(request):
    # определяем маленькую локальную функцию
    def fin():
        fixture.session.ensure_logout()  # убедиться, что мы вышли из системы
        fixture.destroy()
    # указание на то, как эта фикстура должна быть разрушена
    request.addfinalizer(fin)  # в качестве финализатора теперь будет добавлена самодельная функция fin, которая будет выполнять сразу 2 действия и logout и destroy
    return fixture  # возвращает фикстуру

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")