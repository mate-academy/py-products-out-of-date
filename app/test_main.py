import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, product, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5)},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1)}
            ],
            ["duck"]
        )
    ]
)
def test_should_return_outdated_products(
        today: datetime.date,
        product: list,
        expected: list) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = today
        result = outdated_products(product)
    assert result == expected
