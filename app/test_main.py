import datetime
import pytest
from _pytest.monkeypatch import MonkeyPatch
from unittest.mock import Mock
from app.main import outdated_products
from app.products import products


@pytest.mark.parametrize(
    "test_year, test_month, test_day, expected_outdated_products",
    [
        (2022, 2, 1, []),
        (2022, 2, 5, ["duck"]),
        (2022, 2, 10, ["duck", "chicken"]),
        (2022, 2, 11, ["duck", "chicken", "salmon"])
    ],
    ids=["no expired products", "one expired product",
         "two expired products", "all products expired"]
)
def test_outdated_products(
        monkeypatch: MonkeyPatch,
        test_year: int,
        test_month: int,
        test_day: int,
        expected_outdated_products: list
) -> None:
    mock_date_class = Mock(spec=datetime.date)
    mock_date_class.today.return_value = datetime.date(
        test_year, test_month, test_day
    )
    mock_date_class.side_effect = lambda *args, **kwargs: datetime.date(
        *args, **kwargs
    )

    mock_datetime_module = Mock(spec=datetime)
    mock_datetime_module.date = mock_date_class

    monkeypatch.setattr("app.main.datetime", mock_datetime_module)

    actual_expired_products = outdated_products(products)

    assert sorted(
        actual_expired_products
    ) == sorted(
        expected_outdated_products
    )
