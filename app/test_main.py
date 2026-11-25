import datetime
import pytest
from unittest import mock


from app import main


product_list = [
    {
        "name": "item 1",
        "expiration_date": datetime.date(2026, 12, 31)
    },
    {
        "name": "item 2",
        "expiration_date": datetime.date(2027, 6, 30)
    },
    {
        "name": "item 3",
        "expiration_date": datetime.date(2028, 2, 29)
    }
]


@pytest.mark.parametrize(
    "mocked_date, expired_product", [
        pytest.param(datetime.date(2026, 1, 24),
                     [],
                     id="Today, no product expired."),
        pytest.param(datetime.date(2026, 12, 31),
                     [],
                     id="At year end, no product expired."),
        pytest.param(datetime.date(2027, 1, 1),
                     ["item 1"],
                     id="At New Year, one product expired."),
        pytest.param(datetime.date(2027, 6, 30),
                     ["item 1"],
                     id="At 30th June, one product expired."),
        pytest.param(datetime.date(2027, 7, 1),
                     ["item 1", "item 2"],
                     id="At July 1st, two products expired."),
        pytest.param(datetime.date(2028, 2, 29),
                     ["item 1", "item 2"],
                     id="At February 29th, two products expired."),
        pytest.param(datetime.date(2028, 3, 1),
                     ["item 1", "item 2", "item 3"],
                     id="At march, 1st, all products expired.")
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date_function: mock.Mock,
                           mocked_date: datetime.date,
                           expired_product: list[str | None]) -> None:
    mocked_date_function.date.today.return_value = mocked_date
    assert main.outdated_products(product_list) == expired_product
