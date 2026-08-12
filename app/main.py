import datetime
from typing import List, Dict


def outdated_products(products: List[Dict]) -> List[str]:

    today = datetime.date.today()
    return [
        product["name"]
        for product in products
        if product["expiration_date"] < today
    ]
