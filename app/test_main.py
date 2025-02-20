from datetime import date
from unittest.mock import patch

from app.main import outdated_products


def test_return_outdated_product_name() -> None:
    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        result = outdated_products([
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ])
        assert result == ["duck"]
