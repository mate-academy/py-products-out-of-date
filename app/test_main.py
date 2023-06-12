from app.main import outdated_products
from unittest import mock
import pytest


class TestOutdatedProducts:

    @pytest.fixture
    def mocked_datetime(self) -> None:
        with mock.patch("datetime.date") as mocked_test_datetime:
            yield mocked_test_datetime

    def test_expect_list_of_outdated_products(
            self,
            mocked_datetime: mock.MagicMock
    ) -> None:

        mocked_datetime.today.return_value = "2022-02-08"

        result = outdated_products([
            {
                "name": "salmon",
                "expiration_date": "2022-02-10",
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": "2022-02-08",
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": "2022-02-01",
                "price": 160
            }
        ])

        assert result == ["duck"]
