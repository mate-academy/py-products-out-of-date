import pytest
from unittest import mock
from app.main import outdated_products
import datetime


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 11)
                }
            ],
            [],
            id="expiration day today not outdated"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 10)
                }
            ],
            ["chicken"],
            id="expiration day yesterday outdated"
        ),
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 12)
                }
            ],
            [],
            id="expiration day tomorrow not outdated"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_list_with_products_are_correctly(
        mocked_data: mock.MagicMock,
        products: list[dict],
        expected: list[str]
) -> None:
    mocked_data.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(products) == expected
