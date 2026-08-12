import datetime
import pytest
from unittest import mock

from app.main import outdated_products


class MockedDate(datetime.date):
    pass


@pytest.fixture()
def product_list() -> list[dict]:
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
    "year,month,day,expected",
    [
        (2022, 2, 1, []),
        (2022, 2, 2, ["duck"]),
        (2022, 2, 6, ["chicken", "duck"]),
        (2022, 2, 11, ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("datetime.date", MockedDate)
def test_products_out_of_date(
    product_list: list[dict],
    year: int,
    month: int,
    day: int,
    expected: list[str]
) -> None:
    MockedDate.today = classmethod(lambda cls: datetime.date(year, month, day))
    assert outdated_products(product_list) == expected
