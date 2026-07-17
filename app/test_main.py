import pytest
import datetime
from unittest.mock import patch, MagicMock
from app import main


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "products,expired_products",
        [
            (
                [{"name": "chicken",
                  "expiration_date": datetime.date(2026, 8, 10)
                  }],
                []
            ),
            (
                [{"name": "chicken",
                  "expiration_date": datetime.date(2026, 7, 17)
                  }],
                []
            ),
            (
                [{"name": "chicken",
                  "expiration_date": datetime.date(2026, 7, 16)
                  }],
                ["chicken"]
            ),
            (
                [{"name": "chicken",
                  "expiration_date": datetime.date(2026, 4, 19)
                  }],
                ["chicken"]
            ),

        ],
        ids=[
            "Product up to date",
            "Expiration date is today",
            "Expired yesterday",
            "Expired product",
        ]
    )
    @patch("app.main.datetime")
    def test_outdated_products(
        self,
        mock_datetime: MagicMock,
        products: list,
        expired_products: list
    ) -> None:
        mock_datetime.date.today.return_value = datetime.date(2026, 7, 17)
        assert main.outdated_products(products) == expired_products
