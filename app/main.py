import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]

products = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 10, 21),
            "price": 200
        },
        {
            "name": "fish",
            "expiration_date": datetime.date(2023, 10, 21),
            "price": 200
        },
        {
            "name": "rabbit",
            "expiration_date": datetime.date(2023, 10, 21),
            "price": 200
        }
    ]
print(datetime.date.today())
print(outdated_products(products))
