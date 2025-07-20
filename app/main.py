import datetime

def get_today() -> datetime:
    return datetime.date.today()

def outdated_products(products: list[dict]) -> list[str]:
    today = get_today()
    return [p["name"] for p in products if p["expiration_date"] < today]
