import datetime
from unittest.mock import patch
import pytest
from app.main import outdated_products

SAMPLE_PRODUCTS = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "mocked_today,expected_names",
    [
        pytest.param(
            datetime.date(2022, 2, 2),
            ["duck"],
            id="One product is outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
            [],
            id="All products are within the expiration date"
        ),
        pytest.param(
            datetime.date(2022, 2, 6),
            ["chicken", "duck"],
            id="More then one product is outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
            id="All products are outdated"
        ),
    ]
)
def test_outdated_products(
        mocked_today: datetime.date,
        expected_names: list[str]
) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = mocked_today
        assert outdated_products(SAMPLE_PRODUCTS) == expected_names
