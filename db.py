import sqlite3
from datetime import date


def get_db(name="main.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT PRIMARY KEY, 
        description TEXT,
        category TEXT,
        frequency INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        counterName TEXT,
        FOREIGN KEY (counterName) REFERENCES counter(name))""")

    db.commit()


def add_counter(db, name, description, category, frequency):
    cur = db.cursor()
    cur.execute("INSERT INTO counter VALUES (?, ?, ?, ?)", (name, description, category, frequency))
    db.commit()


def increment_counter(db, name, event_date=None):
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
        cur.execute("INSERT INTO tracker VALUES (?, ?)", (event_date, name))
        db.commit()


def get_counter_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker  WHERE counterName=?", (name,))
    return cur.fetchall()


def get_table_of_habits(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM counter")
    return cur.fetchall()


def delete_the_habit(db, name):
    cur = db.cursor()
    cur.execute(f"DELETE FROM counter WHERE name=?", (name,))
    db.commit()
