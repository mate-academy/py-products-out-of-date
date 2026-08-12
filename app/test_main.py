import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
    [
        pytest.param(
            [{"name": "salmon", "expiration_date": datetime.date(2022, 2, 1)}],
            ["salmon"], id="if expiration date "
                           "equals yesterday product is outdated"),
        pytest.param(
            [{"name": "salmon", "expiration_date": datetime.date(2022, 2, 2)}],
            [], id="if expiration date equals today product is not outdated")
    ]
)
def test_outdated_products(products: list, result: list) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == result
