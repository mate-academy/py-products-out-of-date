import datetime as _stdlib_datetime

# Subclasse Python de datetime.date — permite mocks em testes
class Date(_stdlib_datetime.date):
    @classmethod
    def today(cls):
        return _stdlib_datetime.date.today()

class _DatetimeModule:
    date = Date

# Expondo 'datetime' para testes (mockers)
datetime = _DatetimeModule()

def outdated_products(products: list) -> list:
    return [
        product["name"]
        for product in products
        if product["expiration_date"] < datetime.date.today()
    ]
