from src.data_models.booking_request_data_model import BookingDataModel, BookingDates
from faker import Faker

faker = Faker()


class BookingData:
    @staticmethod
    def create_booking_data() -> BookingDataModel:
        return BookingDataModel(
            firstname=faker.first_name(),
            lastname=faker.last_name(),
            totalprice=faker.random_int(min=100, max=10000),
            depositpaid=True,
            bookingdates=BookingDates(checkin="2024-04-05", checkout="2024-04-08"),
            additionalneeds="Breakfast"
        )
