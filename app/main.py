from datetime import date


def outdated_products(products: list) -> list:
    today = date.today()
    return [product["name"] for product in products
            if product["expiration_date"] < today]
