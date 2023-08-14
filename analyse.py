from db import get_counter_data
import sqlite3


def calculate_count(db, counter):
    """
    The function calculate how many times the habit has been incremented
    :param db: an initialized sqlite3 database connection
    :param counter:name of the habit in database
    :return:length of the counter increment events
    """
    data = get_counter_data(db, counter)
    return len(data)


def list_habits(db):
    """
    This function is responsible for getting a names of all habits
    :param db: an initialized sqlite3 database connection
    :return: a list of names of all added habits
    """
    connection = sqlite3.connect(db)
    cur = connection.cursor()

    rows = cur.execute(f"SELECT name FROM counter")
    listed_rows = [list(row)[0] for row in rows]

    return listed_rows




