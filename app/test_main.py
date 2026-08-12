import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today, result",
    [
        pytest.param([{"name": "salmon",
                       "expiration_date": datetime.date(2023, 3, 10),
                       "price": 600},
                      {"name": "chicken",
                       "expiration_date": datetime.date(2023, 5, 5),
                       "price": 120}], datetime.date(2023, 5, 6),
                     ["salmon", "chicken"],
                     id="test when one product is overdue"),
        pytest.param([{"name": "salmon",
                       "expiration_date": datetime.date(2023, 3, 10),
                       "price": 600},
                      {"name": "chicken",
                       "expiration_date": datetime.date(2023, 5, 6),
                       "price": 120}], datetime.date(2023, 5, 6), ["salmon"],
                     id="test when one product is overdue")
    ]
)
def test_should_return_correct_product(
        products: list,
        today: tuple,
        result: list) -> None:
    with mock.patch("datetime.date") as mocked_time:
        mocked_time.today.return_value = today
        assert outdated_products(products) == result
