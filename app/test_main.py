import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: datetime, ) -> None:
    # Set today's date to 2022-02-02
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    # Test with a list of products
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

    # Call the function and check the result
    result = outdated_products(products)
    assert result == ["duck"]


@patch("app.main.datetime")
def test_outdated_products_empty_list(mock_datetime: datetime) -> None:
    # Set today's date to 2022-02-02
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    # Test with an empty list of products
    products = []

    # Call the function and check the result
    result = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_outdated_products_no_outdated(mock_datetime: datetime) -> None:
    # Set today's date to 2022-02-02
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    # Test with a list of products where none are outdated
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 15),
            "price": 120
        }
    ]

    # Call the function and check the result
    result = outdated_products(products)
    assert result == []

# Add more tests as needed for other scenarios or edge cases
