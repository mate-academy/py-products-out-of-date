import datetime
import pytest
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ]


class NewDate:
    new_date = datetime.date(2022, 6, 6)

    @classmethod
    def today(cls) -> object:
        return cls.new_date


def test_should_return_empty_if_its_date_equal(
        monkeypatch: object,
        products_template: list
) -> None:
    NewDate.new_date = datetime.date(2022, 2, 10)

    monkeypatch.setattr(datetime, "date", NewDate)
    assert outdated_products(products_template) == []


def test_should_return_empty_if_its_date_was_yesterday(
        monkeypatch: object,
        products_template: list
) -> None:
    NewDate.new_date = (products_template[0]["expiration_date"]
                        + datetime.timedelta(days=1))

    monkeypatch.setattr(datetime, "date", NewDate)
    assert outdated_products(products_template) == ["salmon"]
