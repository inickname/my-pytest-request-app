from typing import Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker()


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingDataModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

    @staticmethod
    def create_booking_data():
        return BookingDataModel(
            firstname=faker.first_name(),
            lastname=faker.last_name(),
            totalprice=faker.random_int(min=100, max=10000),
            depositpaid=True,
            bookingdates=BookingDates(checkin="2024-04-05", checkout="2024-04-08"),
            additionalneeds="Breakfast"
        )
