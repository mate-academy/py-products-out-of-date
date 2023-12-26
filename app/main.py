import datetime


def get_date() -> datetime.date:
    return datetime.date.today()


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < get_date()]
