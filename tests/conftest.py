import allure
import pytest
import requests

from src.enums.urls import Url
from src.enums.headers import Headers
from src.enums.data import AuthData
from src.data_models.booking_request_data_model import BookingDataModel

HEADERS = Headers.HEADERS.value
BASE_URL = Url.BASE_URL.value
AUTH_DATA = AuthData.AUTH_DATA.value


@pytest.fixture(scope="session")
@allure.title("Создание сессии с авторизацией")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json=AUTH_DATA)
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
@allure.title("Генерация данных для элемента")
def booking_data():
    def _booking_data():
        booking = BookingDataModel.create_booking_data()
        return booking

    yield _booking_data
