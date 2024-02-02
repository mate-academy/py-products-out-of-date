import datetime


def outdated_products(products: list) -> list:
    print(">>> ", datetime.date.today())
    print("PRODUCTS >>> ", products)
    print(
        "RETURN >>> ", [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
    )
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
