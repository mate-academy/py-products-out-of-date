import datetime


def get_today_date() -> datetime.date:
    return datetime.date.today()


def outdated_products(products: list) -> list:
    today = get_today_date()
    return [
        product["name"] for product in products
        if product["expiration_date"] < today
    ]
