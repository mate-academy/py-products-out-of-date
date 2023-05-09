import datetime
import pytest

from unittest.mock import patch, MagicMock

from app.main import outdated_products


@pytest.fixture
def mocked_date() -> MagicMock:
    with patch("datetime.date") as mock_date:
        yield mock_date


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "current_date,products,expected_result",
        [
            (
                datetime.date(2022, 2, 2),
                [
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 160
                    },
                ],
                ["duck"]
            ),
            (
                datetime.date(2022, 2, 1),
                [
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 160
                    }
                ],
                []
            ),
            (
                datetime.date(2022, 1, 30),
                [
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 160
                    }
                ],
                []
            )
        ],
        ids=[
            "returns 'name' when 'expiration_date' is less than current date",
            "returns empty list when 'expiration_date' equal to current_date",
            "returns empty list when current_date less than 'expiration_date'"
        ]
    )
    def test_outdated_products(
            self,
            current_date: datetime,
            products: list,
            expected_result: list,
            mocked_date: MagicMock
    ) -> None:
        mocked_date.today.return_value = current_date
        result = outdated_products(products)
        assert result == expected_result


class TestOutdatedProductsErrors:
    @pytest.mark.parametrize(
        "products,expected_error",
        [
            (
                [
                    {
                        "name": "salmon",
                        "price": 600
                    },
                ],
                KeyError
            ),
            (
                [
                    {
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    }
                ],
                KeyError
            ),
            (
                [
                    {
                        "name": "duck",
                        "expiration_date": "2022-02-02",
                        "price": 160
                    }
                ],
                TypeError
            ),
        ],
        ids=[
            "KeyError when no 'expiration_date' key",
            "KeyError when no 'name' key",
            "TypeError when 'expiration_date' type is not 'datetime.date'",

        ]
    )
    def test_raise_key_error_when_no_needed_key_have_found(
            self,
            products: list,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            outdated_products(products)
