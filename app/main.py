import datetime


def outdated_products(products: list) -> list:
    outdated = []
    today = datetime.date.today()
    for product in products:
        if product["expiration_date"] < today:
            outdated.append(product["name"])
    return outdated
