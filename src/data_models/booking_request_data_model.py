from typing import Optional

from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingDataModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates  # dict[str, str]
    additionalneeds: Optional[str] = None
