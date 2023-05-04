
#  "Operations on accounts"

## Widget

***
This is a widget that shows the client's last few successful banking transactions.
***

* transfer date
* translation description
* from -> where
* transfer amount currency

'''

def convert_transactions(data: List[dict]) -> List[Transaction]:

    transactions = []
    for item in data:
        if 'from' in item and item['state'] == 'EXECUTED':
            transactions.append(Transaction(
                id=item['id'],
                state=item['state'],
                date=item['date'],
                amount=float(item['operationAmount']['amount']),
                currency=item['operationAmount']['currency']['name'],
                description=item['description'],
                from_account=item["from"],
                to_account=item['to']
            ))

    return transactions

'''