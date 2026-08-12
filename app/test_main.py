import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "name,date,result",
    [
        ("salmon", datetime.date(2022, 2, 10), []),
        ("chicken", datetime.date(2022, 2, 3), []),
        ("duck", datetime.date(2022, 2, 1), ["duck"]),
    ]
)
@mock.patch('app.main.datetime')
def test_outdated_products(mocked_datetime, name, date, result):
    product_list = [{"name": name, "expiration_date": date}]
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == result
