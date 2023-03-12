import pytest
from fixture.application import Application

# инициализация фикстуры

# такая метка (@pytest.fixture()) превращает функцию (app) в инициализатор фикстуры
# функция app создает фикстуру, т.е. объект типа Application и возвращать эту фикстуру
# для разрушения фикстуры в функцию, которая инициализирует фикстуру (app) может передаваться специальный параметр (request)
@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()  # объект типа Application
    # указание на то, как эта фикстура должна быть разрушена
    request.addfinalizer(fixture.destroy)  # у параметра request есть метод addfinalizer, а передать надо fixture.destroy
    return fixture  # возвращает фикстуру