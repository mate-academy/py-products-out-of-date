import datetime

from freezegun import freeze_time

from app.main import outdated_products


@freeze_time("2022-02-02")
def test_first_basket_with_products() -> None:
    assert outdated_products([
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
    ]) == ["duck"]


@freeze_time("2020-12-17")
def test_second_basket_with_products() -> None:
    assert outdated_products([
        {
            "name": "sardine",
            "expiration_date": datetime.date(2020, 12, 17),
            "price": 60
        },
        {
            "name": "yoghurt",
            "expiration_date": datetime.date(2020, 12, 15),
            "price": 40
        },
        {
            "name": "tuna",
            "expiration_date": datetime.date(2020, 2, 1),
            "price": 100
        }
    ]) == ["yoghurt", "tuna"]


@freeze_time("2021-07-05")
def test_third_basket_with_products() -> None:
    assert outdated_products([
        {
            "name": "beef",
            "expiration_date": datetime.date(2021, 3, 3),
            "price": 300
        },
        {
            "name": "pork",
            "expiration_date": datetime.date(2021, 5, 22),
            "price": 200
        },
        {
            "name": "ice cream",
            "expiration_date": datetime.date(2021, 7, 1),
            "price": 50
        }
    ]) == ["beef", "pork", "ice cream"]
