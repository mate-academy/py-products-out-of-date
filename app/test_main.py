from unittest import mock
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": 2022210,
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": 2022205,
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": 2022201,
                    "price": 160
                }
            ],
            ["duck"], id="test_when_in_result_only_one_product_is_returned"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": 2022210,
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": 2022215,
                    "price": 160
                }
            ],
            [], id="test_when_in_result_no_product_is_returned"
        )
    ])
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: object,
                           products: list[dict],
                           expected_result: list[str]) -> None:
    mock_datetime.date.today.return_value = 2022202
    result = outdated_products(products)
    assert result == expected_result
