import datetime


def outdated_products(products: list) -> list:
    print("Inside function", datetime.date.today())
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
