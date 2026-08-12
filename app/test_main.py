from app.main import outdated_products
from unittest.mock import patch
import datetime


def test_should_return_empty_list_if_exp_date_more_than_today() -> None:
    fake_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        assert outdated_products([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            }
        ]) == []


def test_should_return_name_if_exp_date_less_than_today() -> None:
    fake_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        assert outdated_products([
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]) == ["duck"]


def test_should_return_empty_list_if_exp_date_equal_today() -> None:
    fake_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        assert outdated_products([
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            }
        ]) == []
