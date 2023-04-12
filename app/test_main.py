import pytest
import datetime
from unittest import mock
import app.main


@pytest.fixture
def test_data() -> dict:
    current_date = [2022, 2, 9]
    products = [
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
    ]
    return {
        "current_date": current_date,
        "products": products,
        "expected_result": ["chicken", "duck"]
    }


def test_outdated_products(test_data: dict) -> None:
    current_date = test_data["current_date"]
    products = test_data["products"]
    expected_result = test_data["expected_result"]

    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_today = datetime.date(
            current_date[0],
            current_date[1],
            current_date[2]
        )
        mocked_datetime.date.today.return_value = mocked_today
        mocked_datetime.date = mock.Mock()
        mocked_datetime.date.today = mock.Mock(return_value=mocked_today)

        assert app.main.outdated_products(products) == expected_result
