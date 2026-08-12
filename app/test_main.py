import pytest
import datetime
from unittest.mock import patch, Mock

from app.main import outdated_products


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


@pytest.mark.parametrize(
    "today_date,result",
    [
        (datetime.date(2022, 1, 25), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
    ]
)
@patch("app.main.datetime")
def test_outdated_product(
        mocked_date: Mock,
        today_date: datetime.date,
        result: list[str]
) -> None:
    mocked_date.date.today.return_value = today_date

    func_result = outdated_products(products)

    assert func_result == result
