import datetime
import pytest
from unittest import mock


from app.main import outdated_products


@pytest.fixture()
def mocked_datetime_date():
    with mock.patch('datetime.date') as mocked:
        yield mocked


@pytest.mark.parametrize(
    'error, products, current_date',
    [
        pytest.param(
            KeyError,
            [
                {
                    'expiration_date': datetime.date(2022, 1, 9),
                    'price': 0,
                },
            ],
            datetime.date(2022, 1, 10),
            id="Raise KeyError when 'name' not in product"
        ),
        pytest.param(
            KeyError,
            [
                {
                    'name': 'name_1',
                    'price': 100,
                },
            ],
            datetime.date(2000, 1, 1),
            id="Raise KeyError when 'expiration_date' not in product"
        )
    ]
)
def test_not_valid_data(
        mocked_datetime_date,
        error,
        products,
        current_date
):

    with pytest.raises(error):
        mocked_datetime_date.today.return_value = current_date
        print(outdated_products(products))


@pytest.mark.parametrize(
    'current_date, products, awaited_value',
    [
        pytest.param(
            datetime.date(2022, 1, 10),
            [
                {
                    'name': 'name_1',
                    'expiration_date': datetime.date(2022, 1, 9),
                    'price': 0,
                },
                {
                    'name': 'name_2',
                    'expiration_date': datetime.date(2022, 1, 12),
                    'price': 500,
                }
            ],
            ['name_1'],
            id='Test valid data with all keys'
        ),
        pytest.param(
            datetime.date(2022, 1, 10),
            [
                {
                    'name': 'name_1',
                    'expiration_date': datetime.date(2022, 1, 9),
                },
                {
                    'name': 'name_2',
                    'expiration_date': datetime.date(2022, 1, 12),
                }
            ],
            ['name_1'],
            id='Test valid data without price key'
        ),
    ]
)
def test_valid_products(
        mocked_datetime_date,
        current_date,
        products,
        awaited_value,
):
    mocked_datetime_date.today.return_value = current_date
    assert outdated_products(products) == awaited_value
