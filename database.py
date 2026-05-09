import psycopg2 # type: ignore
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id SERIAL PRIMARY KEY,
                time TEXT,
                amount DOUBLE PRECISION NOT NULL,
                description TEXT,
                currency_code INTEGER,
                balance DOUBLE PRECISION
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                chat_id BIGINT UNIQUE NOT NULL
            )
        """)

        self.connection.commit()

    def add_transaction(self, time, amount, description, currency_code, balance):
        self.cursor.execute("""
            INSERT INTO transactions (time, amount, description, currency_code, balance)
            VALUES (%s, %s, %s, %s, %s)
        """, (time, amount, description, currency_code, balance))

        self.connection.commit()

    def get_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    def get_transactions_by_id(self, transaction_id):
        self.cursor.execute(
            "SELECT * FROM transactions WHERE id = %s",
            (transaction_id,)
        )
        return self.cursor.fetchone()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def add_user(self, chat_id):
        self.cursor.execute("""
            INSERT INTO users (chat_id)
            VALUES (%s)
            ON CONFLICT (chat_id) DO NOTHING
        """, (chat_id,))

        self.connection.commit()