from datetime import date


def outdated_products(products: list) -> list:
    current_date = date.today()
    outdated = []
    for product in products:
        if product["expiration_date"] <= current_date:
            outdated.append(product["name"])
    return outdated
