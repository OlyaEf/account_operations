from typing import List
from dataclasses import dataclass


@dataclass
class Transaction:
    id: int
    state: str
    date: str
    amount: float
    currency: str
    description: str
    from_account: str
    to_account: str

