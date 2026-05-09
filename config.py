import os

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
MONOBANK_ACCOUNT_ID = os.getenv('MONOBANK_ACCOUNT_ID')
CURRENCY_CODE = os.getenv('CURRENCY_CODE', 'USD')
DB_NAME = os.getenv('DB_NAME', 'transactions')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = 'db'
DB_PORT = '5432'