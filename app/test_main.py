import pytest
from datetime import date
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "today,expected_result",
    [
        (date(2022, 1, 13), []),
        (date(2022, 2, 27), ["salmon", "chicken", "duck"]),
        (date(2022, 2, 1), []),
        (date(2022, 2, 2), ["duck"]),
        (date(2022, 2, 7), ["chicken", "duck"]),
    ]
)
@mock.patch("datetime.date")
def test_values(
        mocked_date: mock.MagicMock,
        today: date,
        expected_result: list[str]
) -> None:
    mocked_date.today.return_value = today

    products = [
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
    ]

    assert outdated_products(products) == expected_result

    assert len(mocked_date.today.mock_calls) == len(products)
