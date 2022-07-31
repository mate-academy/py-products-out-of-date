import pytest

import datetime

from unittest import mock

from app.main import outdated_products


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
        with mock.patch('app.main.datetime') as mocked_time:
            mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
            assert outdated_products(product) == func_feedback
