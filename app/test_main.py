import pytest
from unittest.mock import patch
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today_date, expected_names",
    [
        (
            [
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 1)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 2)},
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 5)},
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),

        (
            [
                {"name": "apple",
                 "expiration_date": datetime.date(2022, 3, 1)},
            ],
            datetime.date(2022, 2, 2),
            [],
        ),

        (
            [],
            datetime.date(2022, 2, 2),
            [],
        ),
    ],
    ids=[
        "mixed_products",
        "all_fresh",
        "empty_list"
    ]
)
def test_outdated_products(products: list,
                           today_date: datetime.date,
                           expected_names: list) -> None:
    with patch("app.main.datetime.date") as mocked_date:
        mocked_date.today.return_value = today_date

        result = outdated_products(products)

        assert result == expected_names
