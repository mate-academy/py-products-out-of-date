import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]


today = datetime.date.today()
current = datetime.date(2024, 2, 8)
print(current == today)
