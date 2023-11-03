import datetime
from app.main import outdated_products


def test_empty_products_list():
    products = []
    assert outdated_products(products) == []


def test_no_outdated_products():
    products = [
        {"name": "Product1", "expiration_date": datetime.date(2023, 12, 31)},
        {"name": "Product2", "expiration_date": datetime.date(2023, 10, 15)}
    ]
    assert outdated_products(products) == []


def test_some_outdated_products():
    products = [
        {"name": "Product1", "expiration_date": datetime.date(2022, 1, 1)},
        {"name": "Product2", "expiration_date": datetime.date(2023, 3, 15)},
        {"name": "Product3", "expiration_date": datetime.date(2022, 2, 1)}
    ]
    expected_result = ["Product1", "Product2", "Product3"]
    assert outdated_products(products) == expected_result


def test_all_outdated_products():
    products = [
        {"name": "Product1", "expiration_date": datetime.date(2021, 1, 1)},
        {"name": "Product2", "expiration_date": datetime.date(2020, 3, 15)}
    ]
    expected_result = ["Product1", "Product2"]
    assert outdated_products(products) == expected_result
