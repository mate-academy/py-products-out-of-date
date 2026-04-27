from datetime import date as real_date
from unittest import mock
from app.main import outdated_products


def test_out_products() -> None:
    with (mock.patch("app.main.datetime.date") as mocked_date):
        mocked_date.today.return_value = real_date(2022, 2, 2)
        mocked_date.side_effect = lambda *args, **kwargs: real_date(
            *args, **kwargs
        )

        assert outdated_products([
            {
                "name": "salmon",
                "expiration_date": real_date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": real_date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": real_date(2022, 2, 1),
                "price": 160
            },
            {
                "name": "fish",
                "expiration_date": real_date(2022, 2, 2),
                "price": 160
            },
            {
                "name": "pork",
                "expiration_date": real_date(2022, 2, 3),
                "price": 160
            },

        ]) == ["duck"]
