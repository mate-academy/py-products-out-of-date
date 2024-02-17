from unittest import mock
import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "test_data,data_today,test_result",
    [
        pytest.param([
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
            }],
            datetime.date(2022, 2, 2),
            ["duck"],
            id="Test function outdated_products with mock_date += 1 day"),
        pytest.param([
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
            }],
            datetime.date(2022, 2, 1),
            [],
            id="Test function outdated_products with mock_date = today")

    ]
)
def test_function_outdated_products_with_mock(test_data: list,
                                              data_today: None,
                                              test_result: list) -> None:
    with mock.patch("app.main.datetime.date") as mocked_date_today:
        mocked_date_today.today.return_value = data_today
        assert outdated_products(test_data) == test_result
