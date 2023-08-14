from habit import Habit
from db import get_db, add_counter, increment_counter, get_counter_data
from analyse import calculate_count


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")

        add_counter(self.db, "test_counter", "test_description", "study", 1)
        increment_counter(self.db, "test_counter", "2023-08-02")
        increment_counter(self.db, "test_counter", "2023-08-03")

        increment_counter(self.db, "test_counter", "2023-08-04")
        increment_counter(self.db, "test_counter", "2023-08-05")

    def test_counter(self):
        counter = Habit("test_counter_1", "test_description_1")
        counter.store(self.db)

        counter.increment()
        counter.add_event(self.db)
        counter.reset()
        counter.increment()

    def test_db_counter(self):
        self.db = get_db("test.db")
        data = get_counter_data(self.db, "test_counter")
        assert len(data) == 4

        count = calculate_count(self.db, "test_counter")
        assert count == 4

    def teardown_method(self):
        import os
        os.remove("test.db")
