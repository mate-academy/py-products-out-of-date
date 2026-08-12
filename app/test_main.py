from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock.MagicMock) -> None:
    mocked_datetime.date.side_effect = [10, 24, 30]
    mocked_datetime.date.today.return_value = 25

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": mocked_datetime.date(),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": mocked_datetime.date(),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": mocked_datetime.date(),
            "price": 160
        }
    ]) == ["salmon", "chicken"]
