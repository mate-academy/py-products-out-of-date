import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    test_product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 3, 3),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 3, 2),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 2, 1),
        }
    ]
    expected_output = ["chicken", "duck"]

    faked_today = datetime.date(2023, 3, 3)
    with patch("datetime.date") as mock_datetime_date:
        mock_datetime_date.today.return_value = faked_today

        assert outdated_products(test_product_list) == expected_output
