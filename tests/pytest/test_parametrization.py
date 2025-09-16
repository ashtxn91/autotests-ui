import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def browser(request: SubRequest) -> str:
    return (
        request.param
    )  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")


@pytest.mark.parametrize(
    "value", [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass
