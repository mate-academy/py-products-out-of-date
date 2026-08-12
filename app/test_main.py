import pytest
from unittest import mock
from datetime import date
from app.main import outdated_products


@pytest.fixture()
def mock_datetime_today() -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        yield mocked_date


def test_expiration_date_today(mock_datetime_today: date) -> None:
    mock_datetime_today.date.today.return_value = date(2022, 2, 2)
    products = outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ])
    assert products == ["duck"]
