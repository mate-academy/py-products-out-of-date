import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date(2022, 2, 2)]
