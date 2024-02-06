import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize("today_date, product_list, outdated_product", [
    (datetime.date.today(), [
        {"name": "salmon",
         "expiration_date": datetime.date(2024, 2, 5),
         "price": 600},
        {
            "name": "shrimp",
            "expiration_date": datetime.date(2024, 2, 6),
            "price": 540
        }
    ], ["salmon"]
    )
]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_datetime_date: mock.MagicMock,
                           today_date: datetime.date,
                           product_list: list,
                           outdated_product: list) -> None:
    mock_datetime_date.today.return_value = today_date
    assert outdated_products(product_list) == outdated_product
