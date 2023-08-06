from unittest import mock

import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products",
    [
        (
                [
                    {"name": "salmon",
                     "expiration_date": datetime.date(2022, 2, 10)
                     },
                    {"name": "chicken",
                     "expiration_date": datetime.date(2022, 2, 2)
                     },
                    {"name": "duck",
                     "expiration_date": datetime.date(2022, 2, 1)
                     }
                ]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_date,
        products: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
