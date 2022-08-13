import datetime

from app.main import outdated_products


def test_should_return_empty_list_if_products_actual_dates():
    products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 8, 13),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 8, 13),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 8, 13),
        "price": 160
    }
]
    assert outdated_products(products) == []


def test_should_return_list_with_spoiled_products_if_it_out_of_dates():
    spoiled_products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 8, 12),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 8, 12),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 9, 1),
        "price": 160
    }
]
    assert outdated_products(spoiled_products) == ['salmon', 'chicken']


def test_should_return_empty_list_if_products_out_of_dates():
    all_spoiled_products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 7, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 7, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 7, 1),
            "price": 160
        }
    ]
    assert len(outdated_products(all_spoiled_products)) == len(all_spoiled_products)
