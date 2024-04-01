import pytest
import datetime

from unittest import mock

from app.main import outdated_products


class TestOutdatedProducts:

    @pytest.fixture
    def mocked_datetime(self) -> mock.MagicMock:
        with mock.patch("app.main.datetime") as mocked_datetime:
            mocked_datetime.date.today.return_value = datetime.date(2024, 4, 1)
            return mocked_datetime

    @pytest.fixture
    def products(self) -> list:
        return [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2024, 4, 1),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2024, 4, 5),
                "price": 120,
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2024, 3, 31),
                "price": 160,
            },
        ]

    def test_should_return_correct_result(
        self,
        products: list,
        mocked_datetime: mock.MagicMock
    ) -> None:
        assert outdated_products(products) == ["duck"]
