import datetime
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "data, result, message", [
        ([{"name": "salmon",
           "expiration_date": datetime.date(2023, 6, 27),
           "price": 600
           }],
         [],
         "If date is today, product is not out."),
        ([{"name": "pork",
           "expiration_date": datetime.date(2023, 6, 26),
           "price": 600}],
         ["pork"],
         "If date is today, product is not out.")]
)
def test_outdated_products(
        data: list,
        result: list,
        message: str,
) -> None:

    assert outdated_products(data) == result, message
