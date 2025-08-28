from enum import Enum


class Url(Enum):
    BASE_URL = "https://restful-booker.herokuapp.com"


class Headers(Enum):
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


class AuthData(Enum):
    AUTH_DATA = {
        "username": "admin",
        "password": "password123"
    }
