import datetime
from unittest import mock

import pytest

from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "expiration_date,verification_date,result",
        [
            (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    }
                ], datetime.date(2022, 2, 11), ["salmon"]
            ),
            (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    }
                ], datetime.date(2022, 2, 9), []
            ),
            (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    }
                ], datetime.date(2022, 2, 10), []
            )
        ]
    )
    def test_expiration_date(
        self,
        expiration_date: list,
        verification_date: datetime,
        result: str
    ) -> None:
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = verification_date
            assert outdated_products(expiration_date) == result
