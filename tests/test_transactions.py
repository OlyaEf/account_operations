import json
from datetime import datetime
from unittest import mock

from src.transaction import convert_transactions, get_last_transactions, load_transactions_from_json, Transaction


def test_convert_transactions(data_transactions, valid_transaction):
    transactions = convert_transactions(data_transactions)
    assert transactions[0] == valid_transaction


def test_get_last_transactions(transactions):
    last_transactions = get_last_transactions(transactions, count=3)
    assert len(last_transactions) == 3
    sort_transactions = sorted(transactions, key=lambda t: datetime.fromisoformat(t.date), reverse=True)
    assert last_transactions == sort_transactions[:3]


def test_load_transactions_from_json(tmp_path):
    test_data = [
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
        }
    ]
    test_file = tmp_path / "test.json"
    with open(test_file, "w") as f:
        json.dump(test_data, f)
    expected_transactions = [
        Transaction(
            id=921286598,
            state="EXECUTED",
            date="2018-03-09T23:57:37.537412",
            amount=25780.71,
            currency="руб.",
            description="Перевод организации",
            from_account="Счет 26406253703545413262",
            to_account="Счет 20735820461482021315"
        )
    ]
    assert load_transactions_from_json(str(test_file)) == expected_transactions

