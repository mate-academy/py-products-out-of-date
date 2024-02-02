import datetime


def outdated_products(products: list) -> list:
    d = datetime.date.today()
    print(">>>> ", d)
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
