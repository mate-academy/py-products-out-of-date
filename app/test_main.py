import pytest
import datetime
from unittest.mock import patch
import app.main


@pytest.fixture()
def products_template() -> list:
    products = [
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
    return products


@pytest.mark.parametrize(
    "mock_datetime_today,result",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ],
    ids=[
        "No expired products at 01/02/2022",
        "Duck is expired at 02/02/2022",
        "Chicken and duck are expired at 06/02/2022",
        "Salmon, chicken and duck are expired at 11/02/2022"
    ]
)
@patch("datetime.date")
def test_outdated_products(mock_datetime: callable,
                           mock_datetime_today: tuple,
                           result: list,
                           products_template: list) -> None:
    mock_datetime.today.return_value = mock_datetime_today
    assert app.main.outdated_products(products_template) == result
