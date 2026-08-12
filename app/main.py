import datetime


def outdated_products(products: list) -> list:
    for product in products:
        if product["expiration_date"] < datetime.date.today():
            return product["name"]
