import datetime

from .main import outdated_products
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "products, today, expected_list_result",
    [
        ([
         {
             "name": "apple",
             "expiration_date": datetime.date(2022, 11, 30),
         },
         {
             "name": "ananas",
             "expiration_date": datetime.date(2024, 11, 19),
         },
         {
             "name": "potatoes",
             "expiration_date": datetime.date(2023, 11, 19),
         },
         {
             "name": "tomatoes",
             "expiration_date": datetime.date(2023, 12, 28),
         },
         {
             "name": "cherry",
             "expiration_date": datetime.date(2023, 11, 20),
         },
         {
             "name": "banana",
             "expiration_date": datetime.date(2021, 7, 20),
         }
         ],
         datetime.date(2023, 11, 20),
         ["apple", "potatoes", "banana"]
         )
    ]
)
@mock.patch("datetime.date")  # today +
def test_outdated_products(
        mocked_datetime_today: mock,
        products: list[dict],
        today: datetime,
        expected_list_result: list[dict]
) -> None:
    mocked_datetime_today.today.return_value = today  #
    assert outdated_products(products) == expected_list_result
