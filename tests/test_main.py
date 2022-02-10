import pytest
import datetime
from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "exp_1_date, exp_2_date, "
        "exp_3_date, exp_4_date, "
        "exp_5_date, expected_list",
        [
            pytest.param(
                datetime.date(2022, 2, 4),
                datetime.date(2023, 1, 3),
                datetime.date(2022, 1, 10),
                datetime.date(2022, 2, 5),
                datetime.date(1999, 12, 31),
                ["salmon", "milk", "duck"],
                id="first last medium products outdated"
            ),
            pytest.param(
                datetime.date(2022, 2, 5),
                datetime.date(2022, 3, 3),
                datetime.date(2023, 1, 1),
                datetime.date(2022, 8, 31),
                datetime.date(3000, 12, 31),
                [],
                id="all product fresh"
            )
        ]
    )
    def test_different_dates(
            self,
            exp_1_date,
            exp_2_date,
            exp_3_date,
            exp_4_date,
            exp_5_date,
            expected_list
    ):
        class NewDate(datetime.date):
            @classmethod
            def today(cls):
                return cls(2022, 2, 5)

        # datetime.date.today = mock.MagicMock
        # datetime.date = (2022, 2, 5)
        datetime.date = NewDate
        products = [
            {
                "name": "salmon",
                "expiration_date": exp_1_date,
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": exp_2_date,
                "price": 120
            },
            {
                "name": "milk",
                "expiration_date": exp_3_date,
                "price": 30
            },
            {
                "name": "meat",
                "expiration_date": exp_4_date,
                "price": 115
            },
            {
                "name": "duck",
                "expiration_date": exp_5_date,
                "price": 160
            }
        ]
        assert outdated_products(products) == expected_list

    @pytest.mark.parametrize(
        "products, expected_error",
        [
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": None,
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": "2022-03-03",
                        "price": 120
                    },
                    {
                        "name": "milk",
                        "expiration_date": datetime.date(2023, 1, 1),
                        "price": 30
                    },
                    {
                        "name": "meat",
                        "expiration_date": datetime.date(2022, 8, 31),
                        "price": 115
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(3000, 12, 31),
                        "price": 160
                    }
                ],
                TypeError,
                id="should raise error when 'expiration_date' "
                   "is not datetime class"
            ),
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "price": 600
                    },
                    {
                        "name": "milk",
                        "expiration_date": datetime.date(2023, 1, 1),
                        "price": 30
                    },
                    {
                        "name": "meat",
                        "expiration_date": datetime.date(2022, 8, 31),
                        "price": 115
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(3000, 12, 31),
                        "price": 160
                    }
                ],
                KeyError,
                id="should raise error when no key 'expiration_date'"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            products,
            expected_error
    ):
        class NewDate(datetime.date):
            @classmethod
            def today(cls):
                return cls(2022, 2, 5)

        datetime.date = NewDate
        with pytest.raises(expected_error):
            outdated_products(products)

    def test_initial_list_is_not_changed(self):
        class NewDate(datetime.date):
            @classmethod
            def today(cls):
                return cls(2022, 2, 5)

        datetime.date = NewDate
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 4),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2023, 1, 3),
                "price": 120
            },
            {
                "name": "milk",
                "expiration_date": datetime.date(2022, 1, 10),
                "price": 30
            },
            {
                "name": "meat",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 115
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(1999, 12, 31),
                "price": 160
            }
        ]
        initial_id = id(products)
        outdated_products(products)
        assert initial_id == id(products)

    def test_empty_initial_list(self):
        class NewDate(datetime.date):
            @classmethod
            def today(cls):
                return cls(2022, 2, 5)

        datetime.date = NewDate
        products = []
        assert outdated_products(products) == []

    def test_one_product_in_initial_list(self):
        class NewDate(datetime.date):
            @classmethod
            def today(cls):
                return cls(2022, 2, 5)

        datetime.date = NewDate
        products = [
            {
                "name": "duck",
                "expiration_date": datetime.date(2021, 12, 31),
                "price": 160
            }
        ]
        assert outdated_products(products) == ["duck"]
