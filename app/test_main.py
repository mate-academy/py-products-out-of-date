from unittest.mock import patch

from app.main import outdated_products
import pytest
import datetime


@pytest.mark.parametrize(
    "input_list, output_list",
    [
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5)},
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 1)}
            ],
            ["duck"],
        )
    ]
)
def test_check_date_products(input_list: list,
                             output_list: list) -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 4)
        assert outdated_products(input_list) == output_list
