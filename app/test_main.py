import datetime
import pytest


from unittest import mock


from app.main import outdated_products


@pytest.mark.parametrize(
    "mocker,thrown",
    [
        (
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 6),
            ["duck", "chicken"]
        ),
        (
            datetime.date(2022, 2, 12),
            ["duck", "chicken", "salmon"]
        )
    ]
)
def test_duck_should_be_outdated(
    mocker: datetime.date,
    thrown: list[str]
) -> None:
    products = [
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
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = mocker
        assert sorted(outdated_products(products)) == sorted(thrown)
