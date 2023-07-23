import datetime
from pytest import fixture, mark
from unittest import mock

from app.main import outdated_products


@fixture
def products_list_template() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@mark.parametrize(
    "today_date, return_list",
    [
        (
                datetime.date(2022, 2, 1),
                []
        ),
        (
                datetime.date(2022, 2, 5),
                ["duck"]
        ),
        (
                datetime.date(2022, 2, 10),
                ["chicken", "duck"]
        ),
        (
                datetime.date(2022, 2, 11),
                ["salmon", "chicken", "duck"]
        )
    ],
    ids=[
        "should return empty list when no outdated products",
        "when 1 product is outdated should return list with it",
        "when 2 products are outdated should return list with them",
        "when 3 products is outdated should return list with them"
    ]
)
def test_if_determines_outdated_products_correctly(
        products_list_template: list[dict],
        today_date: datetime,
        return_list: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = today_date
        assert outdated_products(products_list_template) == return_list
