from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class Headers(Enum):
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
