import datetime
from typing import Any, Dict, List


def outdated_products(products: List[Dict[str, Any]]) -> List[str]:
    today = datetime.date.today()
    expired = []

    for product in products:
        if product["expiration_date"] < today:
            expired.append(product["name"])

    return expired
