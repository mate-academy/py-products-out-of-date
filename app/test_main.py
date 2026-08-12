from app.main import outdated_products
from unittest import mock
import datetime
import pytest


class TestOutdatedProducts:

    @pytest.fixture
    def mocked_datetime(self) -> None:
        with mock.patch("app.main.datetime") as mocked_test_datetime:
            yield mocked_test_datetime

    def test_expect_list_of_outdated_products(
            self,
            mocked_datetime: mock.MagicMock
    ) -> None:

        mocked_datetime.date.today.return_value = datetime.date(2022, 2, 6)

        result = outdated_products([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 6),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ])

        assert result == ["duck"]
