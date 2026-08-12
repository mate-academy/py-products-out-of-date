import datetime
from unittest.mock import patch
import pytest
from app import main

MOCK_TODAY = datetime.date(2022, 2, 2)


def make_product(name: str, expiration_date: None, price: int = 100) -> None:
    return {"name": name, "expiration_date": expiration_date, "price": price}


@pytest.mark.parametrize(
    "products, expected",
    [
        # Single expired product
        ([make_product("duck", datetime.date(2022, 2, 1))], ["duck"],),
        # Single fresh product
        ([make_product("salmon", datetime.date(2022, 2, 10))], [],),
        # Expiring exactly today — NOT outdated (strict <)
        ([make_product("chicken", datetime.date(2022, 2, 2))], [],),
        # Mixed — only expired ones returned
        ([make_product("salmon",
                       datetime.date(2022, 2, 10)),
          make_product("chicken", datetime.date(2022, 2, 5)),
          make_product("duck", datetime.date(2022, 2, 1)), ], ["duck"],),
        # All outdated
        ([make_product("beef",
                       datetime.date(2022, 1, 30)),
          make_product("pork", datetime.date(2022, 1, 15)), ],
         ["beef", "pork"],),
        # All fresh
        ([make_product("salmon",
                       datetime.date(2022, 2, 10)),
          make_product("chicken", datetime.date(2022, 2, 5)),
          ], [],),
        # Empty list
        ([], [],),
    ],
)
@patch("app.main.datetime")
def test_outdated_products(mock_dt: None,
                           products: None,
                           expected: None) -> None:
    mock_dt.date.today.return_value = MOCK_TODAY
    assert main.outdated_products(products) == expected
