from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class Url(Enum):
    BASE_URL = "https://restful-booker.herokuapp.com"


class Headers(Enum):
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


class AuthData(Enum):
    AUTH_DATA = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
