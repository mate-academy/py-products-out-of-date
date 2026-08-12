import pytest
from unittest import mock


from app.main import outdated_products, datetime


@pytest.mark.parametrize(
    "products, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                }
            ],
            datetime.date(2022, 1, 10),
            [],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                }
            ],
            datetime.date(2022, 2, 10),
            [],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                }
            ],
            datetime.date(2022, 3, 10),
            ["salmon"],
        ),
    ],
    ids=[
        "date is not expired",
        "today is the last day",
        "product already expired",
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mock_today_date: mock.MagicMock,
    products: list[dict],
    today_date: datetime.date,
    expected: list[dict],
) -> None:
    mock_today_date.date.today.return_value = today_date
    assert outdated_products(products) == expected
