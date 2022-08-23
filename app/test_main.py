import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def test_products():
    return[
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today,result",
    [
        pytest.param(
            datetime.date(2022, 1, 1),
            [],
            id="all ok"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
            [],
            id="all ok in day of expire"
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            ["duck"],
            id="expired at 02.02.2022"),
        pytest.param(
            datetime.date(2022, 2, 6),
            ["chicken", "duck"],
            id="expired at 06.02.2022"
        ),
        pytest.param(
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
            id="all expired"
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(mocked_today, today, result, test_products):
    mocked_today.today.return_value = today
    assert outdated_products(test_products) == result
