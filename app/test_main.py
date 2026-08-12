import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.outdated_products")
def test_time_on_time_and_out_of_time(
        mocked_datatime_today: mock
) -> None:

    mocked_datatime_today.return_value = datetime.date(
        datetime.date.today().year,
        datetime.date.today().month,
        datetime.date.today().day - 1
    )

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 12, 15),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 12, 15),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 12, 13),
            "price": 160
        }
    ]) == ["duck"]


def test_simple_variation() -> None:
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 12, 14),
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
        }]
    ) == ["chicken", "duck"]
