import datetime
import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "products, expected_products",
    [
        (
            [{"name": "meat", "expiration_date": datetime.date(2022, 2, 5)}],
            ["meat"]
        ),
        (
            [{"name": "fish", "expiration_date": datetime.date(2022, 2, 10)}],
            []
        ),
        (
            [{"name": "duck", "expiration_date": datetime.date(2022, 2, 7)}],
            []
        ),
        (
            [
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 5)},
                {"name": "fish", "expiration_date": datetime.date(2022, 2, 3)},
                {"name": "meat", "expiration_date": datetime.date(2022, 2, 2)}
            ],
            ["duck", "fish", "meat"]
        ),
        (
            [
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 8)},
                {"name": "fish", "expiration_date": datetime.date(2022, 2, 3)},
                {"name": "meat", "expiration_date": datetime.date(2022, 2, 12)}
            ],
            ["fish"]
        ),
        ([], [])
    ],
    ids=[
        "outdated product test",
        "fresh product test",
        "expiration date is the today date",
        "all products is outdated",
        "mixed outdated and fresh products",
        "empty lists"
    ]
)
def test_outdated_products(
        mock_datetime: MagicMock,
        products: list[dict],
        expected_products: list
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 7)
    result = outdated_products(products)

    assert result == expected_products
