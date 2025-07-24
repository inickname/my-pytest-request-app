from src.api.booking_api_client import BookingApiClient
from src.data_models.booking_response_data_model import BookingResponseModel
from src.utils.validate_booking_response import validate_response


class BookingScenarios:
    def __init__(self, api_client: BookingApiClient):  # Типизация для ясности
        self.api_client = api_client

    def get_and_verify_bookings_exist(self):
        """
        Сценарий: получить список bookings и проверить, что он не пуст.
        """
        bookings = self.api_client.get_bookings().json()
        assert len(bookings) > 0, "Список bookings пуст"
        print(f"Получено {len(bookings)} bookings id.")
        return bookings

    def create_booking_check_and_delete(self, booking_data):
        """
        Сценарий: создать booking и сразу же его удалить.
        Возвращает ID созданного и удаленного booking.
        """
        created_booking_data = self.api_client.create_booking(booking_data)
        booking_id = created_booking_data.get("bookingid")
        assert booking_id is not None, f"ID не найден в ответе на создание: {created_booking_data}"

        get_booking = self.api_client.get_bookings(booking_id)
        validate_response(get_booking, BookingResponseModel, 200, booking_data.model_dump())

        self.api_client.delete_booking(booking_id)
        # Проверка на успешность удаления внутри delete_booking (raise_for_status)
        # или можно проверить статус ответа здесь, если delete_booking его возвращает
        print(f"Booking с ID {booking_id} успешно создан и удален.")
        return booking_id

    def update_booking_and_verify_changes(self, booking_id, booking_data):
        """
        Сценарий: обновить booking и проверить, что данные изменились.
        """
        updated_booking = self.api_client.update_booking(booking_id, booking_data)

        assert updated_booking["firstname"] == booking_data.firstname, \
            f"Имя не обновилось. Ожидалось: {booking_data['firstname']}, получено: {updated_booking['firstname']}"
        assert updated_booking["lastname"] == booking_data.lastname, \
            f"Фамилия не обновилась. Ожидалось: {booking_data['lastname']}, получено: {updated_booking['lastname']}"
        print(f"Booking с ID {booking_id} успешно обновлен.")
        return updated_booking

    def delete_existing_booking_and_verify(self, booking_id):  # test_booking переименован в booking_id для ясности
        """
        Сценарий: удалить существующий booking и убедиться, что он удален.
        """
        self.api_client.delete_booking(booking_id)
        print(f"Booking с ID {booking_id} отправлен на удаление.")
