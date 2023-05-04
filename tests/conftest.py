import pytest

from src.transaction import Transaction


@pytest.fixture
def data_transactions():
    return [
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
    ]


@pytest.fixture()
def valid_transaction(data_transactions):
    item = data_transactions[0]
    return Transaction(
                id=item['id'],
                state=item['state'],
                date=item['date'],
                amount=float(item['operationAmount']['amount']),
                currency=item['operationAmount']['currency']['name'],
                description=item['description'],
                from_account=item["from"],
                to_account=item['to']
            )


@pytest.fixture()
def transactions():
    """
    Фикстура возвращает список объектов класса Transaction для тестирования функции get_last_transactions.
    """
    return [
        Transaction(id=104807525, state='EXECUTED', date='2019-06-01T06:46:16.803326', amount=60888.63, currency='RUB',
                    description='Transaction 1', from_account='МИР 6664', to_account='Счет 9956'),
        Transaction(id=464419177, state='CANCELED', date='2018-07-15T18:44:13.346362', amount=71024.64, currency='RUB',
                    description='Transaction 2', from_account='Visa 2945', to_account='Счет 4261'),
        Transaction(id=560813069, state='CANCELED', date='2019-12-03T04:27:03.427014', amount=17628.50, currency='USD',
                    description='Transaction 3', from_account='MasterCard 9527', to_account='Visa 9288'),
        Transaction(id=894961746, state='EXECUTED', date='2019-08-04T20:17:25.443322', amount=2523.44, currency='RUB',
                    description='Transaction 4', from_account='Счет 3372', to_account='Счет 6877'),
        Transaction(id=636137913, state='EXECUTED', date='2019-06-16T22:17:01.825020', amount=24260.78, currency='USD',
                    description='Transaction 5', from_account='Visa 8990', to_account='Счет 1557')
    ]



