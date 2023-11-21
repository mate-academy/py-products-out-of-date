import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "value, result",
    [
        pytest.param([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            }], ["salmon"], id="test_expired"),
        pytest.param([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 11, 20),
                "price": 600
            }], ["salmon"], id="yesterday_expired"),
        pytest.param([
            {
                "name": "chicken",
                "expiration_date": datetime.date(2024, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2023, 11, 21),
                "price": 160
            }], [], id="today_and_future_not_expired")])
def test_product_date_expired(value: list[dict], result: list) -> None:
    mock_today = datetime.date(2023, 11, 21)
    with mock.patch("datetime.date",
                    mock.Mock(today=mock.Mock(return_value=mock_today))):
        assert outdated_products(value) == result
