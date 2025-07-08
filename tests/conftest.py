import pytest
import requests
from faker import Faker

from src.config.constant import Url, return_base_url, Headers, return_headers
from src.utils.validate_booking_request import BookingData

faker = Faker()

HEADERS = return_headers(Headers.HEADERS)
BASE_URL = return_base_url(Url.BASE_URL)


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth",
                                 json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    booking = BookingData.create_booking_data()
    return booking
