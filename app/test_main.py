import datetime
from unittest.mock import patch
from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> "MockDate":
        return cls(2022, 2, 2)


@patch("app.main.datetime.date", MockDate)
def test_one_outdated_product() -> None:
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
    assert outdated_products(products) == ["duck"]


@patch(
    "app.main.datetime.date",
    new_callable=lambda: type(
        "MockDate",
        (datetime.date,),
        {
            "today": classmethod(lambda cls: cls(2022, 2, 11))
        }
    )
)
def test_all_products_outdated(mock_date: type) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": mock_date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": mock_date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": mock_date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@patch(
    "app.main.datetime.date",
    new_callable=lambda: type(
        "MockDate",
        (datetime.date,),
        {
            "today": classmethod(lambda cls: cls(2022, 1, 1))
        }
    )
)
def test_no_products_outdated(mock_date: type) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": mock_date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": mock_date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": mock_date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == []


@patch(
    "app.main.datetime.date",
    new_callable=lambda: type(
        "MockDate",
        (datetime.date,),
        {
            "today": classmethod(lambda cls: cls(2022, 2, 2))
        }
    )
)
def test_empty_product_list(mock_date: type) -> None:
    assert outdated_products([]) == []


@patch(
    "app.main.datetime.date",
    new_callable=lambda: type(
        "MockDate",
        (datetime.date,),
        {
            "today": classmethod(lambda cls: cls(2022, 2, 5))
        }
    )
)
def test_product_expires_today(mock_date: type) -> None:
    products = [
        {
            "name": "chicken",
            "expiration_date": mock_date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": mock_date(2022, 2, 4),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["duck"]
