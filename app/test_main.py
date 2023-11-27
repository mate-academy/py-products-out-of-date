import datetime

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "product_expiration_date, today_date, result",
    [
        pytest.param(
            datetime.date(2022, 2, 10),
            datetime.date(2022, 2, 2),
            [],
            id="product is valid"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
            datetime.date(2022, 2, 2),
            ["Product1", "Product2"],
            id="product is expired"
        )
    ]
)
def test_outdated_products(
    product_expiration_date: datetime.date,
    today_date: datetime.date,
    result: list
) -> None:

    with(
        mock.patch("app.main.datetime")
        as mocked_datetime
    ):
        mocked_datetime.date.today.return_value = today_date

        products = [
            {
                "name": "Product1",
                "expiration_date": product_expiration_date
            },
            {
                "name": "Product2",
                "expiration_date": product_expiration_date
            },
        ]

        expected_result = outdated_products(products)
        assert expected_result == result
