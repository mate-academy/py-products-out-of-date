import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products_with_mixed_expiration_dates(
    mock_datetime: MagicMock,
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2026, 9, 27)

    products = [
        {"name": "bread", "expiration_date": datetime.date(2026, 9, 20)},
        {"name": "cheese", "expiration_date": datetime.date(2026, 9, 27)},
        {"name": "butter", "expiration_date": datetime.date(2026, 10, 5)},
    ]

    tovar = outdated_products(products)
    assert tovar == ["bread"]


@patch("app.main.datetime")
def test_oudated_products_when_expiration_date_is_yesterday(
    mock_datetime: MagicMock,
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2026, 9, 27)
    products = [
        {"name": "carrot", "expiration_date": datetime.date(2026, 9, 26)},
    ]
    new_tovar = outdated_products(products)
    assert new_tovar == ["carrot"]
