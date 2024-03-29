import pytest
from fixture.application import Application
import jsonpickle
import json
import os.path
import importlib

fixture = None  # глобальная переменная (fixture) пока не будет определена (None)
target = None



# инициализация фикстуры

# такая метка (@pytest.fixture()) превращает функцию (app) в инициализатор фикстуры
# функция app создает фикстуру, т.е. объект типа Application и возвращать эту фикстуру
# для разрушения фикстуры в функцию, которая инициализирует фикстуру (app) может передаваться специальный параметр (request)
@pytest.fixture
def app(request):
    global fixture  # объявляем, что мы собираемся пользоваться этой глобальной переменной
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    # выполняем проверку
    if fixture is None or not fixture.is_valid():
        # нужно фикстуру проинициализировать
        fixture = Application(browser=browser, base_url=target['baseUrl'])  # объект типа Application
        # альтернативная ситуация. предположим, что фикстура уже создана и надо проверить не испортилась ли она, поэтому добавляем вторую проверку
    fixture.session.ensure_login(username=target['username'], password=target['password']) # строчку нужно выполнять не только после того, как браузер запущен, а выносят сюда, чтобы она выполнялась при каждом обращении к функции (def app(request)) инициализирующей фикстуру ->
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

# загрузить данные из модуля с заданным именем
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc): # добавляем специальную функцию, которая называется pytest_generate_tests и в качестве параметра в нее передается особый объект - metafunc (через этот объект можно получить практически полную информацию о тестовой функции)
    # в частности, мы можем получить информацию о фикстурах, которые есть у этой тестовой функции (они же, параметры тестовой функции
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"): # пробегаем по всем параметрам, но нас будут интересовать только те, которые начинаются с префикса data
            testdata = load_from_module(fixture[5:]) # как только встретилась такая фикстура мы должны загрузить тестовые данные из модуля, который имеет такое же название, как и фикстура, но обрезанные. первые 5 символов нужно удалить fixture[5:]
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata]) # используем загруженные тестовые данные для того, чтобы праметризовать нашу тестовую финкцию
            # нужно добавить еще одно условие для фикстур, которые начинаются с префикса json
        elif fixture.startswith("json_"):
            # необходимо выполнять похожее действие, только загружать будем не из модуля, а из json файла
            testdata = load_from_json(fixture[5:])  # как только встретилась такая фикстура мы должны загрузить тестовые данные из модуля, который имеет такое же название, как и фикстура, но обрезанные. первые 5 символов нужно удалить fixture[5:]
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


