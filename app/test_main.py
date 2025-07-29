from pytest import mark, param
from unittest import mock
from datetime import date, timedelta
from app.main import outdated_products


curr_day = date.today()
yesterday = curr_day - timedelta(days=1)
test_day = date(2022, 2, 3)

test_days = curr_day, yesterday, test_day,

inp_data = [
    {
        "name": "salmon",
        "expiration_date": date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": date(2022, 2, 1),
        "price": 160
    }
]

outp_res = (
    ["duck"],
    ["salmon", "chicken", "duck"],
    ["salmon", "chicken", "duck"]
)


@mark.parametrize(
    ("inp_data,mock_day,outp_res"),
    [
        param(inp_data, test_days[2], outp_res[0], id="std_testcase"),
        param(inp_data, test_days[0], outp_res[0], id="today"),
        param(inp_data, test_days[1], outp_res[0], id="yesterday"),
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mock_today: object,
        mock_day: object,
        inp_data: list,
        outp_res: list) -> None:
    mock_today.today.return_value = mock_day
    mock_today.side_effect = lambda *args, **kw: date(*args, **kw)
    assert outdated_products(inp_data) == outp_res


if __name__ == "__main__":
    pass
