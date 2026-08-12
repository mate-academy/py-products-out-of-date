import datetime
import pytest
from app.main import outdated_products
from unittest import mock


@pytest.mark.parametrize(
    "test_data, expected_result, test_date",
    [
        (
            [
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
            ],
            ["duck"],
            datetime.date(2021, 2, 10)
        ),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock,
                           test_data: list[dict],
                           expected_result: list,
                           test_date: datetime.date
                           ) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(test_data) == expected_result
