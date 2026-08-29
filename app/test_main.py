from app.main import outdated_products
from unittest import mock
from unittest.mock import MagicMock
import pytest
import datetime

_real_date = datetime.date


@pytest.fixture()
def template_product() -> list:
    return [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 28),
         "price": 600
         },
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 28),
         "price": 120
         },
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 25),
         "price": 160
         },
        {"name": "eel",
         "expiration_date": datetime.date(2022, 2, 26),
         "price": 200
         }

    ]


@mock.patch("app.main.datetime.date")
def test_data_time(mocked_date: MagicMock , template_product: list) -> None:
    mocked_date.today.return_value = _real_date(2022, 2, 26)
    assert outdated_products(template_product) == ["duck"]
