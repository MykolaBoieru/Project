from db import add_counter, increment_counter, delete_the_habit


class Habit:

    def __init__(self, name: str, description: str):
        """
        Counter class, to count events
        :param name: name of the habit
        :param description: description of the habit
        """
        self.name = name
        self.description = description
        self.category = ""
        self.frequency = 0
        self.count = 0

    def increment(self):
        """
        This function increments the count
        """
        self.count += 1

    def reset(self):
        """
        This function resets a counter
        :return: reset count
        """
        self.count = 0

    def __str__(self):
        """
        This function defines how the object will be printed
        :return: new string
        """
        return f"{self.name}: {self.count}"

    def store(self, db):
        """
        This function is responsible for storing habits in database
        :param db: an initialized sqlite3 database connection
        """
        add_counter(db, self.name, self.description, self.category, self.frequency)

    def add_event(self, db, date: str = None):
        """
        This function is responsible for adding an event in database
        :param db: an initialized sqlite3 database connection
        :param date: the current date of the event
        """
        increment_counter(db, self.name, date)

    def delete(self, db, name):
        """
        This function deletes the habit from the database
        """
        delete_the_habit(db, self.name)
