from enum import Enum


class Url(Enum):
    BASE_URL = "https://restful-booker.herokuapp.com"


def return_base_url(url: Url) -> str:
    return url.value


class Headers(Enum):
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def return_headers(api_headers: Headers) -> dict:
    return api_headers.value
