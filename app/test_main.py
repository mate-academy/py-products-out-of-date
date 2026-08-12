import pytest
import datetime

from typing import Any
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def mock_datetime_today() -> Any:
    with mock.patch("app.main.datetime.date") as mocked_date:
        yield mocked_date


@pytest.mark.parametrize(
    "product_list, expirate_date, name_key",
    [
        (
            pytest.param(
                [{"name": "salmon",
                  "expiration_date": datetime.date(2022, 2, 1),
                  "price": 600}],
                datetime.date(2022, 2, 2),
                ["salmon"]
            )
        ),
        (
            pytest.param(
                [{"name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 600}],
                datetime.date(2022, 2, 2),
                []
            )
        ),
        (
            pytest.param(
                [{"name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 600}],
                datetime.date(2022, 2, 2),
                []
            )
        )
    ]
)
def test_outdates_products(
        mock_datetime_today: mock.MagicMock,
        product_list: list[dict],
        expirate_date: datetime.date,
        name_key: list[str]) -> None:
    mock_datetime_today.today.return_value = expirate_date
    result = outdated_products(product_list)
    assert result == name_key
