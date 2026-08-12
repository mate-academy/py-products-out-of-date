from app.main import outdated_products
import datetime
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "today,products,result",
    [
        (datetime.date(2022, 2, 2),
         [
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
             }],
         ["duck"]
         ),
        (datetime.date(2022, 2, 14),
         [
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
                 "expiration_date": datetime.date(2022, 2, 15),
                 "price": 160
             }],
         ["salmon", "chicken"]
         ),
        (datetime.date(2022, 2, 2),
         [
             {
                 "name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600
             },
             {
                 "name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 2),
                 "price": 120
             },
             {
                 "name": "duck",
                 "expiration_date": datetime.date(2022, 2, 15),
                 "price": 160
             }],
         []
         )
    ],
    ids=[
        "For 'duck' expiration date out the date",
        "For 'salmon', and 'chicken' expiration date out the date",
        "All products are fresh",
    ]
)
def test_outdated_products(
        today: datetime,
        result: list,
        products: list[dict],
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(products) == result
