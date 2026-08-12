from unittest import mock
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
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


@pytest.mark.parametrize(
    "value,expect_result",
    [
        (
            datetime.date(2023, 5, 20),
            ["salmon", "chicken", "duck"],
        ),
        (
            datetime.date(2022, 2, 5),
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 6),
            ["chicken", "duck"],
        )
    ]
)
@mock.patch("datetime.date")
def test_(mock_datetime: mock,
          value: datetime,
          expect_result: list,
          products: list) -> None:
    mock_datetime.today.return_value = value
    assert outdated_products(products) == expect_result
