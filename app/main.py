import datetime


def outdated_products(products: list):
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]


# products = [
#         {
#             "name": "salmon",
#             "expiration_date": datetime.date(2022, 9, 30),
#             "price": 600
#         },
#         {
#             "name": "chicken",
#             "expiration_date": datetime.date(2022, 9, 22),
#             "price": 120
#         },
#         {
#             "name": "duck",
#             "expiration_date": datetime.date(2022, 9, 21),
#             "price": 160
#         }
#     ]
#
# print(outdated_products(products))
