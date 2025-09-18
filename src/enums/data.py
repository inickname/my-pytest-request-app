from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class AuthData(Enum):
    AUTH_DATA = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
