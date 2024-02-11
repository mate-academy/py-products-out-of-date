import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    ("products", "expected_result"),
    [
        ([
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
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ], ["duck"])
    ],
    ids=[
        "Should return ['duck'] when expiratuion_date has passed"
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mock_datetime: mock.MagicMock,
    products: list,
    expected_result: list
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected_result
