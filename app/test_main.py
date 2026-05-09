import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    fixed_today = datetime.date(2022, 2, 2)

    with patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = fixed_today
        mocked_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 1)
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2)
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 10)
            }
        ]

        result = outdated_products(products)
        assert result == ["salmon"]
