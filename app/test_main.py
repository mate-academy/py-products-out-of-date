import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today, expected",
    [
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5)},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 4)},
            ],
            datetime.date(2022, 2, 5),
            ["duck"],
        ),
    ],
)
def test_outdated_products(
        products: list[dict],
        today: datetime.date,
        expected: list[str]
) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        mock_date.side_effect = lambda *args, **kwargs:\
            datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == expected
