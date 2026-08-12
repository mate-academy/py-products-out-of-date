import datetime
import pytest


class NewDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 5)


@pytest.fixture()
def mocked_datetime_date_today() -> None:
    datetime.date = NewDate


def test_datetime_date_today(mocked_datetime_date_today: None) -> None:
    today = datetime.date.today()
    assert today == datetime.date(2022, 2, 5)
