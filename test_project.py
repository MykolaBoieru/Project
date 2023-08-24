from habit import Habit
from db import get_db, add_counter, increment_counter, get_counter_data
from analyse import calculate_count
import os


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")

        add_counter(self.db, "Learning Python", "To learn Python at least four hours every day", "study", 1)
        increment_counter(self.db, "Learning Python", "2023-08-14")
        increment_counter(self.db, "Learning Python", "2023-08-15")
        increment_counter(self.db, "Learning Python", "2023-08-16")
        increment_counter(self.db, "Learning Python", "2023-08-17")
        increment_counter(self.db, "Learning Python", "2023-08-18")
        increment_counter(self.db, "Learning Python", "2023-08-19")
        increment_counter(self.db, "Learning Python", "2023-08-20")
        increment_counter(self.db, "Learning Python", "2023-08-21")
        increment_counter(self.db, "Learning Python", "2023-08-22")
        increment_counter(self.db, "Learning Python", "2023-08-23")
        increment_counter(self.db, "Learning Python", "2023-08-24")

        add_counter(self.db, "More sport", "To do more sport activities", "sport", 7)
        increment_counter(self.db, "More sport", "2023-07-13")
        increment_counter(self.db, "More sport", "2023-07-20")
        increment_counter(self.db, "More sport", "2023-07-27")
        increment_counter(self.db, "More sport", "2023-08-03")
        increment_counter(self.db, "More sport", "2023-08-10")
        increment_counter(self.db, "More sport", "2023-08-17")
        increment_counter(self.db, "More sport", "2023-08-24")



    def test_counter(self):

        test_habit = Habit("Learning Python", "To learn Python at least four hours every day")

        test_habit.increment()
        test_habit.add_event(self.db)
        test_habit.reset()
        test_habit.increment()

    def test_db_counter(self):
        self.db = get_db("test.db")
        data = get_counter_data(self.db, "Learning Python")
        assert len(data) == 12

        count = calculate_count(self.db, "Learning Python")
        assert count == 12

        data = get_counter_data(self.db, "More sport")
        assert len(data) == 7

        count = calculate_count(self.db, "More sport")
        assert count == 7

    def teardown_method(self):
        os.remove("test.db")
