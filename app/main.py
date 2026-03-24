import datetime


def outdated_products(products: dict) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
