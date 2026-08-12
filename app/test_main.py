import pytest
import datetime
from app.main import outdated_products


overdue = datetime.date.today() - datetime.timedelta(days=1)
no_overdue = datetime.date.today() + datetime.timedelta(days=1)


@pytest.mark.parametrize(
    "incoming,expected",
    [
        pytest.param(
            [
                {"name": "a", "expiration_date": no_overdue, "price": 1},
                {"name": "b", "expiration_date": overdue, "price": 1},
            ],
            ["b"],
            id="",
        ),
        pytest.param(
            [{"name": "s", "expiration_date":
                datetime.date.today(), "price": 1}],
            [],
            id="",
        ),
    ],
)
def test_can_sum(incoming: list, expected: list) -> None:
    assert (
        outdated_products(incoming) == expected
    ), f"Result {outdated_products(incoming)} should be equal to {expected}"
