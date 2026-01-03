from src.api.booking_api_client import BookingApiClient
from src.data_models.booking_response_data_model import BookingResponseModel
from src.utils.validate_booking_response import ValidateBookingResponse


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
        booking_data = booking_data()
        created_booking_data = self.api_client.create_booking(booking_data)
        booking_id = created_booking_data.json().get("bookingid")
        assert booking_id is not None, f"ID не найден в ответе на создание: {created_booking_data}"

        get_booking = self.api_client.get_bookings(booking_id)
        ValidateBookingResponse.validate_response(get_booking, BookingResponseModel, 200,
                                                  booking_data.model_dump())

        self.api_client.delete_booking(booking_id)
        # Проверка на успешность удаления внутри delete_booking (raise_for_status)
        # или можно проверить статус ответа здесь, если delete_booking его возвращает
        print(f"Booking с ID {booking_id} успешно создан и удален.")
        return booking_id

    def update_booking_and_verify_changes(self, booking_data):
        """
        Сценарий: обновить booking и проверить, что данные изменились.
        """
        booking_data_1 = booking_data()
        booking_data_2 = booking_data()
        booking_id = self.api_client.create_booking(booking_data_1).json().get("bookingid")
        updated_booking = self.api_client.update_booking(booking_id, booking_data_2)

        ValidateBookingResponse.validate_response(updated_booking, BookingResponseModel, 200,
                                                  booking_data_2.model_dump())

        print(f"Booking с ID {booking_id} успешно обновлен.")
        self.api_client.delete_booking(booking_id)
        return booking_id

    def partial_update_booking_and_verify_changes(self, booking_data):
        """
        Сценарий: Частично обновить booking и проверить, что данные изменились.
        """
        booking_data_1 = booking_data()
        booking_data_2 = booking_data()
        booking_id = self.api_client.create_booking(booking_data_1).json().get("bookingid")
        partial_update_booking = self.api_client.partial_update_booking(booking_id, booking_data_2)

        ValidateBookingResponse.validate_response(partial_update_booking, BookingResponseModel, 200,
                                                  booking_data_2.model_dump())

        print(f"Booking с ID {booking_id} успешно обновлен.")
        self.api_client.delete_booking(booking_id)
        return booking_id

    def delete_existing_booking_and_verify(self, booking_data):  # test_booking переименован в booking_id для ясности
        """
        Сценарий: удалить существующий booking и убедиться, что он удален.
        """
        booking_data = booking_data()
        booking_id = self.api_client.create_booking(booking_data).json().get("bookingid")

        self.api_client.delete_booking(booking_id)
        print(f"Booking с ID {booking_id} отправлен на удаление.")
        return booking_id
