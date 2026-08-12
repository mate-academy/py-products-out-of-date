import pytest
import datetime

from freezegun import freeze_time
from app.main import outdated_products


@pytest.fixture(scope="module")
def products() -> list:
    return [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600
         },
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120
         },
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160
         },
        {"name": "milk",
         "expiration_date": datetime.date(2022, 2, 4),
         "price": 50
         },
    ]


@freeze_time("2022-02-05")
def test_outdated_products(products: list) -> None:
    result = outdated_products(products)
    assert set(result) == {"duck", "milk"}
