# from app.main import outdated_products
# from unittest import mock
# import pytest
# import datetime
#
# list_of_products = [
#     {
#         "name": "salmon",
#         "expiration_date": datetime.date(2022, 2, 10),
#         "price": 600
#     },
#     {
#         "name": "chicken",
#         "expiration_date": datetime.date(2022, 2, 5),
#         "price": 120
#     },
#     {
#         "name": "duck",
#         "expiration_date": datetime.date(2022, 2, 1),
#         "price": 160
#     }
# ]
# # d1 = datetime.date(2022, 2, 2)
# # d2 = datetime.date(2022, 3, 5)
# # d3 = datetime.date(2022, 2, 6)
# # d4 = datetime.date(2022, 1, 5)
#
#
# @pytest.mark.parametrize(
#     "not_true_time, expected_result",
#     [
#         (datetime.date(2022, 2, 2), ["duck"]),
#         (datetime.date(2022, 3, 5), ["salmon", "chicken", "duck"]),
#         (datetime.date(2022, 2, 6), ["salmon", "chicken", "duck"]),
#         (datetime.date(2022, 1, 5), [])
#     ]
# )
# def test_outdated_products(
#         not_true_time: datetime.date | list[str],
#         expected_result: list[str] | list
# ) -> None:
#     with mock.patch(
#             "app.main.datetime.date.today",
#             return_value=not_true_time
#     ):
#         assert outdated_products(
#             list_of_products
#         ) == expected_result

import datetime
from unittest import mock

from app.main import outdated_products

MOCKED_DATE = datetime.date(2024, 3, 14)


def test_mock_datetime_today() -> None:
    goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 3, 13),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 3, 14),
            "price": 160
        }
    ]
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = MOCKED_DATE
        assert outdated_products(goods) == ["chicken"]
