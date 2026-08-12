import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]
#
# print(outdated_products([
#     {
#         "name": "salmon",
#         "expiration_date": datetime.date(2022, 10, 28),
#         "price": 600
#     },
#     {
#         "name": "chicken",
#         "expiration_date": datetime.date(2022, 10, 27),
#         "price": 120
#     },
#     {
#         "name": "duck",
#         "expiration_date": datetime.date(2022, 10, 28),
#         "price": 160
#     }
# ]))
