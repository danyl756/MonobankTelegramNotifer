import flask # type: ignore
from config import MONOBANK_ACCOUNT_ID, CURRENCY_CODE
from process_data import add_transaction

app = flask.Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = flask.request.json
    process_webhook_data(data)
    return 'OK', 200
@app.route('/webhook', methods=['GET'])
def webhook_get():
    return 'OK', 200
def process_webhook_data(data):
    account = data['data']['account']
    statementItem = data['data']['statementItem']
    time = statementItem['time']
    description = statementItem['description']
    amount = statementItem['amount']
    currencyCode = statementItem['currencyCode']
    balance = statementItem ['balance']
    if check_webhook_data(account, currencyCode):
        add_transaction(time, amount, description, currencyCode, balance)
    pass
def check_webhook_data(account, currencyCode):
    if account == MONOBANK_ACCOUNT_ID and currencyCode == CURRENCY_CODE:
        return True
    return False
if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')