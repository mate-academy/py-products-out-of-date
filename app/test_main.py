import pytest
from unittest import mock


from app.main import outdated_products


PRODUCT_LIST = [
    {
        "name": "salmon",
        "expiration_date": 1,
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": 1,
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": 0,
        "price": 160
    }
]


@pytest.mark.parametrize(
    "product_list,today_value,result",
    [
        pytest.param(
            [],
            1,
            [],
            id="Should return the empty list if product list is empty"
        ),
        pytest.param(
            PRODUCT_LIST,
            1,
            ["duck"],
            id="Should return only outdated products"
        )
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mock_date: callable,
        product_list: list,
        today_value: int,
        result: list
) -> None:
    mock_date.today.return_value = today_value
    assert outdated_products(product_list) == result
