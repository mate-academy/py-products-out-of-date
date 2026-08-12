import pytest
from datetime import date

from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "data_today, expected_result",
    [
        ((2022, 2, 4), []),
        ((2022, 2, 5), []),
        ((2022, 2, 11), ["salmon", "chicken"]),
    ]
)
def test_outdated_products(
        data_today: tuple,
        expected_result: str
) -> None:
    animal_list = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        }
    ]
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(*data_today)
        assert outdated_products(animal_list) == expected_result
