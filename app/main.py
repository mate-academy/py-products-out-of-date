import datetime


def get_today() -> datetime:
    return datetime.date.today()


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < get_today()]
