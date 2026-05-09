from database import Database
from telegram_bot import send_message
from messages import add_transaction_message
from datetime import datetime

def add_transaction(time, amount, description, currency_code, balance):
    with Database() as db:
        db.add_transaction(time, amount, description, currency_code, balance)
        users = db.get_users()
        amount = amount/100
        balance = balance/100
        date = datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')
    for user in users:
        print(user)
        send_message(user[1], add_transaction_message.format(date, amount, description, currency_code, balance))
        