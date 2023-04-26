from typing import List
from dataclasses import dataclass


@dataclass
class Transaction:
    """
    Класс Transaction представляет информацию о финансовой транзакции.
    Атрибуты:
    id (int): идентификатор транзакции.
    state (str): статус транзакции, возможные значения: EXECUTED, CANCELED.
    date (str): дата выполнения транзакции в формате ГГГГ-ММ-ДДTЧЧ:ММ:СС.МСК.
    amount (float): сумма операции.
    currency (str): название валюты операции.
    description (str): описание операции.
    from_account (str): номер счета или карты, с которого была произведена операция.
    to_account (str): номер счета или карты, на который была произведена операция.
    """
    id: int
    state: str
    date: str
    amount: float
    currency: str
    description: str
    from_account: str
    to_account: str


def load_tran_transactions_from_json(file_path: str) -> List[Transaction]:
    """
    Функция загрузки списка транзакций из JSON файла
    и преобразование его в список объектов класса Transaction.
    :param file_path: JSON файл.
    :return: список объектов класса Transaction.
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    transactions = []
    for item in data:
        transactions.append(Transaction(
            id=item['id'],
            state=item['state'],
            date=item['date'],
            amount=float(item['operationAmount']['amount']),
            currency=item['operationAmount']['currency']['name'],
            description=item['description'],
            from_account=item['from'],
            to_account=item['to']
        ))
        return transactions


def get_last_transactions(transactions: List[Transaction], count: int = 5) -> List[Transaction]:
    """
    Функция получения последней транзакции из списка объектов класса Transaction.
    :param transactions: список объектов класса Transaction.
    :param count: количество транзакций.
    :return: список объектов класса Transaction.
    """
    return sorted(transactions, key=lambda t: t.date, reverse=True)[:count]
