import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
    yield [
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
    "date, result",
    [
        (
            datetime.date(2022, 2, 2), ["duck"]
        ),
        (
            datetime.date(2022, 4, 2), ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 6), ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 1), []
        ),
        (
            datetime.date(2022, 2, 5), ["duck"]
        ),
        (
            datetime.date(2022, 2, 10), ["chicken", "duck"]
        ),
    ]
)
@mock.patch("datetime.date")
def test_return_list_outdated_products(
        mock_date: mock.Mock,
        products_template: list[dict],
        date: datetime.date,
        result: list[str]
) -> None:
    mock_date.today.return_value = date

    assert outdated_products(products_template) == result
