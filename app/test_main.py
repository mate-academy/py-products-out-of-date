from unittest import mock
import datetime
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "product, today_date, expected",
    [
        (
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 1),
            },
            datetime.date(2022, 2, 1),
            []
        ),
        (
            {
                "name": "duck",
                "expiration_date": datetime.date(2024, 5, 1),
            },
            datetime.date(2024, 5, 2),
            ["duck"]
        )

    ]
)
def test_outdated_products(
        product: dict,
        today_date: datetime.date,
        expected: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = today_date
        print(type(today_date))
        assert outdated_products([product]) == expected
