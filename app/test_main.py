import pytest

from unittest import mock
import datetime


from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result",
    [
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2026, 7, 15),
                    "price": 200,
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2026, 7, 19),
                    "price": 50,
                },
                {
                    "name": "pineapples",
                    "expiration_date": datetime.date(2026, 7, 10),
                    "price": 120,
                },
            ],
            [
                "duck", "pineapples",
            ],
            id="Should return list of outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 7, 25),
                    "price": 400,
                },
                {
                    "name": "yoghurt",
                    "expiration_date": datetime.date(2026, 8, 10),
                    "price": 40,
                },
                {
                    "name": "apple juice",
                    "expiration_date": datetime.date(2027, 3, 17),
                    "price": 150,
                },
            ],
            [],
            id="Should return empty list if all products not outadated"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 7, 18),
                    "price": 400,
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2026, 7, 18),
                    "price": 80,
                },
            ],
            [],
            id="Should return empty list if all priducts will be otdated today"
        ),
        pytest.param(
            [
                {
                    "name": "fish",
                    "expiration_date": datetime.date(2026, 7, 17),
                    "price": 130,
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2026, 7, 17),
                    "price": 90,
                },
            ],
            ["fish", "cheese"],
            id="SHould return name of products which outdated yesterday"
        )
    ]
)
def test_function_wroking_correctly(
    products: list,
    result: list
) -> None:
    date_today = datetime.date
    with mock.patch("app.main.datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = date_today(2026, 7, 18)
        assert outdated_products(products) == result
