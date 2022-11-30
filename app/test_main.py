from freezegun import freeze_time
import datetime
from app.main import outdated_products


@freeze_time("2022-2-2")
def test_without_products_out_date() -> None:
    list_goods = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ]
    assert outdated_products(list_goods) == []


@freeze_time("2022-2-2")
def test_products_with_today_date() -> None:
    list_goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        }
    ]
    assert outdated_products(list_goods) == []


@freeze_time("2022-2-2")
def test_products_with_yesterday_date() -> None:
    list_goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120
        }
    ]
    assert outdated_products(list_goods) == ["chicken"]
