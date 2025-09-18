import allure

from src.enums.urls import Url


class BookingApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = Url.BASE_URL.value

    @allure.step("Создание booking")
    def create_booking(self, booking_data):
        """Отправляет запрос на создание booking."""
        response = self.auth_session.post(f"{self.base_url}/booking", json=booking_data.model_dump())
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status()  # Выбросит HTTPError для плохих статусов
        return response

    @allure.step("Получение bookings")
    def get_bookings(self, booking_id=""):
        """Отправляет запрос на получение списка bookings."""
        response = self.auth_session.get(f"{self.base_url}/booking/{booking_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response

    @allure.step("Обновление booking")
    def update_booking(self, booking_id, booking_data):
        """Отправляет запрос на обновление booking."""
        response = self.auth_session.put(f"{self.base_url}/booking/{booking_id}", json=booking_data.model_dump())
        if response.status_code != 200:
            response.raise_for_status()
        return response

    @allure.step("Частичное обновление booking")
    def partial_update_booking(self, booking_id, booking_data):
        """Отправляет запрос на частичное обновление booking."""
        response = self.auth_session.patch(f"{self.base_url}/booking/{booking_id}", json=booking_data.model_dump())
        if response.status_code != 200:
            response.raise_for_status()
        return response

    @allure.step("Удаление booking")
    def delete_booking(self, booking_id):
        """Отправляет запрос на удаление booking."""
        response = self.auth_session.delete(f"{self.base_url}/booking/{booking_id}")
        if response.status_code != 201:  # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response  # или response.status_code
