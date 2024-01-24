import datetime
from app.main import outdated_products


def test_return_func_value() -> None:
    assert outdated_products([
        {"name": "pro1",
         "expiration_date": datetime.date(2024, 1, 25)
         },
        {"name": "pro2",
         "expiration_date": datetime.date(2024, 1, 23)
         },
        {"name": "pro3",
         "expiration_date": datetime.date(2024, 1, 24)
         }
    ]) == ["pro2"]
