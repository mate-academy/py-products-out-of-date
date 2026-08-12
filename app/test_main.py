import datetime
from app.main import outdated_products


def test_date_of_goods() -> None:
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2025, 2, 10),
        "price": 600
    },
        {
        "name": "salm",
        "expiration_date": datetime.date(2022, 12, 29),
        "price": 600
    },
        {
        "name": "salo",
        "expiration_date": datetime.date(2022, 12, 30),
        "price": 600
    }
    ]) == ["salm"]
