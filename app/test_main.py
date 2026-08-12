from unittest import mock
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 12, 22),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 12, 20),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 12, 19),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_check_correct_result(
        mocked_date: mock.MagicMock,
        products: list[dict]
) -> None:
    mocked_date.date.today.return_value = datetime.date(2024, 12, 20)
    mocked_date.side_effect = datetime.date
    assert outdated_products(products) == ["duck"]
