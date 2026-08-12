from datetime import date
from typing import List, Dict


def outdated_products(products: List[Dict]) -> List[str]:
    today = date.today()
    return [
        product["name"]
        for product in products
        if product["expiration_date"] < today
    ]
