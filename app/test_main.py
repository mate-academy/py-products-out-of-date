import datetime

from pytest_mock import MockerFixture
from app import main


def test_outdated_products(mocker: MockerFixture) -> None:
    real_date = datetime.date

    mocked_date = mocker.patch("app.main.datetime.date")
    mocked_date.today.return_value = real_date(2022, 2, 2)
    mocked_date.side_effect = real_date

    products = [
        {
            "name": "salmon",
            "expiration_date": real_date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 2, 2),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": real_date(2022, 2, 1),
            "price": 160,
        },
    ]

    assert main.outdated_products(products) == ["duck"]
