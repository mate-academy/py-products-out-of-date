import pytest
import datetime
from unittest import mock
import app.main


@pytest.mark.parametrize(
    "current_date, expected_result",
    [
        ((2021, 2, 1), []),
        ((2022, 2, 6), ["chicken", "duck"]),
        ((2023, 2, 21), ["salmon", "chicken", "duck"]),
    ]
)
def test_outdated_products(
        current_date: tuple[int],
        expected_result: list
) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date = mock.Mock()
        mocked_datetime.date.today = mock.Mock(
            return_value=datetime.date(*current_date)
        )
        assert app.main.outdated_products(
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
            ]
        ) == expected_result
