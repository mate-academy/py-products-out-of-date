import pytest

import datetime

from app.main import outdated_products


class NewDate(datetime.date):
    @classmethod
    def today(cls):
        return cls(2022, 2, 2)


datetime.date = NewDate


class TestMain:

    @pytest.mark.parametrize(
        "expiration_date, func_feedback",
        [
            pytest.param(datetime.date(2022, 2, 2), [],
                         id="should return []"
                            "if expiration_date = date today"),
            pytest.param(datetime.date(2022, 2, 1), ["salmon"],
                         id="should return product name"
                            "if expiration_date < date today"),
            pytest.param(datetime.date(2022, 2, 3), [],
                         id="should return [] "
                            "if expiration_date > date today")
        ]
    )
    def test_outdated_products(self,
                               expiration_date,
                               func_feedback):
        product = [{"name": "salmon",
                    "expiration_date": expiration_date,
                    "price": 600}]
        assert outdated_products(product) == func_feedback
