import datetime
from unittest.mock import patch

import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        ([
             {
                 "name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600
             }
         ],
         []
         ),
        ([
             {
                 "name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120
             }
         ],
         []
         ),
        ([
             {
              "name": "duck",
              "expiration_date": datetime.date(2022, 2, 1),
              "price": 160
             }
         ],
         ["duck"]
         ),
    ]
)
def test_outdated_products(products: list,
                           expected: list
                           ) -> None:
    with (patch("app.main.datetime") as mocked_date_today):
        mocked_date_today.date.today.return_value = datetime.date(2022, 2, 2)

        assert outdated_products(products) == expected
