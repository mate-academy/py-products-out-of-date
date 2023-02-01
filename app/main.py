import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]


user = [{
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }]
print(datetime.date.today())