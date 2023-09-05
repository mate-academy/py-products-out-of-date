# write your code here
import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_list",
    [
        pytest.param(
            [{
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            }],
            [],
            id="Test when date is OK"
        ),
        pytest.param(
            [{
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            }],
            [],
            id="Test when date is today"
        ),
        pytest.param(
            [{
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }],
            ["duck"],
            id="Test when expiration was yesterday"
        )
    ]
)
def test_outdated_products(
        monkeypatch: pytest.MonkeyPatch,
        products: dict,
        expected_list: list
) -> None:
    date = datetime.date(2022, 2, 2)

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date
        assert outdated_products(products) == expected_list
