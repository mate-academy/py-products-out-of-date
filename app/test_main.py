import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected,",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 3, 12),
                }
            ],
            [],
            id="should not add to list if data is more than today"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 3, 11),
                }
            ],
            [],
            id="should not add to list if date is today",
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 3, 10),
                }
            ],
            "salmon",
            id="should add to list if data is less than today",
        )
    ]
)
@mock.patch("app.main.datetime.date.today")
def test_modify_expiration_date(
        mocked_date_today: type,
        products: list[dict],
        expected: str
) -> None:

    mocked_date_today.return_value = datetime.date(2026, 3, 11)
    assert outdated_products(products) == [expected]
