from unittest.mock import MagicMock, patch
import datetime
import pytest
from app.main import outdated_products


@pytest.fixture
def products() -> list:
    return [
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
        },
    ]


@pytest.mark.parametrize(
    "mock_today_date, expected_names",
    [
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2000, 1, 1), []),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: MagicMock,
    mock_today_date: datetime.date,
    expected_names: list,
    products: list[dict],
) -> None:
    mock_date.today.return_value = mock_today_date
    mock_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)

    result = outdated_products(products)

    assert result == expected_names
