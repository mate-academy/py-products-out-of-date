import datetime
from unittest import mock
from app.main import outdated_products

import pytest

products_template = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 2),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "products_list, date_to_check, result",
    [
        pytest.param(
            products_template,
            datetime.date(2022, 2, 2),
            [],
            id="empty list"
        ),
        pytest.param(
            products_template,
            datetime.date(2022, 2, 6),
            ["chicken", "duck"],
            id="chicken and duck are outdated"
        ),
        pytest.param(
            products_template,
            datetime.date(2022, 2, 10),
            ["chicken", "duck"],
            id="chicken and duck are outdated"
        ),
    ]
)
def test_outdated_products(
        products_list: list,
        date_to_check: datetime.date,
        result: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date_to_check
        assert outdated_products(products_list) == result
