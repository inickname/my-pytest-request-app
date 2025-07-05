import requests

from src.conftest import auth_session
from src.constant import BASE_URL, HEADERS


class TestBookings:

    def test_create_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_get_bookings_ids(self, auth_session):
        get_bookings_ids = auth_session.get(f"{BASE_URL}/booking")
        assert get_bookings_ids.status_code == 200

        bookings_ids_response = get_bookings_ids.json()
        assert len(bookings_ids_response) > 0, "Список идентификаторов бронирований пуст"

    def test_get_bookings_ids_filtered_by_name(self, auth_session):
        get_bookings_ids_filtered_by_name = auth_session.get(f"{BASE_URL}/booking?firstname=Sally&lastname=Brown")
        assert get_bookings_ids_filtered_by_name.status_code == 200
        booking_id = get_bookings_ids_filtered_by_name.json()[0].get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == "Sally", "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == "Brown", "Фамилия не совпадает с заданной"

    def test_get_bookings_ids_filtered_by_date(self, auth_session):
        get_bookings_ids_filtered_by_date = auth_session.get(f"{BASE_URL}/booking?checkout=2019-01-01")
        assert get_bookings_ids_filtered_by_date.status_code == 200
        booking_id = get_bookings_ids_filtered_by_date.json()[0].get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['bookingdates']['checkout'] == "2019-01-01", "Дата выезда не совпадает"

    def test_update_booking(self, booking_data, auth_session):
        initial_booking_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=initial_booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        # Проверка без токена
        update_booking = requests.put(f"{BASE_URL}/booking/{booking_id}", headers=HEADERS, json=booking_data)
        assert update_booking.status_code == 403, "Доступ к запрошенному ресурсу разрешен"

        # Проверка с поддельным токеном
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token=faketoken555"}
        update_booking = requests.put(f"{BASE_URL}/booking/{booking_id}", headers=headers, json=booking_data)
        assert update_booking.status_code == 403, "Доступ к запрошенному ресурсу разрешен"

        # Проверка с пустым телом запроса
        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json={})
        assert update_booking.status_code == 400, "Сервер принимает пустое тело запроса"

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
        assert update_booking.status_code == 200

        booking_data_response = update_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

    def test_partial_update_booking(self, booking_data, auth_session):
        partial_booking_data = {
            "firstname": "Firstname",
            "lastname": "Lastname"
        }

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        # Проверка без токена
        update_booking = requests.patch(f"{BASE_URL}/booking/{booking_id}", headers=HEADERS, json=partial_booking_data)
        assert update_booking.status_code == 403, "Доступ к запрошенному ресурсу разрешен"

        # Проверка с поддельным токеном
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token=faketoken555"}
        update_booking = requests.patch(f"{BASE_URL}/booking/{booking_id}", headers=headers, json=partial_booking_data)
        assert update_booking.status_code == 403, "Доступ к запрошенному ресурсу разрешен"

        update_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=partial_booking_data)
        assert update_booking.status_code == 200

        booking_data_response = update_booking.json()
        assert booking_data_response['firstname'] == partial_booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == partial_booking_data['lastname'], "Фамилия не совпадает с заданной"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
