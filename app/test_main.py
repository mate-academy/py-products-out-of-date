import datetime
from app.main import outdated_products
import pytest
from unittest import mock


@pytest.fixture()
def mock_datetime():
    with mock.patch("app.main.datetime") as date_today:
        yield date_today


class TestOutdatedProducts:

    test_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        }
    ]

    @pytest.mark.parametrize(
        "data_time,result",
        [
            pytest.param(datetime.date(2022, 1, 1), [],
                         id="no one is out of date"),
            pytest.param(datetime.date(2022, 2, 7), ["chicken", "duck"],
                         id="two is out of date"),
            pytest.param(datetime.date(2022, 3, 2), [
                "salmon",
                "chicken",
                "duck"
            ],
                id="three is out of date")
        ]
    )
    def test_outdated_products(self, data_time, result, mock_datetime):
        mock_datetime.date.today.return_value = data_time
        assert outdated_products(self.test_list) == result
