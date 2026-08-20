import sqlite3
from pathlib import Path

# Database ફાઈલ ક્યાં Save થશે
DB_PATH = Path.home() / ".dharam_window" / "dharam.db"

class DBManager:
    def __init__(self):
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(DB_PATH))
        self.create_tables()

    def create_tables(self):
        # Window નું ટેબલ
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS windows(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT,
                width REAL,
                height REAL,
                rate REAL,
                total REAL
            )
        """)
        # Bill નું ટેબલ
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS bills(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bill_no TEXT,
                date TEXT,
                client_name TEXT,
                amount REAL
            )
        """)
        self.conn.commit()

    def add_window(self, client, w, h, rate):
        total = w * h * rate
        self.conn.execute("INSERT INTO windows(client_name,width,height,rate,total) VALUES(?,?,?,?,?)",
                          (client, w, h, rate, total))
        self.conn.commit()
        return total

    def get_all_windows(self):
        cur = self.conn.execute("SELECT * FROM windows")
        return cur.fetchall()
