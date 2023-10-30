import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]

# @mock.patch("app.main.datetime")
# def test_check_if_all_expired(mocked_time, products_template) -> None:
#     mocked_time.date.today.return_value = datetime.date(2023, 2, 3)
#     assert outdated_products(products_template) == ["salmon", "chicken", "duck"]