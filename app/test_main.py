import datetime
import pytest
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, expected",
    [
        pytest.param(
            datetime.date(2025, 4, 6),
            ["chicken"],
            id="one item expired"
        ),
        pytest.param(
            datetime.date(2025, 5, 2),
            ["chicken", "duck"],
            id="test item just expired"
        ),
        pytest.param(
            datetime.date(2025, 10, 10),
            ["chicken", "duck"],
            id="test for last day"
        ),
        pytest.param(
            datetime.date(2025, 10, 11),
            ["salmon", "chicken", "duck"],
            id="test for every product expired",
        ),
        pytest.param(
            datetime.date(2025, 1, 11),
            [],
            id="test for every product is OK"
        ),
    ]
)
def test_outdated_products(today: datetime.date, expected: list) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 10, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 4, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 5, 1),
            "price": 160
        },
    ]
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products) == expected
