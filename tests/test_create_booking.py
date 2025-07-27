from src.api.booking_api_client import BookingApiClient
from src.scenarios.booking_scenarios import BookingScenarios
from tests.conftest import auth_session


class TestBookings:
    def test_get_and_verify_bookings_exist(self, auth_session):
        booking_api_client = BookingApiClient(auth_session)
        booking_scenarios = BookingScenarios(booking_api_client)
        booking_scenarios.get_and_verify_bookings_exist()

    def test_create_booking_check_and_delete(self, auth_session, booking_data):
        booking_api_client = BookingApiClient(auth_session)
        booking_scenarios = BookingScenarios(booking_api_client)
        booking_scenarios.create_booking_check_and_delete(booking_data)

    def test_update_booking_and_verify_changes(self, auth_session, booking_data):
        booking_api_client = BookingApiClient(auth_session)
        booking_scenarios = BookingScenarios(booking_api_client)
        booking_scenarios.update_booking_and_verify_changes(booking_data)

    def test_partial_update_booking_and_verify_changes(self, auth_session, booking_data):
        booking_api_client = BookingApiClient(auth_session)
        booking_scenarios = BookingScenarios(booking_api_client)
        booking_scenarios.partial_update_booking_and_verify_changes(booking_data)

    def test_delete_existing_booking_and_verify(self, auth_session, booking_data):
        booking_api_client = BookingApiClient(auth_session)
        booking_scenarios = BookingScenarios(booking_api_client)
        booking_scenarios.delete_existing_booking_and_verify(booking_data)
